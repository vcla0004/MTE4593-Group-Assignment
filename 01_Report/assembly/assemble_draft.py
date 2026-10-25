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
ORDER = [  # body in the team template's structure (01_Report/MTE4593 Report.docx, extended as in Leroy's draft)
    ("0-abstract.md", None),
    ("1-introduction.md", None),
    ("2-methods-data.md", None),
    ("4.1-technology-projects.md", None),
    ("4.2-bwrx300-darlington.md", None),
    ("3-barriers.md", None),
    ("4.3-initiative.md", None),
    ("5-materials-life-cycle.md", None),
    ("6-lca-eco-audit.md", None),
    ("7-carbon-avoided.md", None),
    ("8.5-stakeholders-money.md", None),
    ("8.4-social-licence.md", None),
    ("8.2-economics-finance.md", None),
    ("8.3-supply-concentration.md", None),
    ("8.1-law-regulation-licensing.md", None),
    ("8.6-implementation.md", None),
    ("9-tbl-mcda.md", None),
    ("10-future-materials.md", None),
    ("11-conclusions.md", None),
]
# Section numbers in the source files -> numbers in the template structure
NUM_MAP = {"1": "1", "2": "2", "4": "3.1", "4.1": "3.1.1", "4.2": "3.1.2", "3": "3.1.3",
           "4.3": "3.1.4", "5": "3.1.5", "6": "3.2", "7": "3.3", "8": "3.4–3.6",
           "8.5": "3.4.1", "8.4": "3.4.2", "8.2": "3.5.1", "8.3": "3.5.2", "8.1": "3.6.1",
           "8.6": "3.6.2", "9": "3.7", "10": "3.8", "11": "4"}
HEADING_TEXT = {"2": "Data Sources/Methodology", "4.1": "Current Projects and Patents",
                "4.2": "Technical Descriptions: the BWRX-300 at Darlington", "6": "Lifecycle Analysis",
                "7": "National Strategies and Industrial Policies: Carbon Avoided in Ontario and Australia",
                "11": "Conclusion"}


def map_num(num: str) -> str:
    num = num.rstrip(".")
    if num in NUM_MAP:
        return NUM_MAP[num]
    head, _, rest = num.partition(".")
    return NUM_MAP[head] + "." + rest if head in NUM_MAP and rest else num


def restructure(body: str) -> str:
    """Renumber headings to the template structure; heading level follows the new number's depth."""
    def sub(m):
        old, text = m.group(2), m.group(3)
        new = map_num(old)
        text = HEADING_TEXT.get(old, text)
        return "#" * (new.count(".") + 1) + f" {new} {text}"
    body = re.sub(r"^(#{1,6}) (\d+(?:\.\d+)*) (.*)$", sub, body, flags=re.M)
    return re.sub(r"^#{1,6} Abstract\s*$", "# Abstract", body, flags=re.M)
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


def _p(text: str, style: str = "", size: int = 0, before: int = 0, italic: bool = False) -> str:
    ppr = f'<w:pStyle w:val="{style}"/>' if style else ""
    rpr = (f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>' if size else "") + ("<w:i/>" if italic else "")
    return (f'<w:p><w:pPr>{ppr}<w:jc w:val="center"/><w:spacing w:before="{before}" w:after="120"/></w:pPr>'
            f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{text}</w:t></w:r></w:p>')


AUTHORS = "Authors: Leroy Louis Jean (33880212), Sam [surname] ([student ID]), Victor Clarke ([student ID])"
TITLE = ("```{=openxml}\n"
         + _p("Small Modular Reactors", "Title", before=3600)
         + _p("MTE4593 Assignment 2", "Subtitle")
         + _p("Where small modular reactors cut the most carbon, what holds them back, and a "
              "low-clinker concrete initiative for Darlington", size=22, before=240, italic=True)
         + _p("{AUTHORS}", size=20, before=600)
         + _p("Date of Submission: 25 October 2026", size=20)
         + "\n```\n\n")
TOC = ("```{=openxml}\n"
       '<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Table of Contents</w:t></w:r></w:p>'
       '<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
       '<w:r><w:instrText xml:space="preserve">TOC \\o "1-3" \\h \\z \\u</w:instrText></w:r>'
       '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
       '<w:r><w:t>Right-click here and choose Update Field to build the table of contents.</w:t></w:r>'
       '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>'
       "\n```\n")
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

DECLARATION = """# Declaration of generative AI use

[TODO: team to write the AI-use declaration required by the unit (CLAUDE.md: the team decides how AI use is declared).]
"""
DROP_HEADINGS = ("IDs covered", "Remaining TODOs")
PARENT = {"4.1-technology-projects.md": "# 3 Discussion\n\n## 3.1 Overview of SMR\n\n",
          "8.5-stakeholders-money.md": "## 3.4 Stakeholder Analysis\n\n",
          "8.2-economics-finance.md": "## 3.5 Market Analysis and Economic Feasibility\n\n",
          "8.1-law-regulation-licensing.md": "## 3.6 Government Regulations Review\n\n"}


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


LABEL_RENAME = {"C1": "The initiative (C1)", "LCA": "Life-cycle assessment"}


def no_section_signs(text: str) -> str:
    """Replace "§" cross-references with words in the template numbering ("Section 3.3").

    A "§" that points into a results file or an external document (`results/x.md` §3,
    Guidelines (2010), §5.3) keeps its own number and becomes lower-case "section".
    """
    num = r"\d+(?:\.\d+)*[a-z]?"

    def internal(m) -> bool:
        before = text[max(0, m.start() - 20):m.start()]
        return not any(k in before for k in (".md", "`", "Guidelines", "brief"))

    def rng(m):
        if not internal(m):
            return f"section {m.group(1)}{m.group(2)}{m.group(3)}"
        if m.group(1).startswith("8") and m.group(3).startswith("8"):
            return "Sections 3.4–3.6"
        start, end = map_num(m.group(1)).split("–")[0], map_num(m.group(3)).split("–")[-1]
        return f"Sections {start}{m.group(2)}{end}"

    def one(m):
        if not internal(m):
            return f"section {m.group(1)}"
        new = map_num(m.group(1))
        return f"Sections {new}" if "–" in new else f"Section {new}"
    text = re.sub(r"§§\s*", "§", text)
    text = re.sub(r"(§\s*\d[\d.]*[a-z]?\s*[–-])\s*§\s*", r"\1", text)  # "§6–§8" -> "§6–8"
    text = re.sub(rf"§\s*({num})\s*([–-])\s*({num})", rng, text)
    text = re.sub(rf"§\s*({num})", one, text)
    return text.replace("§", "Section ")


def report_style(body: str) -> str:
    """Make draft notes read as report prose.

    - a short bold label opening a paragraph ("**Canada.** ...") becomes a level-4 heading;
    - a longer bold opening sentence, and any other bold inside prose, becomes plain text;
    - bulleted or numbered lists become one running paragraph.
    Tables and headings are left alone.
    """
    out = []
    for para in body.split("\n\n"):
        lines = para.strip("\n").split("\n")
        first = lines[0] if lines else ""
        if not first or first.startswith(("#", "|", "!", "```", "*Table", "*Source", "[")) or "custom-style" in para:
            out.append(para)
            continue
        is_item = [bool(re.match(r"\s*(?:[-*]|\d+\.)\s", ln)) for ln in lines]
        was_list = len(lines) > 1 and all(is_item[1:])  # an optional lead-in line, then items
        if was_list and not first.lstrip().startswith(("#### ",)) and "Research questions" not in para:
            items = [re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", ln) for ln in lines if ln.strip()]
            para = " ".join(i if i.rstrip().endswith((".", ":", ";", "?")) else i.rstrip() + "." for i in items)
        else:
            was_list = was_list and False
        m = re.match(r"\*\*([^*]+?)\*\*\s*(.*)", para, re.S)
        if m and not was_list and len(m.group(1).split()) <= 4 and m.group(1).rstrip().endswith((".", ":")):
            label = m.group(1).rstrip().rstrip(".:")
            out.append(f"#### {LABEL_RENAME.get(label, label)}")
            para = m.group(2)
        out.append(para.replace("**", ""))
    return "\n\n".join(out)


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
        body = restructure(report_style(body))
        body = PARENT.get(name, "") + body
        parts.append(body)
        rows.append((name, *words(body)))
    parts, first = renumber_tables(parts)
    parts[0] = PAGE_BREAK + parts[0] + "\n\n" + PAGE_BREAK + TOC + PAGE_BREAK  # abstract page, contents page
    parts.append(PAGE_BREAK)
    if (SEC / REFS).exists():  # full list; check_refs.py only reports mismatches
        parts.append(re.sub(r"^## References", "# 5 References",
                            clean((SEC / REFS).read_text(encoding="utf-8")), flags=re.M))
    else:
        parts.append("# 5 References\n\n**[TODO: reference list]**\n")
    parts.append("# Declaration of generative AI use\n\n" + note("TEAM: agree the AI-use declaration wording and add it here.")
                 if REVIEW else DECLARATION)
    parts.append(PAGE_BREAK + "# Appendices\n")
    for name in APPENDICES:
        f = SEC / name
        if f.exists():
            app = clean(f.read_text(encoding="utf-8"))
            if REVIEW and name in NOTES:
                app = re.sub(r"^(#{1,6} .*\n)", lambda m: m.group(1) + "\n" + note(NOTES[name]) + "\n",
                             app, count=1, flags=re.M)
            # appendix subsections sit below the contents' three levels (only "Appendix X" is listed)
            app = re.sub(r"^(#{3,5}) ", r"#\1 ", app, flags=re.M)
            parts.append(renum_app(app, first))
        elif "moved" not in name and "appendix-E" not in name:
            parts.append(f"## {name}\n\n**[TODO: not yet in the repo]**\n")
    if REVIEW:
        head = TITLE.replace("{AUTHORS}", AUTHORS.replace("[surname]", "ADD SURNAME")
                             .replace("[student ID]", "ADD STUDENT ID")) + PAGE_BREAK + CHECKLIST
    elif FINAL:
        head = TITLE.replace("{AUTHORS}", AUTHORS)
    else:
        head = ('---\ntitle: "Small modular reactors: DRAFT (assembled from sections)"\n---\n\n'
            "**Draft for the team, not the submission.** Every [TO VERIFY] and [TODO] "
            "marker is still open. Leroy's sections are placeholders until they are in the repo.\n\n")
    OUT_MD.write_text(no_section_signs(head + "\n\n".join(parts)), encoding="utf-8")
    out_docx = OUT_REVIEW if REVIEW else OUT_FINAL if FINAL else OUT_DOCX
    subprocess.run(["pandoc", "-f", "markdown-tex_math_dollars", str(OUT_MD), "-o", str(out_docx),
                    f"--reference-doc={REF_DOCX}", "--columns=10000"], check=True)
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
