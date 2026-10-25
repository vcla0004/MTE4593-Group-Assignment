"""Assemble a draft report from 01_Report/sections/ (Q19 draft build).

Strips working notes (Rubric coverage lines, HTML-comment changelogs, the
"IDs covered" and "Remaining TODOs" blocks) and keeps every [TO VERIFY]/[TODO]
marker. Missing sections get a visible placeholder. Prints word counts per
section, split into prose and table words, for the page-limit check (H6:
tables count towards the limit).

Run from the repo root:  python3 01_Report/assembly/assemble_draft.py
Final build:  assemble_draft.py, then check_refs.py, then assemble_draft.py --final
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / "01_Report" / "sections"
OUT_MD = ROOT / "01_Report" / "assembly" / "draft-assembled.md"
OUT_DOCX = ROOT / "01_Report" / "draft-assembled.docx"
OUT_FINAL = ROOT / "01_Report" / "MTE4593 Group 9 SMR Report.docx"
OUT_REVIEW = ROOT / "01_Report" / "MTE4593 Group 9 SMR Report - TEAM REVIEW.docx"
REF_DOCX = ROOT / "01_Report" / "assembly" / "reference.docx"  # make_reference_doc.py

# Body order; None means the section is not in the repo yet (placeholder).
ORDER = [
    ("0-abstract.md", None),
    ("1-introduction.md", None),
    ("2-methods-data.md", None),
    ("3-barriers.md", None),
    ("4.1-technology-projects.md", "4.1 Technology, projects and patents (Leroy)"),
    ("4.2-bwrx300-darlington.md", "4.2 BWRX-300 at Darlington (Leroy)"),
    ("4.3-initiative.md", None),
    ("5-materials-life-cycle.md", "5 Materials from extraction to end-of-life (Leroy)"),
    ("6-lca-eco-audit.md", None),
    ("7-carbon-avoided.md", None),
    ("8.1-law-regulation-licensing.md", None),
    ("8.2-economics-finance.md", None),
    ("8.3-supply-concentration.md", None),
    ("8.4-social-licence.md", None),
    ("8.5-stakeholders-money.md", None),
    ("8.6-implementation.md", None),
    ("9-tbl-mcda.md", None),
    ("10-future-materials.md", "10 Future material properties and processes (Leroy)"),
    ("11-conclusions.md", None),
]
APPENDICES = [
    "appendix-A-lca-inventory.md",
    "appendix-B-policy-and-supply-working.md",
    "appendix-B-moved-from-8.4-8.6.md",  # merged into App B at the end
    "appendix-C-sensitivity.md",
    "appendix-E-search-log.md",
]
REFS = "12-references.md"
FIG_DIR = ROOT / "03_LCA_Calculations" / "results"
FIG_RE = re.compile(r"^\[Figure F?(\d+)[.:]\s*(.*)\]\s*$")
REVIEW = "--review" in sys.argv
FINAL = "--final" in sys.argv or REVIEW
PAGE_BREAK = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'


TITLE = """---
title: "Small modular reactors: where they cut the most carbon, what holds them back, and a low-clinker concrete initiative for Darlington"
subtitle: "MTE4593 Materials and Sustainability, Assignment 2 (Group 9)"
author:
  - "Victor Clarke [TODO: student ID]"
  - "Leroy Louis Jean (33880212)"
  - "Sam [TODO: surname] [TODO: student ID]"
date: "October 2026"
---

"""
# Team-review build: highlighted notes placed after the first heading of each file.
def note(text: str) -> str:
    return f"[{text}]{{custom-style=\"TeamNote\"}}\n"

GRANTA = ("run the Granta EduPack Eco Audit on one BWRX-300: concrete 120,000 t (50,000 m³ × 2.4 t/m³) "
          "and steel 14,000 t (Ostrołęka PIS, Table 14), with a second run where 40% of the concrete "
          "(20,000 m³) is LC³ at 270 instead of 380 kg CO₂e/m³ (Pillai et al., 2019). Send the CO₂ "
          "footprint and energy per life stage (screenshot or export)")
NOTES = {
    "6-lca-eco-audit.md": "LEROY (Granta EduPack): please " + GRANTA + ". Then confirm or update this "
        "section's Granta sentence, Appendix A9 and §2. Everything else in the report is complete.",
    "appendix-A-lca-inventory.md": "LEROY: your Granta EduPack results go in A9 (currently 'planned but not completed').",
    "2-methods-data.md": "LEROY: once Granta is run, this section's Granta sentence changes to describe it.",
}
CHECKLIST = """## Team review checklist (this page is removed in the submission version)

[Highlighted notes like this one mark what is still needed. Everything else is complete and fact-checked.]{custom-style="TeamNote"}

**Leroy: Granta EduPack** (the only open technical item)

- Run the Granta EduPack Eco Audit as set out in the note at the top of §6, and send the results (screenshots or export).
- The results go in §6, Appendix A9 and one sentence in §2. The report currently says Granta was planned but not completed.

**Everyone**

- Title page: Victor's and Sam's student IDs, and Sam's surname (Leroy's is in).
- Agree the AI-use declaration wording (placeholder before the appendices).

**Victor (before submitting)**

- Update the table of contents in Word (right-click, Update Field).

"""

DECLARATION = """## Declaration of generative AI use

[TODO: team to write the AI-use declaration required by the unit (CLAUDE.md: the team decides how AI use is declared).]
"""
DROP_HEADINGS = ("IDs covered", "Remaining TODOs")
PARENT = {"4.1-technology-projects.md": "## 4 The technology and the initiative\n\n",
          "8.1-law-regulation-licensing.md": "## 8 Non-technical factors affecting translation to practice\n\n"}


def clean(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"^Rubric coverage:.*$", "", text, flags=re.M)
    out, skipping = [], False
    for line in text.splitlines():
        m = re.match(r"^(#{1,6}) (.*)", line)
        if m:
            skipping = any(m.group(2).startswith(h) for h in DROP_HEADINGS)
        if not skipping:
            out.append(line)
    out = [figure(line) for line in out]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def figure(line: str) -> str:
    """Turn a "[Figure Fn. caption]" placeholder into an embedded image if its PNG exists."""
    m = FIG_RE.match(line.strip())
    if not m:
        return line
    n, caption = m.group(1), m.group(2)
    pngs = sorted(FIG_DIR.glob(f"F{n}_*.png"))
    if pngs:
        return f"![Figure F{n}. {caption}]({pngs[0]}){{width=95%}}"
    return f"**[TODO: Figure F{n} image missing]** *Figure F{n}. {caption}*"


def words(text: str) -> tuple[int, int]:
    prose = table = 0
    for line in text.splitlines():
        n = len(re.findall(r"\w[\w'’.,%/×–-]*", line))
        if line.lstrip().startswith("|"):
            table += n
        elif not line.startswith("#"):
            prose += n
    return prose, table


def renumber_tables(bodies: list[str]) -> list[str]:
    """Renumber body tables T1, T2, ... in caption order.

    Labels captioned in a file map to their new numbers within that file (so two
    sections that both used "T10" get different numbers); a label only referred to
    in a file uses the first file that captions it. Appendix tables (B12, A3, ...)
    are untouched.
    """
    cap_re = re.compile(r"Table T(\d+[a-z]?)[.:]")
    n, local, first = 0, [], {}
    for body in bodies:
        mapping = {}
        for old in cap_re.findall(body):
            if old not in mapping:
                n += 1
                mapping[old] = n
                first.setdefault(old, n)
        local.append(mapping)
    out = []
    for body, mapping in zip(bodies, local):
        def sub(m):
            old = m.group(1)
            new = mapping.get(old, first.get(old))
            return f"T{new}" if new else m.group(0)
        out.append(re.sub(r"\bT(\d+[a-z]?)\b", sub, body))
    return out, first


APP_T = re.compile(r"\b(Tables?) T(\d+[a-z]?)(?:( and )T(\d+[a-z]?))?\b")


def renum_app(text: str, first: dict) -> str:
    """In appendices, point "Table(s) T…" at the new body numbers (grid labels T1/T2 untouched)."""
    def sub(m):
        out = f"{m.group(1)} T{first.get(m.group(2), m.group(2))}"
        return out + (f"{m.group(3)}T{first.get(m.group(4), m.group(4))}" if m.group(4) else "")
    return APP_T.sub(sub, text)


def main() -> None:
    parts, rows = [], []
    for name, placeholder in ORDER:
        f = SEC / name
        if f.exists():
            body = clean(f.read_text(encoding="utf-8"))
        elif placeholder:
            body = f"## {placeholder}\n\n**[TODO: section not yet in the repo]**\n"
        else:
            raise SystemExit(f"missing {name}")
        if REVIEW and name in NOTES:
            body = re.sub(r"^(#{1,6} .*\n)", lambda m: m.group(1) + "\n" + note(NOTES[name]) + "\n",
                          body, count=1, flags=re.M)
        if name[:2] in ("4.", "8."):
            body = re.sub(r"^(#{2,5}) ", r"#\1 ", body, flags=re.M)
        if not body.lstrip().startswith(PARENT.get(name, "##").strip()):
            body = PARENT.get(name, "") + body
        parts.append(body)
        rows.append((name, *words(body)))
    parts, first = renumber_tables(parts)
    parts[0] = PAGE_BREAK + parts[0]  # abstract starts after the title page and contents
    parts.append(PAGE_BREAK)
    if (SEC / REFS).exists():  # full list; check_refs.py only reports mismatches
        parts.append(clean((SEC / REFS).read_text(encoding="utf-8")))
    else:
        parts.append("## References\n\n**[TODO: reference list]**\n")
    parts.append("## Declaration of generative AI use\n\n" + note("TEAM: agree the AI-use declaration wording and add it here.")
                 if REVIEW else DECLARATION)
    parts.append(PAGE_BREAK + "# Appendices\n")
    for name in APPENDICES:
        f = SEC / name
        if f.exists():
            app = clean(f.read_text(encoding="utf-8"))
            if REVIEW and name in NOTES:
                app = re.sub(r"^(#{1,6} .*\n)", lambda m: m.group(1) + "\n" + note(NOTES[name]) + "\n",
                             app, count=1, flags=re.M)
            parts.append(renum_app(app, first))
        elif "moved" not in name and "appendix-E" not in name:
            parts.append(f"## {name}\n\n**[TODO: not yet in the repo]**\n")
    if REVIEW:
        hl = '[{}]{{custom-style=\\"TeamNote\\"}}'
        head = (TITLE.replace("[TODO: student ID]", hl.format("ADD STUDENT ID"))
                .replace("[TODO: surname]", hl.format("ADD SURNAME")))
        head += PAGE_BREAK + CHECKLIST
    elif FINAL:
        head = TITLE
    else:
        head = ('---\ntitle: "Small modular reactors: DRAFT (assembled from sections)"\n---\n\n'
            "**Draft for the team, not the submission.** Every [TO VERIFY] and [TODO] "
            "marker is still open. Leroy's sections are placeholders until they are in the repo.\n\n")
    OUT_MD.write_text(head + "\n\n".join(parts), encoding="utf-8")
    out_docx = OUT_REVIEW if REVIEW else OUT_FINAL if FINAL else OUT_DOCX
    subprocess.run(["pandoc", "-f", "markdown-tex_math_dollars", str(OUT_MD), "-o", str(out_docx),
                    f"--reference-doc={REF_DOCX}", "--toc", "--columns=10000"], check=True)
    tp = tt = 0
    print(f"{'section':42} {'prose':>6} {'table':>6}")
    for name, p, t in rows:
        tp, tt = tp + p, tt + t
        print(f"{name:42} {p:6} {t:6}")
    print(f"{'BODY TOTAL':42} {tp:6} {tt:6}  (~{(tp + tt) / 500:.1f} pages at 500 words/page)")
    full = OUT_MD.read_text(encoding="utf-8")
    print("markers left: TO VERIFY", full.count("[TO VERIFY"), "| TODO", full.count("[TODO"))


if __name__ == "__main__":
    main()
