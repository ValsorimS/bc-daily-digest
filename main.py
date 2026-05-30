import json
import feedparser
import google.generativeai as genai
import os
import time
from datetime import datetime

# Konfigurace
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-flash-latest')

def summarize(text):
    prompt = (
        "Jsi expert na Microsoft Dynamics 365 Business Central a AL programování. "
        "Tvým úkolem je shrnout tento text pro zkušeného BC vývojáře. "
        "Zaměř se primárně na technické novinky v AL, Business Central a na to, "
        "jak dané téma souvisí s trendem AI agentů a moderním programováním. "
        "Buď maximálně technický, stručný a piš v češtině. "
        "Výstup dej do 3 krátkých odrážek.\n\n"
        f"Text k analýze: {text[:3000]}"
    )
    response = model.generate_content(prompt)
    return response.text

# Načtení dat
with open('sources.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Iterace přes všechny blogy
for blog in data.get('blogs', []):
    print(f"Zpracovávám: {blog['name']}...")
    feed = feedparser.parse(blog['url'])
    
    if feed.entries:
        entry = feed.entries[0]
        
        # Sumarizace
        summary_text = summarize(entry.summary)
        
        content = f"# {entry.title}\n\n{summary_text}\n\n[Číst celý článek]({entry.link})"

        # Uložení do souboru
        # Přidáme identifikátor blogu do názvu souboru, aby se nepřepisovaly
        date_str = datetime.now().strftime("%Y-%m-%d")
        os.makedirs("_posts", exist_ok=True)
        filename = f"_posts/{date_str}-{blog['name'].replace(' ', '-').lower()}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"---\nlayout: post\ntitle: \"{blog['name']}: {entry.title}\"\npublished: true\n---\n\n" + content)
        
        # Klíčová pauza pro dodržení limitu kvóty (1 minuta)
        print("Čekám 60 sekund před dalším dotazem...")
        time.sleep(60)

print("Hotovo! Všechny zdroje zpracovány.")
