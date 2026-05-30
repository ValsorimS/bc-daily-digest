import json
import feedparser
import google.generativeai as genai
import os
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def summarize(text):
    prompt = f"Shrň technické novinky z Business Central pro vývojáře do 5 odrážek v češtině. Text: {text[:10000]}"
    return model.generate_content(prompt).text

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
