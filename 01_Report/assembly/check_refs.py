"""Match the reference list against the in-text citations of the cleaned report body.

Reads 01_Report/assembly/draft-assembled.md (run assemble_draft.py first) and
01_Report/sections/12-references.md. Report only (the final build prints the full list):
prints uncited entries and in-text citations that
have no entry. Matching is heuristic (first author word + year), so read the
printed lists before submitting.
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEC = HERE.parent / "sections"
BODY = HERE / "draft-assembled.md"
REFS = SEC / "12-references.md"
OUT = HERE / "references-cited.md"

ENTRY_RE = re.compile(r"^(?P<author>.+?),? (?P<year>(?:19|20)\d\d[a-z]?|n\.d\.)[.,]?(?:\s|$)")
CITE_RE = re.compile(r"(?:\(|; )([A-Z][\w’'.&-]+(?: [A-Z][\w’'.&-]+)*?)(?: et al\.)?(?: and [A-Z][\w’'-]+)?,? \(?((?:19|20)\d\d[a-z]?|n\.d\.)")
SKIP = {"The", "A", "An"}


def key_word(author: str) -> str:
    words = [w for w in re.findall(r"[A-Z][\w’'-]+", author) if w not in SKIP]
    return words[0] if words else author.split()[0]


def main() -> None:
    body_full = BODY.read_text(encoding="utf-8")
    body = body_full.split("## References")[0] + body_full.split("# Appendices")[-1]
    text = REFS.read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    head, _, rest = text.partition("## References")
    kept, dropped, keys = [], [], set()
    for para in [p.strip() for p in rest.split("\n\n") if p.strip()]:
        if para.startswith("#"):
            kept.append(para)
            continue
        m = ENTRY_RE.match(para)
        if not m:
            kept.append(para)  # Acts etc.: keep, check by hand
            continue
        kw, yr = key_word(m.group("author")), m.group("year")
        keys.add((kw, yr))
        keys.add((kw, yr[:4]))
        yr_body = yr if yr == "n.d." else yr[:4]  # tolerate a missing a/b suffix in the text
        if re.search(re.escape(kw) + r"[^\n]{0,120}?" + re.escape(yr_body), body):
            kept.append(para)
        else:
            dropped.append(para[:90])
    missing = set()
    for m in CITE_RE.finditer(body):
        kw, yr = key_word(m.group(1)), m.group(2)
        if (kw, yr) not in keys and kw not in {"Table", "Figure", "Appendix", "Section", "Units", "Unit"}:
            missing.add(f"{m.group(1)} {yr}")
    print(f"kept {len(kept)}, dropped {len(dropped)} uncited")
    for d in dropped:
        print("  uncited:", d)
    print(f"in-text citations with no entry (heuristic): {len(missing)}")
    for x in sorted(missing):
        print("  missing:", x)


if __name__ == "__main__":
    main()
