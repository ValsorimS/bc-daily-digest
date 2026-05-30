import json
import feedparser
import google.generativeai as genai
import os
import time
import google.api_core.exceptions
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-3.5-flash')

def summarize(text):
    for attempt in range(3): # Zkusí to 3x
        try:
            # Pošleme jen kousek textu, abychom šetřili tokeny
            return model.generate_content(text[:4000]).text
        except google.api_core.exceptions.ResourceExhausted:
            print(f"Kvóta vyčerpána, čekám 60 sekund... (pokus {attempt+1})")
            time.sleep(60) # Čekání 1 minuta mezi pokusy
        except Exception as e:
            print(f"Chyba: {e}")
            break
    return "Nepodařilo se shrnout (kvóta vyčerpána)."

# Hlavní logika
with open('sources.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

content = "# Denní přehled BC novinek\n\n"

for blog in data.get('blogs', []):
    feed = feedparser.parse(blog['url'])
    if feed.entries:
        entry = feed.entries[0]
        content += f"## {entry.title}\n{summarize(entry.summary)}\n\n[Číst celý článek]({entry.link})\n\n"

# Uložení do _posts
date_str = datetime.now().strftime("%Y-%m-%d")
filename = f"_posts/{date_str}-bc-novinky.md"
os.makedirs("_posts", exist_ok=True)

# Upravená hlavička (přidali jsme 'published: true')
header = f"---\nlayout: post\ntitle: \"BC novinky {date_str}\"\npublished: true\n---\n\n"

with open(filename, "w", encoding="utf-8") as f:
    f.write(header + content)
