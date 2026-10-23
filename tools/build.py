# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown-it-py>=3,<4", "mdit-py-plugins>=0.4,<1"]
# ///
"""Rakentaa työpajan sivuston kansion sisalto/ Markdown-tiedostoista.

Ajo repon juuresta:  uv run tools/build.py
Tuottaa: index.html, claude/, codex/, ohjaaja/ (ohjaaja ei ole linkitetty etusivulta).
"""
from __future__ import annotations

import html
import re
import shutil
import sys
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.tasklists import tasklists_plugin

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "sisalto"
VERSION = "Versio 1 · 23.10.2026"

PATHS = {
    "claude": {
        "name": "Claude-polku",
        "tool": "Claude-työpöytäsovelluksen Code-välilehti",
        "file_word": "ohjetiedosto CLAUDE.md",
    },
    "codex": {
        "name": "Codex-polku",
        "tool": "Codex-työpöytäsovellus Windowsille",
        "file_word": "ohjetiedosto AGENTS.md",
    },
}

md = MarkdownIt("commonmark", {"html": False}).enable("table").use(tasklists_plugin, enabled=True)


# ---------- Markdown → HTML ----------

def strip_h1(text: str) -> tuple[str, str]:
    """Palauttaa (h1-otsikko, loput tekstistä)."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return line[2:].strip(), "\n".join(lines[i + 1:])
        if line.strip():
            break
    return "", text


def pull_question(text: str) -> tuple[str, str]:
    """Irrottaa '> Ajattelukysymys: …' -rivin tekstistä."""
    m = re.search(r"^> Ajattelukysymys:\s*(.+)$", text, flags=re.M)
    if not m:
        return "", text
    return m.group(1).strip(), text[: m.start()] + text[m.end():]


def site_text(text: str) -> str:
    """Sivustolla tiedostonimet korvataan osion osilla."""
    text = text.replace("osion lukuteksti (self-study.md)", "osion lukuteksti")
    text = text.replace(" (self-study.md)", "")
    text = text.replace("(`teacher-led-tasks.md`)", "(ohjatut tehtävät tällä sivulla)")
    text = text.replace("`teacher-led-tasks.md`", "ohjatut tehtävät")
    return text


_counter = {"n": 0}


def render(text: str, shift: int = 1) -> str:
    out = md.render(site_text(text))
    # Otsikkotasot alaspäin, koska sivun h1 ja osioiden h2 tulevat rungosta.
    def bump(m: re.Match) -> str:
        level = min(int(m.group(2)) + shift, 6)
        return f"<{m.group(1)}h{level}"
    out = re.sub(r"<(/?)h([1-6])", bump, out)

    # Kopioitavat lohkot
    def prompt(m: re.Match) -> str:
        _counter["n"] += 1
        pid = f"k{_counter['n']}"
        code = m.group(2)
        return (
            f'<div class="prompt"><div class="prompt-head"><span class="kicker dim">Kopioi koko lohko</span>'
            f'<button class="copy-btn" type="button" data-copy="#{pid}">Kopioi</button></div>'
            f'<pre id="{pid}"><code>{code}</code></pre></div>'
        )
    out = re.sub(r'<pre><code( class="language-[^"]*")?>(.*?)</code></pre>', prompt, out, flags=re.S)
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return out


# ---------- Sivupohja ----------

FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' rx='7' fill='%23775EC4'/%3E%3Ctext x='16' y='22' "
    "text-anchor='middle' font-family='Georgia,serif' font-size='18' font-weight='600' "
    "fill='white'%3EV%3C/text%3E%3C/svg%3E"
)


def page(title: str, body: str, depth: int, description: str = "") -> str:
    up = "../" * depth
    desc = html.escape(description or "Vibekoodaus-työpaja: ohjelmointia osaamaton rakentaa agentin avulla Oppisopimustäyttäjän.")
    return f"""<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{up}assets/style.css">
<script src="{up}assets/site.js" defer></script>
</head>
<body>
<main>
{body}
<footer class="page">Kaikki materiaalin henkilöt, yritykset, tunnisteet ja palkat ovat kuvitteellisia. {VERSION}.</footer>
</main>
</body>
</html>
"""


# ---------- Sisällön luku ----------

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def readme_sections() -> tuple[str, dict[str, str]]:
    text = read(SRC / "README.md")
    _, text = strip_h1(text)
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    intro = parts[0]
    secs = {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}
    return intro, secs


def schedule() -> list[dict]:
    """Osioiden nimet ja ajat READMEn taulukosta."""
    _, secs = readme_sections()
    rows = []
    for line in secs["Rakenne"].splitlines():
        m = re.match(r"^\| (\d\d) \| (.+?) \| (.+?) \|$", line)
        if m:
            rows.append({"nro": m.group(1), "nimi": m.group(2), "aika": m.group(3)})
    if len(rows) != 10:
        sys.exit(f"Aikataulutaulukosta löytyi {len(rows)} osiota, odotettiin 10.")
    return rows


# ---------- Sivut ----------

def lesson_kicker(row: dict) -> str:
    return f"Osio {row['nro']} · {row['aika']}"


def build_student(key: str, rows: list[dict]) -> None:
    info = PATHS[key]
    out_dir = ROOT / key
    out_dir.mkdir(exist_ok=True)

    cards = []
    for row in rows:
        src = SRC / "student" / key / f"lesson-{row['nro']}"
        _, ss = strip_h1(read(src / "self-study.md"))
        question, _ = pull_question(ss)
        cards.append(
            f'<a class="exercise-card" href="osio-{row["nro"]}.html"><div class="row">'
            f'<div class="kicker">{html.escape(lesson_kicker(row))}</div><span class="arrow">→</span></div>'
            f'<div class="title">{html.escape(row["nimi"])}</div>'
            f'<p>{html.escape(question)}</p></a>'
        )
    body = f"""<a class="back-link" href="../index.html">← Työpajan etusivu</a>
<header class="page">
  <div class="kicker">{info['name']}</div>
  <h1>{info['name']}</h1>
  <p class="lead">Työkalu: {info['tool']}. Lue vain tämän polun sivuja. Aloita osiosta 00 itsenäisesti viimeistään kolme arkipäivää ennen työpajaa.</p>
  <p class="note">Jokaisessa osiossa on lukuteksti, tehtävät ja sanasto. Kehotteet kopioit Kopioi-painikkeella.</p>
</header>
<nav class="exercises">
{chr(10).join(cards)}
</nav>"""
    (out_dir / "index.html").write_text(page(f"{info['name']} – Vibekoodaus-työpaja", body, 1), encoding="utf-8")

    for i, row in enumerate(rows):
        src = SRC / "student" / key / f"lesson-{row['nro']}"
        _, ss = strip_h1(read(src / "self-study.md"))
        question, ss = pull_question(ss)
        _, tasks = strip_h1(read(src / "student-tasks.md"))
        _, vocab = strip_h1(read(src / "vocabulary.md"))
        prev_link = (
            f'<a href="osio-{rows[i-1]["nro"]}.html">← Osio {rows[i-1]["nro"]}</a>' if i > 0 else '<span></span>'
        )
        next_link = (
            f'<a href="osio-{rows[i+1]["nro"]}.html">Osio {rows[i+1]["nro"]} →</a>' if i < len(rows) - 1 else '<span></span>'
        )
        body = f"""<a class="back-link" href="index.html">← {info['name']}</a>
<header class="page">
  <div class="kicker">{info['name']} · {html.escape(lesson_kicker(row))}</div>
  <h1>{html.escape(row['nimi'])}</h1>
  <div class="insight"><div class="kicker">Ajattelukysymys</div><p>{html.escape(question)}</p></div>
</header>
<nav class="pills" aria-label="Osion sisältö">
  <a href="#lue">1 · Lukuteksti</a><a href="#tehtavat">2 · Tehtävät</a><a href="#sanasto">3 · Sanasto</a>
</nav>
<section class="md" id="lue"><h2>Lukuteksti</h2>
{render(ss)}
</section>
<section class="md" id="tehtavat"><h2>Tehtävät</h2>
{render(tasks)}
</section>
<section class="md" id="sanasto"><h2>Sanasto</h2>
{render(vocab)}
</section>
<nav class="pager">{prev_link}{next_link}</nav>"""
        (out_dir / f"osio-{row['nro']}.html").write_text(
            page(f"Osio {row['nro']}: {row['nimi']} – {info['name']}", body, 1, question), encoding="utf-8"
        )


def build_teacher(rows: list[dict]) -> None:
    out_dir = ROOT / "ohjaaja"
    out_dir.mkdir(exist_ok=True)
    cards = []
    for i, row in enumerate(rows):
        src = SRC / "teacher" / f"lesson-{row['nro']}"
        _, tm = strip_h1(read(src / "teacher-materials.md"))
        sections = [f'<section class="md" id="materiaali"><h2>Vetäjän materiaali</h2>\n{render(tm)}\n</section>']
        pills = ['<a href="#materiaali">Vetäjän materiaali</a>']
        tl = src / "teacher-led-tasks.md"
        if tl.exists():
            _, tlt = strip_h1(read(tl))
            sections.append(f'<section class="md" id="ohjatut"><h2>Ohjatut tehtävät</h2>\n{render(tlt)}\n</section>')
            pills.append('<a href="#ohjatut">Ohjatut tehtävät</a>')
        pills.append(f'<a href="../claude/osio-{row["nro"]}.html">Oppija: Claude</a>')
        pills.append(f'<a href="../codex/osio-{row["nro"]}.html">Oppija: Codex</a>')
        prev_link = (
            f'<a href="osio-{rows[i-1]["nro"]}.html">← Osio {rows[i-1]["nro"]}</a>' if i > 0 else '<span></span>'
        )
        next_link = (
            f'<a href="osio-{rows[i+1]["nro"]}.html">Osio {rows[i+1]["nro"]} →</a>' if i < len(rows) - 1 else '<span></span>'
        )
        body = f"""<a class="back-link" href="index.html">← Vetäjän sivut</a>
<header class="page">
  <div class="kicker">Vetäjä · {html.escape(lesson_kicker(row))}</div>
  <h1>{html.escape(row['nimi'])}</h1>
</header>
<nav class="pills" aria-label="Osion sisältö">{''.join(pills)}</nav>
{chr(10).join(sections)}
<nav class="pager">{prev_link}{next_link}</nav>"""
        (out_dir / f"osio-{row['nro']}.html").write_text(
            page(f"Vetäjä · Osio {row['nro']}: {row['nimi']}", body, 1), encoding="utf-8"
        )
        cards.append(
            f'<a class="exercise-card" href="osio-{row["nro"]}.html"><div class="row">'
            f'<div class="kicker">{html.escape(lesson_kicker(row))}</div><span class="arrow">→</span></div>'
            f'<div class="title">{html.escape(row["nimi"])}</div></a>'
        )

    _, names = strip_h1(read(SRC / "teacher" / "TARKISTETTAVAT-NIMET.md"))
    body = f"""<a class="back-link" href="index.html">← Vetäjän sivut</a>
<header class="page">
  <div class="kicker">Vetäjä · Harjoitusajo</div>
  <h1>Tarkistettavat nimet</h1>
</header>
<section class="md">
{render(names)}
</section>"""
    (out_dir / "tarkistettavat-nimet.html").write_text(page("Tarkistettavat nimet – Vetäjä", body, 1), encoding="utf-8")

    body = f"""<a class="back-link" href="../index.html">← Työpajan etusivu</a>
<header class="page">
  <div class="kicker">Vetäjä · Ei linkitetty etusivulta</div>
  <h1>Vetäjän sivut</h1>
  <p class="lead">Aikataulut, ohjaus askel askeleelta, jumikohdat, varasuunnitelmat ja polkujen erot. Yksi sivu kattaa molemmat polut.</p>
</header>
<section class="card">
  <div class="kicker dim">Ennen työpajaa</div>
  <ul class="arrows">
    <li>Ennakon aikajana, IT-pyyntö, testi-Wilma-pyyntö ja savutesti ovat osiossa 00.</li>
    <li>Käy harjoitusajossa läpi <a href="tarkistettavat-nimet.html">tarkistettavat nimet</a> omilla sovellusversioillasi.</li>
    <li>Oppijan sivut: <a href="../claude/index.html">Claude-polku</a> · <a href="../codex/index.html">Codex-polku</a>.</li>
  </ul>
</section>
<nav class="exercises">
{chr(10).join(cards)}
</nav>"""
    (out_dir / "index.html").write_text(page("Vetäjän sivut – Vibekoodaus-työpaja", body, 1), encoding="utf-8")


def build_index(rows: list[dict]) -> None:
    intro, secs = readme_sections()
    table = "\n".join(l for l in secs["Rakenne"].splitlines() if l.startswith("|"))
    path_cards = "\n".join(
        f'<a class="exercise-card" href="{key}/index.html"><div class="row">'
        f'<div class="kicker">{info["tool"]}</div><span class="arrow">→</span></div>'
        f'<div class="title">{info["name"]}</div><p>Sama tuote, samat vaiheet ja samat hyväksymiskriteerit. Projektiin tulee {info["file_word"]}.</p></a>'
        for key, info in PATHS.items()
    )
    body = f"""<header class="page">
  <div class="kicker">Vibekoodaus-työpaja · Kaksi päivää</div>
  <h1>Oppisopimustäyttäjä agentin avulla</h1>
  <div class="md lead-md">{render(intro)}</div>
</header>
<section class="card">
  <div class="kicker dim">Valitse polku</div>
  <p>Valitse polku, johon sinulla tai organisaatiollasi on tilaus. Lue sen jälkeen vain oman polkusi sivuja. Aloita osiosta 00 itsenäisesti ennen työpajaa.</p>
</section>
<nav class="exercises">
{path_cards}
</nav>
<section class="md"><h2>Kenelle</h2>{render(secs['Kenelle'])}</section>
<section class="md"><h2>Ennakkovaatimukset</h2>{render(secs['Ennakkovaatimukset'])}</section>
<section class="md"><h2>Aikataulu</h2>{render(table)}
<p class="note">Kopioit kehotteet sivulta Kopioi-painikkeella. Älä kopioi niitä Muistiosta, koska mukaan tulisi ylimääräisiä merkkejä.</p></section>
<section class="md"><h2>Turvaraja</h2>{render(secs['Turvaraja'])}</section>
<section class="md"><h2>Mitä työpajan lopussa on</h2>{render(secs['Mitä työpajan lopussa on'])}</section>
<section class="md"><h2>Projektikansioon syntyvät tiedostot</h2>{render(secs['Projektikansioon syntyvät tiedostot'])}</section>"""
    (ROOT / "index.html").write_text(page("Vibekoodaus-työpaja: Oppisopimustäyttäjä", body, 0), encoding="utf-8")


def main() -> None:
    if not (ROOT / "assets" / "style.css").exists():
        sys.exit("assets/style.css puuttuu")
    for d in ("claude", "codex", "ohjaaja"):
        if (ROOT / d).exists():
            shutil.rmtree(ROOT / d)
    rows = schedule()
    build_index(rows)
    for key in PATHS:
        build_student(key, rows)
    build_teacher(rows)
    n = len(list(ROOT.glob("**/*.html")))
    print(f"Valmis: {n} HTML-sivua, {_counter['n']} kopioitavaa lohkoa.")


if __name__ == "__main__":
    main()
