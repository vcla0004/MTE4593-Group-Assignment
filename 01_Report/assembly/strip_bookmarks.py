"""Final clean-up of built .docx files: remove bookmarks, set 1 pt table borders.

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


BORDER = "".join(f'<w:{side} w:val="single" w:sz="8" w:space="0" w:color="000000"/>'  # 1 pt
                 for side in ("top", "left", "bottom", "right"))
TBL_BORDERS = ("<w:tblBorders>" + BORDER + '<w:insideH w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
               '<w:insideV w:val="single" w:sz="8" w:space="0" w:color="000000"/></w:tblBorders>')


def table_borders(xml: str) -> str:
    """Give every table and cell a 1 pt black border (LibreOffice writes empty cell borders)."""
    xml = re.sub(r"<w:tcBorders>.*?</w:tcBorders>|<w:tcBorders/>", "<w:tcBorders>" + BORDER + "</w:tcBorders>",
                 xml, flags=re.S)
    xml = re.sub(r"<w:tcPr>(?:(?!</w:tcPr>).)*?</w:tcPr>",
                 lambda m: m.group(0) if "<w:tcBorders>" in m.group(0)
                 else m.group(0).replace("</w:tcPr>", "<w:tcBorders>" + BORDER + "</w:tcBorders></w:tcPr>"),
                 xml, flags=re.S)
    xml = re.sub(r"<w:tblBorders>.*?</w:tblBorders>", "", xml, flags=re.S)
    return re.sub(r"(<w:tblPr>(?:(?!</w:tblPr>).)*?)(<w:tblLayout|<w:tblCellMar|<w:tblLook|</w:tblPr>)",
                  lambda m: m.group(1) + TBL_BORDERS + m.group(2), xml, count=0, flags=re.S)


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
                    after = table_borders(strip(before))
                    print(f, "bookmarks removed:", len(re.findall(r"<w:bookmarkStart", before)))
                    data = after.encode("utf-8")
                zout.writestr(item, data)
        shutil.move(tmp_path, src)


if __name__ == "__main__":
    main()
