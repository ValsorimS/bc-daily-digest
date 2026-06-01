import json
import feedparser
import os
import re
import time
from datetime import datetime

from google import genai
from google.genai.errors import ClientError, ServerError

# Konfigurace
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
HISTORY_FILE = "history.json"

# Browser-like UA – některé weby (Cloudflare apod.) blokují "robotí" UA
# a vrací 403 (např. waldo.be), takže by feed nevracel žádné články.
FEED_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

# Modely od preferovaného po záložní. Když je některý dočasně nedostupný
# (503) nebo neexistuje (404), zkusí se další v pořadí.
MODELS = [
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-flash-lite-latest",
]

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
    # Modely zkoušíme v pořadí podle MODELS. U každého pár pokusů
    # s krátkým backoffem na dočasné přetížení (503); když model nezabere,
    # přejdeme na další. 429 (vyčerpaná kvóta) propustíme ven – je účtová,
    # takže jiný model nepomůže a běh se ukončí čistě výš.
    attempts_per_model = 2
    last_error = None
    for model in MODELS:
        for attempt in range(1, attempts_per_model + 1):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                if model != MODELS[0]:
                    print(f"Použit záložní model: {model}")
                return response.text
            except ServerError as e:
                last_error = e
                if attempt == attempts_per_model:
                    print(f"Model {model} nedostupný (kód {getattr(e, 'code', '?')}) "
                          f"po {attempts_per_model} pokusech, zkouším další model.")
                    break
                wait = 15 * attempt
                print(f"Model {model} přetížen (kód {getattr(e, 'code', '?')}). "
                      f"Pokus {attempt}/{attempts_per_model}, čekám {wait}s.")
                time.sleep(wait)
            except ClientError as e:
                # 429 = vyčerpaná kvóta → fallback nepomůže, propustíme ven.
                if getattr(e, 'code', None) == 429:
                    raise
                # Jinak (404/400 – neplatný/nedostupný model) zkusíme další.
                last_error = e
                print(f"Model {model} odmítnut (kód {getattr(e, 'code', '?')}), "
                      f"zkouším další model.")
                break

    # Žádný model neuspěl – předáme poslední chybu k ošetření výš.
    if last_error is not None:
        raise last_error
    raise RuntimeError("Sumarizace selhala: žádný model není dostupný.")

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
    feed = feedparser.parse(blog['url'], agent=FEED_USER_AGENT)

    for index, entry in enumerate(feed.entries):
        if entry.link in processed:
            continue

        # Čas publikace pro řazení nejnovějších v rámci stejné pozice
        published = entry.get('published_parsed') or entry.get('updated_parsed')
        published_ts = time.mktime(published) if published else 0.0
        # Datum původního článku (jen pro zobrazení), prázdné když chybí
        original_date = time.strftime("%Y-%m-%d", published) if published else ""

        candidates.append({
            'feed_index': index,
            'published_ts': published_ts,
            'original_date': original_date,
            'blog': blog,
            'entry': entry,
        })

# Řazení: napřed podle pozice ve feedu (0 = nejnovější v daném zdroji),
# při shodě podle data publikace (nejnovější první).
candidates.sort(key=lambda c: (c['feed_index'], -c['published_ts']))

# 3. Zpracování
count = 0
MAX_PER_RUN = 3

for cand in candidates:
    if count >= MAX_PER_RUN:
        break

    blog = cand['blog']
    entry = cand['entry']
    original_date = cand['original_date']
    print(f"Zpracovávám: {entry.title}")

    try:
        # Sumarizace s ošetřením 429
        summary_text = summarize(entry.summary).strip()

        # Oddělovač excerptu vkládáme deterministicky v kódu,
        # protože model ho generuje nespolehlivě. Na úvodní stránce
        # se tak zobrazí pouze verdikt (první řádek). Dělíme na prvním
        # zalomení řádku, ne na prázdném řádku – model občas mezi verdikt
        # a shrnutí prázdný řádek nevloží a pak by se do excerptu dostalo
        # celé shrnutí.
        summary_text = summary_text.replace("<!--více-->", "").strip()
        parts = summary_text.split("\n", 1)
        verdict = parts[0].strip()
        # Odstraníme vedoucí číslování verdiktu (např. "1.  "), jinak by se
        # excerpt na úvodní stránce vykreslil jako číslovaný seznam.
        # Shrnutí (rest) je za <!--více-->, není v excerptu a "2." tam drží
        # odsazení vnořených odrážek, proto ho necháváme být.
        verdict = re.sub(r'^\s*\d+[.)]\s*', '', verdict)
        rest = parts[1].strip() if len(parts) > 1 else ""

        # Verdikt = excerpt (úvodní stránka), zbytek + odkaz až za oddělovačem
        content = f"{verdict}\n\n<!--více-->\n"
        if rest:
            content += f"\n{rest}\n"
        content += f"\n[Číst celý článek]({entry.link})"

        os.makedirs("_posts", exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"_posts/{date_str}-{blog['name'].replace(' ', '-').lower()}-{count}.md"

        front_matter = (
            "---\n"
            "layout: post\n"
            f"title: \"{blog['name']}: {entry.title}\"\n"
            "published: true\n"
        )
        # Datum původního článku pro zobrazení vedle data zpracování
        if original_date:
            front_matter += f"original_date: {original_date}\n"
        front_matter += "---\n\n"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(front_matter + content)

        processed[entry.link] = datetime.now().isoformat()
        save_processed_links(processed)
        count += 1

        # Exponenciální pauza pro prevenci 429 (začíná na 60s)
        time.sleep(65)

    except ServerError as e:
        # Model je nedostupný i po opakovaných pokusech. Článek
        # neoznačíme jako zpracovaný a zkusíme ho při příštím běhu –
        # běh ukončíme čistě, ať workflow nehlásí chybu.
        print(f"Model nedostupný (kód {getattr(e, 'code', '?')}) i po opakování. "
              f"Končím, zkusím při příštím běhu.")
        break

    except ClientError as e:
        if hasattr(e, 'code') and e.code == 429:
            print("Kvóta vyčerpána (429). Čekám na reset a končím.")
            # Ukončíme běh, kvóta je vyčerpaná
            break
        else:
            raise e

print("Hotovo. Zpracováno nových článků:", count)
