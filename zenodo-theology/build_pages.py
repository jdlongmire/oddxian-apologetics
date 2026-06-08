#!/usr/bin/env python3
"""Build the GitHub Pages public view for the zenodo-theology published set.

Reads every zenodo-theology/<slug>/ that has BOTH metadata.json and a
RECORD.md carrying a DOI (i.e. it has been published to Zenodo), and emits a
static site into <repo>/docs/:

    docs/index.html            journal landing page (article list)
    docs/<slug>/index.html     per-article page (abstract, cite, DOI, PDF)
    docs/<slug>/article.pdf    copy of the deposited PDF
    docs/.nojekyll             bypass Jekyll; serve the HTML as-is

Single-source: metadata.json is the source for titles/abstracts/keywords;
RECORD.md is the source for the minted DOI and dates. Re-run after publishing
a new article. Stdlib only.

GitHub Pages: Settings -> Pages -> Source: Deploy from a branch -> main /docs.
Live at https://jdlongmire.github.io/oddxian-apologetics/
"""

import html
import json
import re
import shutil
from pathlib import Path

# --- Edit these to rename / rebrand the public journal -----------------------
TITLE = "oddXian · Theology"
TAGLINE = "Open-access theological articles, archived with DOIs on Zenodo."
INTRO = (
    "Grammatical-historical theology published openly and archived for "
    "citation on Zenodo. Each article below carries a permanent DOI. This "
    "collection is distinct from the Scientific Designism research program."
)
# -----------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent          # zenodo-theology/
REPO = ROOT.parent                              # repo root
DOCS = REPO / "docs"

CSS = """
:root{--ink:#1a1a1a;--muted:#5b6470;--line:#e3e6ea;--accent:#5b3a8c;--bg:#fbfbfc}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,serif;
  font-family:Georgia,"Times New Roman",serif}
.wrap{max-width:760px;margin:0 auto;padding:48px 22px 80px}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
header.site{border-bottom:2px solid var(--ink);padding-bottom:18px;margin-bottom:34px}
header.site h1{font-size:30px;margin:0 0 6px;letter-spacing:.2px}
header.site .tagline{color:var(--muted);font-style:italic;margin:0}
header.site .intro{color:var(--ink);font-size:15.5px;margin:16px 0 0}
.article{padding:22px 0;border-bottom:1px solid var(--line)}
.article h2{font-size:21px;margin:0 0 4px;line-height:1.3}
.meta{color:var(--muted);font-size:14px;margin:0 0 10px}
.abstract{margin:0 0 12px}
.badges a{display:inline-block;font-family:-apple-system,Segoe UI,Roboto,sans-serif;
  font-size:12.5px;border:1px solid var(--line);border-radius:5px;
  padding:3px 10px;margin:0 8px 0 0;color:var(--muted);background:#fff}
.badges a:hover{border-color:var(--accent);color:var(--accent);text-decoration:none}
.keywords{margin-top:10px;color:var(--muted);font-size:13px}
article.paper h1{font-size:25px;line-height:1.28;margin:0 0 8px}
article.paper .authors{font-size:16px;margin:0 0 2px}
article.paper .subhead{color:var(--muted);font-size:14px;margin:0 0 22px}
article.paper h3{font-size:14px;text-transform:uppercase;letter-spacing:.6px;
  color:var(--muted);margin:30px 0 8px}
.cite{background:#fff;border:1px solid var(--line);border-radius:6px;
  padding:14px 16px;font-size:14.5px;line-height:1.5}
.actions a{display:inline-block;background:var(--accent);color:#fff;
  font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:14px;
  padding:9px 16px;border-radius:6px;margin:0 10px 10px 0}
.actions a.alt{background:#fff;color:var(--accent);border:1px solid var(--accent)}
.actions a:hover{text-decoration:none;opacity:.9}
footer.site{margin-top:46px;padding-top:18px;border-top:1px solid var(--line);
  color:var(--muted);font-size:13px;font-family:-apple-system,Segoe UI,Roboto,sans-serif}
.back{font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:13.5px}
"""

RECORD_FIELDS = {
    "doi": r"DOI \(this version\):\*\*\s*(.+)",
    "concept_doi": r"Concept DOI \(all versions\):\*\*\s*(.+)",
    "record_url": r"Record URL:\*\*\s*(.+)",
    "doi_url": r"DOI URL:\*\*\s*(.+)",
    "published": r"Published:\*\*\s*(.+)",
    "version": r"Version:\*\*\s*(.+)",
}


def parse_record(text):
    out = {}
    for key, pat in RECORD_FIELDS.items():
        m = re.search(pat, text)
        out[key] = m.group(1).strip() if m else ""
    return out


def e(s):
    return html.escape(s or "", quote=True)


def author_str(creators):
    return "; ".join(c.get("name", "") for c in creators)


def author_display(creators):
    # "Longmire, James (JD)" -> "James (JD) Longmire"
    names = []
    for c in creators:
        n = c.get("name", "")
        if ", " in n:
            fam, giv = n.split(", ", 1)
            names.append(f"{giv} {fam}")
        else:
            names.append(n)
    return ", ".join(names)


def year_of(published):
    m = re.match(r"(\d{4})", published or "")
    return m.group(1) if m else ""


def citation(meta, rec):
    yr = year_of(rec.get("published"))
    return (f'{author_str(meta["creators"])}. ({yr}). <em>{e(meta["title"])}</em>. '
            f'Zenodo. {e(rec.get("doi_url"))}')


def page_shell(title, body, css_href="style.css"):
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{css_href}">
</head><body><div class="wrap">
{body}
</div></body></html>
"""


def collect():
    articles = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith("_")):
        meta_f, rec_f, pdf_f = d / "metadata.json", d / "RECORD.md", d / "article.pdf"
        if not (meta_f.exists() and rec_f.exists()):
            continue
        meta = json.loads(meta_f.read_text(encoding="utf-8")).get("metadata", {})
        rec = parse_record(rec_f.read_text(encoding="utf-8"))
        if not rec.get("doi"):
            continue
        articles.append({"slug": d.name, "meta": meta, "rec": rec,
                         "pdf": pdf_f if pdf_f.exists() else None})
    # newest first by published date
    articles.sort(key=lambda a: a["rec"].get("published", ""), reverse=True)
    return articles


def render_index(articles):
    cards = []
    for a in articles:
        m, r = a["meta"], a["rec"]
        abstract = m.get("description", "")
        snippet = abstract[:300].rsplit(" ", 1)[0] + "…" if len(abstract) > 300 else abstract
        kw = ", ".join(m.get("keywords", [])[:8])
        badges = [f'<a href="{a["slug"]}/">Read</a>']
        if r.get("doi_url"):
            badges.append(f'<a href="{e(r["doi_url"])}">DOI: {e(r["doi"])}</a>')
        if a["pdf"]:
            badges.append(f'<a href="{a["slug"]}/article.pdf">PDF</a>')
        cards.append(f"""<div class="article">
  <h2><a href="{a['slug']}/">{e(m['title'])}</a></h2>
  <p class="meta">{e(author_display(m['creators']))} &middot; {e(r.get('published'))}</p>
  <p class="abstract">{e(snippet)}</p>
  <p class="badges">{''.join(badges)}</p>
  <p class="keywords">{e(kw)}</p>
</div>""")
    body = f"""<header class="site">
  <h1>{e(TITLE)}</h1>
  <p class="tagline">{e(TAGLINE)}</p>
  <p class="intro">{e(INTRO)}</p>
</header>
{''.join(cards) if cards else '<p>No published articles yet.</p>'}
<footer class="site">{len(articles)} article(s) &middot; archived on
<a href="https://zenodo.org/">Zenodo</a> &middot;
source: <a href="https://github.com/jdlongmire/oddxian-apologetics">oddxian-apologetics</a></footer>"""
    return page_shell(e(TITLE), body)


def render_article(a):
    m, r = a["meta"], a["rec"]
    kw = ", ".join(m.get("keywords", []))
    actions = []
    if a["pdf"]:
        actions.append('<a href="article.pdf">Read the PDF</a>')
    if r.get("record_url"):
        actions.append(f'<a class="alt" href="{e(r["record_url"])}">View on Zenodo</a>')
    body = f"""<p class="back"><a href="../">&larr; {e(TITLE)}</a></p>
<article class="paper">
  <h1>{e(m['title'])}</h1>
  <p class="authors">{e(author_display(m['creators']))}</p>
  <p class="subhead">ORCID {e(m['creators'][0].get('orcid','')) }
    &middot; {e(r.get('published'))}
    &middot; {e((m.get('license') or '').upper())}
    &middot; Open access</p>

  <div class="actions">{''.join(actions)}</div>

  <h3>Abstract</h3>
  <p>{e(m.get('description'))}</p>

  <h3>Cite</h3>
  <p class="cite">{citation(m, r)}</p>

  <h3>Identifiers</h3>
  <p class="meta">DOI (this version): <a href="{e(r.get('doi_url'))}">{e(r.get('doi'))}</a><br>
  Concept DOI (all versions): {e(r.get('concept_doi'))}<br>
  Version {e(r.get('version'))}</p>

  <h3>Keywords</h3>
  <p class="keywords">{e(kw)}</p>
</article>
<footer class="site"><a href="../">&larr; Back to {e(TITLE)}</a></footer>"""
    return page_shell(e(m["title"]), body, css_href="../style.css")


def main():
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "style.css").write_text(CSS, encoding="utf-8")

    articles = collect()
    (DOCS / "index.html").write_text(render_index(articles), encoding="utf-8")
    for a in articles:
        adir = DOCS / a["slug"]
        adir.mkdir(parents=True, exist_ok=True)
        (adir / "index.html").write_text(render_article(a), encoding="utf-8")
        if a["pdf"]:
            shutil.copy2(a["pdf"], adir / "article.pdf")

    print(f"Built docs/ with {len(articles)} article(s):")
    for a in articles:
        print(f"  - {a['slug']}  ({a['rec'].get('doi')})")


if __name__ == "__main__":
    main()
