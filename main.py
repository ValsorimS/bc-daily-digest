import json
import feedparser
import google.generativeai as genai
import os
import time
from datetime import datetime

# Konfigurace
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-flash-latest')
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
        "Jsi expert na MS Dynamics 365 Business Central a AL programování. "
        "Shrň technické novinky pro zkušeného BC vývojáře. Zaměř se na AL, AI agenty a trendy. "
        "Buď maximálně technický, stručný a piš v češtině. "
        "Výstup dej do 3 krátkých odrážek.\n\n"
        f"Text k analýze: {text[:3000]}"
    )
    return model.generate_content(prompt).text

# 1. Načtení historie a zdrojů
processed = get_processed_links()
with open('sources.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Zpracování (omezeno na 5 článků za běh pro úsporu kvóty)
count = 0
MAX_PER_RUN = 5 

for blog in data.get('blogs', []):
    feed = feedparser.parse(blog['url'])
    
    # Projdeme feed od nejstarších článků (backfilling)
    for entry in reversed(feed.entries):
        if count >= MAX_PER_RUN:
            break
            
        if entry.link not in processed:
            print(f"Zpracovávám: {entry.title}")
            summary = summarize(entry.summary)
            
            # Uložení příspěvku
            date_str = datetime.now().strftime("%Y-%m-%d")
            filename = f"_posts/{date_str}-{blog['name'].replace(' ', '-').lower()}-{count}.md"
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"---\nlayout: post\ntitle: \"{blog['name']}: {entry.title}\"\npublished: true\n---\n\n{summary}\n\n[Číst celý článek]({entry.link})")
            
            # Zápis do historie
            processed[entry.link] = datetime.now().isoformat()
            save_processed_links(processed)
            
            count += 1
            time.sleep(60) # Pauza mezi články pro klid Google API

print("Hotovo. Zpracováno nových článků:", count)
