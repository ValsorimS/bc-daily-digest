import json
import feedparser
import google.generativeai as genai
import os
import time
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash')

def summarize(text):
    # Pokusíme se o sumarizaci 3x, pokud to selže
    for attempt in range(3):
        try:
            return model.generate_content(text[:5000]).text
        except Exception as e:
            if "429" in str(e):
                time.sleep(25)  # Počkej 25 sekund, pokud je limit vyčerpán
            else:
                raise e
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
os.makedirs("_posts", exist_ok=True)
with open(f"_posts/{date_str}-bc-novinky.md", "w", encoding="utf-8") as f:
    f.write(f"---\nlayout: post\ntitle: \"BC novinky {date_str}\"\n---\n\n" + content)
