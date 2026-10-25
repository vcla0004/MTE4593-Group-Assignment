"""Remove bookmarks (and the internal links that point to them) from built .docx files.

Pandoc bookmarks every heading and the filled contents links to them; Google Docs shows each
bookmark as an icon. External web links (the URLs in the references) are kept.
Usage: python3 01_Report/assembly/strip_bookmarks.py <file.docx> [...]
"""
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path


def strip(xml: str) -> str:
    xml = re.sub(r"<w:bookmark(?:Start|End)\b[^>]*/>", "", xml)
    # unwrap internal hyperlinks (w:anchor, no r:id); keep their text runs
    return re.sub(r'<w:hyperlink\b(?![^>]*r:id)[^>]*w:anchor="[^"]*"[^>]*>(.*?)</w:hyperlink>', r"\1",
                  xml, flags=re.S)


def main() -> None:
    for f in sys.argv[1:]:
        src = Path(f)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp_path = Path(tmp.name)
        with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item)
                if item.filename == "word/document.xml":
                    before = data.decode("utf-8")
                    after = strip(before)
                    print(f, "bookmarks removed:", len(re.findall(r"<w:bookmarkStart", before)))
                    data = after.encode("utf-8")
                zout.writestr(item, data)
        shutil.move(tmp_path, src)


if __name__ == "__main__":
    main()
