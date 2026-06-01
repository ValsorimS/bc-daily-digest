import json
import feedparser
import os
import time
from datetime import datetime

from google import genai
from google.genai.errors import ClientError

# Konfigurace
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
HISTORY_FILE = "history.json"

def get_processed_links():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_processed_links(data):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def summarize(text):
    prompt = (
        "Jsi expert na MS Dynamics 365 Business Central a AL. "
        "Shrň technické novinky pro zkušeného BC vývojáře. Zaměř se na AL, AI agenty a trendy. "
        "Analizuj text a napiš výstup v tomto formátu:\n"
        "1. První odstavec: Verdikt (ANO/NE) - shrň jednou větou, jestli má smysl článek číst.\n"
        "2. Následuje technické shrnutí ve 3 odrážkách (co je nového, technické detaily).\n"
        "Piš v češtině, buď extrémně technický a stručný.\n\n"
        f"Text k analýze: {text[:3000]}"
    )
    response = client.models.generate_content(
        # Vrátit: model='gemini-flash-latest',
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

# 1. Načtení historie a zdrojů
processed = get_processed_links()
with open('sources.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Sestavení kandidátů ze všech zdrojů
# Cíl: projít napřed nejnovější článek z KAŽDÉHO zdroje (po jednom),
# pak druhé nejnovější z každého zdroje atd. Když mezi běhy vznikne
# novější příspěvek, dostane přednost, protože se ve feedu objeví na
# pozici 0 (a tedy přeskočí starší články ostatních zdrojů).
candidates = []
for blog in data.get('blogs', []):
    feed = feedparser.parse(blog['url'])

    for index, entry in enumerate(feed.entries):
        if entry.link in processed:
            continue

        # Čas publikace pro řazení nejnovějších v rámci stejné pozice
        published = entry.get('published_parsed') or entry.get('updated_parsed')
        published_ts = time.mktime(published) if published else 0.0

        candidates.append({
            'feed_index': index,
            'published_ts': published_ts,
            'blog': blog,
            'entry': entry,
        })

# Řazení: napřed podle pozice ve feedu (0 = nejnovější v daném zdroji),
# při shodě podle data publikace (nejnovější první).
candidates.sort(key=lambda c: (c['feed_index'], -c['published_ts']))

# 3. Zpracování
count = 0
MAX_PER_RUN = 1

for cand in candidates:
    if count >= MAX_PER_RUN:
        break

    blog = cand['blog']
    entry = cand['entry']
    print(f"Zpracovávám: {entry.title}")

    try:
        # Sumarizace s ošetřením 429
        summary_text = summarize(entry.summary).strip()

        # Oddělovač excerptu vkládáme deterministicky v kódu,
        # protože model ho generuje nespolehlivě. Na úvodní stránce
        # se tak zobrazí pouze verdikt (první odstavec).
        summary_text = summary_text.replace("<!--více-->", "").strip()
        parts = summary_text.split("\n\n", 1)
        verdict = parts[0].strip()
        rest = parts[1].strip() if len(parts) > 1 else ""

        # Verdikt = excerpt (úvodní stránka), zbytek + odkaz až za oddělovačem
        content = f"{verdict}\n\n<!--více-->\n"
        if rest:
            content += f"\n{rest}\n"
        content += f"\n[Číst celý článek]({entry.link})"

        os.makedirs("_posts", exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"_posts/{date_str}-{blog['name'].replace(' ', '-').lower()}-{count}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"---\nlayout: post\ntitle: \"{blog['name']}: {entry.title}\"\npublished: true\n---\n\n{content}")

        processed[entry.link] = datetime.now().isoformat()
        save_processed_links(processed)
        count += 1

        # Exponenciální pauza pro prevenci 429 (začíná na 60s)
        time.sleep(65)

    except ClientError as e:
        if hasattr(e, 'code') and e.code == 429:
            print("Kvóta vyčerpána (429). Čekám na reset a končím.")
            # Ukončíme běh, kvóta je vyčerpaná
            break
        else:
            raise e

print("Hotovo. Zpracováno nových článků:", count)
