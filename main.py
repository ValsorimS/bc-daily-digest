import json
import feedparser
import os
import time
from datetime import datetime

from google import genai
from google.genai.errors import ClientError

# Konfigurace - používáme nového klienta
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
    # Volání nového API
    response = client.models.generate_content(
        # model='gemini-flash-latest',
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

# 1. Načtení historie a zdrojů
processed = get_processed_links()
with open('sources.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Zpracování (omezeno na 1 článek za běh pro úsporu kvóty)
count = 0
MAX_PER_RUN = 1 

for blog in data.get('blogs', []):
    feed = feedparser.parse(blog['url'])
    
    # Projdeme feed od nejstarších článků (backfilling)
    for entry in reversed(feed.entries):
        if count >= MAX_PER_RUN:
            break
            
        if entry.link not in processed:
            print(f"Zpracovávám: {entry.title}")
            # Sumarizace s "Verdiktem"
        try:
            summary_text = summarize(entry.summary)
        except ClientError as e:
            # V nové knihovně je kód chyby v e.code
            if hasattr(e, 'code') and e.code == 429:
                print("Kvóta vyčerpána (429). Končím tento běh, zkusím to příště.")
                break # Ukončíme smyčku for, ale skript doběhne úspěšně
            else:
                raise e # Jiné chyby chceme vidět
            
            # Formátování: Verdikt (před více) \n <!--více--> \n Zbytek (detail)
            # Předpokládáme, že model vrátí text, kde první řádky jsou verdikt
            content = f"{summary_text}\n\n[Číst celý článek]({entry.link})"
            
            # Vložení oddělovače pro Jekyll (zobrazí se jen text nad tímto tagem)
            # Pokud model nevrátí separátor, vložíme ho po prvním odstavci
            final_content = content.replace("\n\n", "\n\n<!--více-->\n\n", 1)

            # Uložení do souboru
            date_str = datetime.now().strftime("%Y-%m-%d")

            # Zajištění existence složky _posts
            os.makedirs("_posts", exist_ok=True)
            filename = f"_posts/{date_str}-{blog['name'].replace(' ', '-').lower()}-{count}.md"
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"---\nlayout: post\ntitle: \"{blog['name']}: {entry.title}\"\npublished: true\n---\n\n{final_content}")
            # Zápis do historie
            processed[entry.link] = datetime.now().isoformat()
            save_processed_links(processed)
            
            count += 1
            time.sleep(60) # Pauza mezi články pro klid Google API

print("Hotovo. Zpracováno nových článků:", count)
