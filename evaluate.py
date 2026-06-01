"""Evaluace kvality digestu.

Dvě části:
  1) Lint formátu (deterministicky, bez API) přes všechny příspěvky v _posts/:
     verdikt, oddělovač <!--více-->, odrážky shrnutí, odkaz, žádné zbylé
     číslování verdiktu.
  2) LLM-judge kvality (Gemini) na vzorku nedávných příspěvků: vhodnost
     verdiktu a věrnost shrnutí vůči zdrojovému článku (znovu staženému
     z feedu). Vyžaduje GEMINI_API_KEY; bez něj se přeskočí.

Markdown report jde na stdout, průběh/chyby na stderr. Návratový kód je
vždy 0 (report-only).
"""

import os
import re
import sys
import json
import glob
import time
from datetime import datetime, timedelta

import feedparser

# Výstup vždy v UTF-8 (kvůli emoji/diakritice i na Windows konzoli)
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

FEED_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
EVAL_RECENT_DAYS = 45      # LLM-judge jen pro články novější než tento limit
MAX_JUDGE = 5              # strop počtu LLM volání (kvóta)
JUDGE_PAUSE_S = 4          # pauza mezi LLM voláními
MODELS = [
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-flash-lite-latest",
]


def log(*args):
    print(*args, file=sys.stderr)


# --- Načtení příspěvků -----------------------------------------------------

def parse_post(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        return None
    fm_raw, body = m.group(1), m.group(2).strip()
    fm = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return {"path": path, "name": os.path.basename(path), "fm": fm, "body": body}


def article_link(body):
    m = re.search(r"\[Číst celý článek\]\((.*?)\)", body)
    return m.group(1) if m else None


def original_date(fm):
    d = fm.get("original_date")
    if not d:
        return None
    try:
        return datetime.strptime(d, "%Y-%m-%d")
    except ValueError:
        return None


# --- 1) Lint formátu -------------------------------------------------------

def lint(post):
    body = post["body"]
    issues = []
    first = next((l for l in body.splitlines() if l.strip()), "")

    if "Verdikt" not in first:
        issues.append("verdikt není na začátku")
    if not re.search(r"\b(ANO|NE)\b", first.upper()):
        issues.append("verdikt bez ANO/NE")
    if re.match(r"^\s*\d+[.)]", first):
        issues.append("verdikt začíná číslováním (1./2.)")
    if "<!--více-->" not in body:
        issues.append("chybí oddělovač <!--více-->")
    if len(re.findall(r"(?m)^\s*[*-]\s+", body)) == 0:
        issues.append("žádné odrážky shrnutí")
    if "[Číst celý článek](" not in body:
        issues.append("chybí odkaz na článek")
    return issues


# --- 2) LLM-judge kvality --------------------------------------------------

def build_source_map():
    """link -> text článku z feedů (pro porovnání věrnosti)."""
    src = {}
    try:
        with open("sources.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return src
    for blog in data.get("blogs", []):
        try:
            feed = feedparser.parse(blog["url"], agent=FEED_USER_AGENT)
        except Exception as e:  # noqa: BLE001
            log(f"  feed selhal: {blog.get('url')}: {e}")
            continue
        for e in feed.entries:
            link = e.get("link")
            if link:
                src[link] = (e.get("summary", "") or "")[:4000]
    return src


def extract_json(text):
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def judge(client, source_text, summary_text):
    prompt = (
        "Jsi přísný hodnotitel kvality. Níže je ZDROJ (úryvek článku) a jeho "
        "SHRNUTÍ vytvořené AI pro zkušeného Business Central / AL vývojáře.\n"
        "Vyhodnoť a vrať POUZE JSON bez dalšího textu:\n"
        '{"verdict_ok": true/false, "faithfulness": 1-5, "note": "krátce česky"}\n'
        "- verdict_ok: je verdikt ANO/NE přiměřený? (ANO = relevantní pro AL, "
        "AI agenty, technické novinky/trendy v BC)\n"
        "- faithfulness: 5 = shrnutí přesně odpovídá zdroji bez vymyšlených "
        "faktů, 1 = silně zavádějící/halucinace.\n\n"
        f"ZDROJ:\n{source_text}\n\nSHRNUTÍ:\n{summary_text}"
    )
    from google.genai.errors import ClientError, ServerError
    for model in MODELS:
        try:
            resp = client.models.generate_content(model=model, contents=prompt)
            data = extract_json(resp.text)
            if data is not None:
                return data
            log(f"  judge: nečitelný JSON z {model}")
            return None
        except ServerError:
            continue
        except ClientError as e:
            if getattr(e, "code", None) == 429:
                raise
            continue
    return None


# --- Report ----------------------------------------------------------------

def main():
    posts = [p for p in (parse_post(p) for p in sorted(glob.glob("_posts/*.md"))) if p]
    log(f"Načteno příspěvků: {len(posts)}")

    # 1) Lint
    lint_results = [(p, lint(p)) for p in posts]
    bad = [(p, iss) for p, iss in lint_results if iss]

    out = []
    out.append(f"# Evaluace digestu – {datetime.now():%d. %m. %Y %H:%M}")
    out.append("")
    out.append(f"## Formát ({len(posts)} příspěvků)")
    out.append("")
    out.append(f"- ✅ Bez problémů: **{len(posts) - len(bad)}**")
    out.append(f"- ⚠️ S problémy: **{len(bad)}**")
    out.append("")
    if bad:
        out.append("| Příspěvek | Problémy |")
        out.append("|---|---|")
        for p, iss in bad:
            out.append(f"| {p['name']} | {'; '.join(iss)} |")
        out.append("")

    # 2) LLM-judge
    out.append("## Kvalita (LLM-judge)")
    out.append("")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        out.append("_Přeskočeno: není GEMINI_API_KEY._")
        print("\n".join(out))
        return

    cutoff = datetime.now() - timedelta(days=EVAL_RECENT_DAYS)
    recent = [p for p in posts
              if (od := original_date(p["fm"])) and od >= cutoff]
    recent.sort(key=lambda p: original_date(p["fm"]), reverse=True)
    log(f"Nedávných příspěvků ke kontrole kvality: {len(recent)}")

    log("Stahuji zdroje z feedů…")
    src_map = build_source_map()

    from google import genai
    client = genai.Client(api_key=api_key)

    rows = []
    faith_scores = []
    verdict_ok_count = 0
    judged = 0
    for p in recent:
        if judged >= MAX_JUDGE:
            break
        link = article_link(p["body"])
        source = src_map.get(link) if link else None
        if not source:
            log(f"  zdroj nedostupný, přeskočeno: {p['name']}")
            continue
        log(f"  hodnotím: {p['name']}")
        try:
            res = judge(client, source, p["body"])
        except Exception as e:  # noqa: BLE001
            log(f"  judge selhal ({e}); končím LLM část.")
            break
        if not res:
            continue
        judged += 1
        vok = bool(res.get("verdict_ok"))
        fth = res.get("faithfulness")
        if vok:
            verdict_ok_count += 1
        if isinstance(fth, (int, float)):
            faith_scores.append(fth)
        rows.append((p["name"], "✅" if vok else "❌",
                     fth if fth is not None else "?",
                     str(res.get("note", "")).replace("|", "/")))
        time.sleep(JUDGE_PAUSE_S)

    if judged == 0:
        out.append("_Nebyl k dispozici žádný nedávný článek se stažitelným zdrojem._")
    else:
        avg = sum(faith_scores) / len(faith_scores) if faith_scores else 0
        out.append(f"Vzorek: **{judged}** nedávných článků.")
        out.append("")
        out.append(f"- Verdikt vhodný: **{verdict_ok_count}/{judged}**")
        out.append(f"- Průměrná věrnost shrnutí: **{avg:.1f}/5**")
        out.append("")
        out.append("| Příspěvek | Verdikt OK | Věrnost | Poznámka |")
        out.append("|---|:--:|:--:|---|")
        for name, vok, fth, note in rows:
            out.append(f"| {name} | {vok} | {fth} | {note} |")

    print("\n".join(out))


if __name__ == "__main__":
    main()
