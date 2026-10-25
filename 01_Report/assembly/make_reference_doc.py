"""Build the pandoc reference doc: the team template plus pandoc's missing styles.

The team template (01_Report/MTE4593 Report.docx) defines only 12 styles, so pandoc's
tables, captions and body paragraphs fall back badly (cells stack one per line). This
copies every style pandoc's default reference.docx defines that the template lacks,
keeping the template's header, footer, fonts and margins.
Output: 01_Report/assembly/reference.docx
"""
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "MTE4593 Report.docx"
OUT = HERE / "reference.docx"


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        default = Path(tmp) / "default.docx"
        subprocess.run(["pandoc", "-o", str(default), "--print-default-data-file",
                        "reference.docx"], check=True)
        dstyles = zipfile.ZipFile(default).read("word/styles.xml").decode("utf-8")
        tz = zipfile.ZipFile(TEMPLATE)
        tstyles = tz.read("word/styles.xml").decode("utf-8")
        have = set(re.findall(r'w:styleId="([^"]+)"', tstyles))
        add = [m.group(0) for m in re.finditer(r"<w:style [^>]*>.*?</w:style>", dstyles, re.S)
               if re.search(r'w:styleId="([^"]+)"', m.group(0)).group(1) not in have]
        # table cell text (pandoc's "Compact" paragraphs) at 9 pt to keep tables short
        add = [re.sub(r"(<w:style [^>]*w:styleId=\"Compact\"[^>]*>.*?)(</w:style>)",
                      r'\1<w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>\2', a, flags=re.S)
               for a in add]
        # highlighted character style for the team-review build (--review)
        add.append('<w:style w:type="character" w:customStyle="1" w:styleId="TeamNote">'
                   '<w:name w:val="Team Note"/><w:rPr><w:b/><w:color w:val="C00000"/>'
                   '<w:highlight w:val="yellow"/></w:rPr></w:style>')
        merged = tstyles.replace("</w:styles>", "".join(add) + "</w:styles>")
        with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in tz.infolist():
                data = merged.encode("utf-8") if item.filename == "word/styles.xml" else tz.read(item)
                zout.writestr(item, data)
    print(f"added {len(add)} styles -> {OUT}")


if __name__ == "__main__":
    main()
