"""Pomocník pro přidávání zdrojů do sources.json.

Použití:
    python add_source.py https://nejakyblog.cz
    python add_source.py https://nejakyblog.cz/feed/ --name "Hezký blog"
    python add_source.py https://www.youtube.com/@nejakykanal      # YouTube se pozná sám
    python add_source.py https://www.youtube.com/@kanal --youtube  # vynucení YouTube

Co dělá:
    - U blogu sám najde RSS/Atom feed (z <link rel="alternate"> na stránce),
      ověří, že jde parsovat, a vytáhne název z titulku feedu.
    - U YouTube z URL kanálu zjistí channel_id a sestaví RSS feed kanálu.
    - Odstraní duplicity a zapíše do sources.json.
"""

import argparse
import json
import re
import sys
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser

import requests
import feedparser

SOURCES_FILE = "sources.json"
YOUTUBE_RSS = "https://www.youtube.com/feeds/videos.xml?channel_id={}"
USER_AGENT = (
    "Mozilla/5.0 (compatible; bc-daily-digest/1.0; "
    "+https://github.com/ValsorimS/bc-daily-digest)"
)


def fetch_html(url):
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=20)
        resp.raise_for_status()
        return resp.text
    except requests.HTTPError as e:
        code = e.response.status_code if e.response is not None else "?"
        sys.exit(f"Stránku {url} se nepodařilo načíst (HTTP {code}). "
                 f"Web možná blokuje scraping – zkus zadat přímou URL feedu "
                 f"(např. .../feed/) a název přes --name.")
    except requests.RequestException as e:
        sys.exit(f"Stránku {url} se nepodařilo načíst: {e}")


def load_sources():
    try:
        with open(SOURCES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_sources(data):
    with open(SOURCES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def normalize_url(url):
    """Pro porovnávání duplicit – sjednotí schéma/host a ořízne koncové lomítko."""
    p = urlparse(url.strip())
    return f"{p.scheme.lower()}://{p.netloc.lower()}{p.path.rstrip('/')}"


# --- Blogy -----------------------------------------------------------------

class _FeedLinkParser(HTMLParser):
    """Vytáhne z HTML odkazy na RSS/Atom feedy (<link rel="alternate">)."""

    def __init__(self):
        super().__init__()
        self.feeds = []  # seznam (href, type)

    def handle_starttag(self, tag, attrs):
        if tag != "link":
            return
        a = {k.lower(): (v or "") for k, v in attrs}
        rel = a.get("rel", "").lower()
        typ = a.get("type", "").lower()
        if "alternate" in rel and typ in ("application/rss+xml", "application/atom+xml"):
            if a.get("href"):
                self.feeds.append((a["href"], typ))


def discover_feed(url):
    """Vrátí URL feedu – buď přímo zadanou (když už je to feed), nebo objevenou."""
    # 1) Je zadaná URL rovnou feed?
    parsed = feedparser.parse(url)
    if parsed.entries:
        return url

    # 2) Jinak stáhneme HTML a hledáme <link rel="alternate">
    html = fetch_html(url)
    parser = _FeedLinkParser()
    parser.feed(html)
    if not parser.feeds:
        sys.exit(f"Na {url} se nepodařilo najít RSS/Atom feed. "
                 f"Zadej prosím přímou URL feedu.")

    # Preferuj RSS před Atomem, jinak vezmi první
    rss = [href for href, typ in parser.feeds if typ == "application/rss+xml"]
    href = rss[0] if rss else parser.feeds[0][0]
    return urljoin(url, href)


def add_blog(url, name=None):
    feed_url = discover_feed(url)
    parsed = feedparser.parse(feed_url)
    if not parsed.entries:
        sys.exit(f"Feed {feed_url} nejde parsovat nebo je prázdný.")

    if not name:
        name = (parsed.feed.get("title") or "").strip() or urlparse(feed_url).netloc

    data = load_sources()
    blogs = data.setdefault("blogs", [])
    if any(normalize_url(b.get("url", "")) == normalize_url(feed_url) for b in blogs):
        print(f"Už existuje v blogs: {feed_url}")
        return

    blogs.append({"name": name, "url": feed_url})
    save_sources(data)
    print(f"Přidáno do blogs: {name} — {feed_url}")


# --- YouTube ---------------------------------------------------------------

def resolve_channel_id(url):
    """Zjistí channel_id (UC…) z URL kanálu nebo videa."""
    # Přímo v URL (…/channel/UCxxxx)
    m = re.search(r"/channel/(UC[\w-]{20,})", url)
    if m:
        return m.group(1)

    # Jinak ze zdroje stránky (handle/@…, /c/…, /user/…, video)
    html = fetch_html(url)
    m = (re.search(r'"channelId":"(UC[\w-]{20,})"', html)
         or re.search(r'/channel/(UC[\w-]{20,})', html))
    if m:
        return m.group(1)
    sys.exit(f"Nepodařilo se zjistit channel_id z {url}.")


def add_youtube(url, name=None):
    channel_id = resolve_channel_id(url)
    parsed = feedparser.parse(YOUTUBE_RSS.format(channel_id))
    if not name:
        name = (parsed.feed.get("title") or "").strip() or channel_id

    data = load_sources()
    channels = data.setdefault("youtube", [])
    if any(c.get("channel_id") == channel_id for c in channels):
        print(f"Už existuje v youtube: {channel_id}")
        return

    channels.append({"name": name, "channel_id": channel_id})
    save_sources(data)
    print(f"Přidáno do youtube: {name} — {channel_id}")


# --- CLI -------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Přidá zdroj (blog nebo YouTube kanál) do sources.json."
    )
    parser.add_argument("url", help="URL blogu/feedu nebo YouTube kanálu")
    parser.add_argument("--name", help="Vlastní název (jinak se vezme z titulku feedu)")
    parser.add_argument("--youtube", action="store_true",
                        help="Vynutit YouTube (jinak se pozná podle domény)")
    args = parser.parse_args()

    host = urlparse(args.url).netloc.lower()
    is_youtube = args.youtube or "youtube.com" in host or "youtu.be" in host

    if is_youtube:
        add_youtube(args.url, args.name)
    else:
        add_blog(args.url, args.name)


if __name__ == "__main__":
    main()
