"""Word-level diff of section files between a git commit and the working tree, as HTML.

Usage: python3 01_Report/assembly/diff_sections.py <commit> <out.html> <section files...>
Insertions are green, deletions red struck through. Working notes (changelogs, IDs/TODO
blocks) are stripped first, so the diff shows only what a reader of the report sees.
"""
import difflib
import html
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble_draft import clean  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def words(text: str) -> list[str]:
    return re.findall(r"\S+|\n", text)


def main() -> None:
    commit, out, files = sys.argv[1], Path(sys.argv[2]), sys.argv[3:]
    blocks = []
    for f in files:
        rel = f"01_Report/sections/{Path(f).name}"
        old = subprocess.run(["git", "show", f"{commit}:{rel}"], cwd=ROOT, capture_output=True,
                             text=True).stdout
        new = (ROOT / rel).read_text(encoding="utf-8")
        a, b = words(clean(old)), words(clean(new))
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        parts, added, removed = [], 0, 0
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                parts.append(html.escape(" ".join(a[i1:i2])))
            if op in ("delete", "replace"):
                removed += i2 - i1
                parts.append(f"<del>{html.escape(' '.join(a[i1:i2]))}</del>")
            if op in ("insert", "replace"):
                added += j2 - j1
                parts.append(f"<ins>{html.escape(' '.join(b[j1:j2]))}</ins>")
        body = " ".join(parts).replace(" \n ", "<br>").replace("\n", "<br>")
        blocks.append(f"<h2>{html.escape(Path(f).name)}</h2><p class=stat>+{added} words added, "
                      f"−{removed} words removed</p><div class=t>{body}</div>")
    out.write_text(f"""<!doctype html><html><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>Yellow sections: merge changes</title>
<style>:root{{--bg:#fff;--fg:#1a1a1a;--ins:#d4f5dc;--del:#fde0e0}}
@media (prefers-color-scheme:dark){{:root{{--bg:#16181c;--fg:#e8e8e8;--ins:#1f4a2c;--del:#5a2323}}}}
body{{background:var(--bg);color:var(--fg);font:15px/1.55 system-ui,sans-serif;max-width:860px;margin:0 auto;padding:16px}}
ins{{background:var(--ins);text-decoration:none}} del{{background:var(--del)}} .stat{{opacity:.75}}
.t{{overflow-wrap:anywhere}}</style></head><body><h1>Yellow sections: merge with Leroy's text</h1>
<p>Green = added (mostly from Leroy's §3.4–3.6), red struck = removed or replaced. Changelogs and working notes are hidden.</p>
{''.join(blocks)}</body></html>""", encoding="utf-8")
    print("wrote", out)


if __name__ == "__main__":
    main()
