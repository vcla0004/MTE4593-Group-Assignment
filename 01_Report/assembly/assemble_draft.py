"""Assemble a draft report from 01_Report/sections/ (Q19 draft build).

Strips working notes (Rubric coverage lines, HTML-comment changelogs, the
"IDs covered" and "Remaining TODOs" blocks) and keeps every [TO VERIFY]/[TODO]
marker. Missing sections get a visible placeholder. Prints word counts per
section, split into prose and table words, for the page-limit check (H6:
tables count towards the limit).

Run from the repo root:  python3 01_Report/assembly/assemble_draft.py
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
REF_DOCX = ROOT / "01_Report" / "MTE4593 Report.docx"

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
    "appendix-C-sensitivity.md",
    "appendix-E-search-log.md",
]
REFS = "12-references.md"
FIG_DIR = ROOT / "03_LCA_Calculations" / "results"
FIG_RE = re.compile(r"^\[Figure F?(\d+)[.:]\s*(.*)\]\s*$")
FINAL = "--final" in sys.argv

TITLE = """---
title: "Small modular reactors: where they cut the most carbon, what holds them back, and a low-clinker concrete initiative for Darlington"
subtitle: "MTE4593 Materials and Sustainability, Assignment 2 (Group 9)"
author:
  - "Victor Clarke [TODO: student ID]"
  - "Leroy Jean [TODO: student ID]"
  - "Sam [TODO: surname] [TODO: student ID]"
date: "October 2026"
---

"""
DECLARATION = """## Declaration of generative AI use

[TODO: team to write the AI-use declaration required by the unit (CLAUDE.md: the team decides how AI use is declared).]
"""
DROP_HEADINGS = ("IDs covered", "Remaining TODOs")


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
        return f"![Figure {n}. {caption}]({pngs[0]}){{width=95%}}"
    return f"**[TODO: Figure {n} image missing]** *Figure {n}. {caption}*"


def words(text: str) -> tuple[int, int]:
    prose = table = 0
    for line in text.splitlines():
        n = len(re.findall(r"\w[\w'’.,%/×–-]*", line))
        if line.lstrip().startswith("|"):
            table += n
        elif not line.startswith("#"):
            prose += n
    return prose, table


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
        parts.append(body)
        rows.append((name, *words(body)))
    if (SEC / REFS).exists():
        parts.append(clean((SEC / REFS).read_text(encoding="utf-8")))
    else:
        parts.append("## References\n\n**[TODO: reference list]**\n")
    parts.append(DECLARATION)
    parts.append("# Appendices\n")
    for name in APPENDICES:
        f = SEC / name
        if f.exists():
            parts.append(clean(f.read_text(encoding="utf-8")))
        else:
            parts.append(f"## {name}\n\n**[TODO: not yet in the repo]**\n")
    if FINAL:
        head = TITLE
    else:
        head = ('---\ntitle: "Small modular reactors: DRAFT (assembled from sections)"\n---\n\n'
            "**Draft for the team, not the submission.** Every [TO VERIFY] and [TODO] "
            "marker is still open. Leroy's sections are placeholders until they are in the repo.\n\n")
    OUT_MD.write_text(head + "\n\n".join(parts), encoding="utf-8")
    out_docx = OUT_FINAL if FINAL else OUT_DOCX
    subprocess.run(["pandoc", "-f", "markdown-tex_math_dollars", str(OUT_MD), "-o", str(out_docx),
                    f"--reference-doc={REF_DOCX}", "--toc"], check=True)
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
