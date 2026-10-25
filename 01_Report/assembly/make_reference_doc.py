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


BLUE = "595959"  # table rules: neutral dark grey, to match the template
TABLE_STYLE = (
    '<w:style w:type="table" w:default="1" w:styleId="Table"><w:name w:val="Table"/>'
    '<w:basedOn w:val="TableNormal"/><w:qFormat/>'
    '<w:pPr><w:spacing w:before="20" w:after="20"/></w:pPr>'
    '<w:tblPr><w:tblInd w:w="0" w:type="dxa"/>'
    '<w:tblBorders><w:top w:val="single" w:sz="8" w:space="0" w:color="' + BLUE + '"/>'
    '<w:bottom w:val="single" w:sz="8" w:space="0" w:color="' + BLUE + '"/>'
    '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/></w:tblBorders>'
    '<w:tblCellMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
    '<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr>'
    '<w:tblStylePr w:type="firstRow"><w:rPr><w:b/></w:rPr>'
    '<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="EDEDED"/></w:tcPr></w:tblStylePr>'
    '</w:style>')


def set_style(xml: str, sid: str, new: str) -> str:
    return re.sub(r'<w:style [^>]*w:styleId="' + sid + r'"[^>]*>.*?</w:style>', lambda m: new, xml,
                  count=1, flags=re.S)


def add_props(xml: str, sid: str, ppr: str = "", rpr: str = "") -> str:
    """Append paragraph and run properties to an existing style."""
    def sub(m):
        st = m.group(0)
        if ppr:
            st = (st.replace("</w:pPr>", ppr + "</w:pPr>", 1) if "<w:pPr>" in st
                  else st.replace("</w:style>", "<w:pPr>" + ppr + "</w:pPr></w:style>"))
        if rpr:
            st = (st.replace("</w:rPr>", rpr + "</w:rPr>", 1) if "<w:rPr>" in st
                  else st.replace("</w:style>", "<w:rPr>" + rpr + "</w:rPr></w:style>"))
        return st
    return re.sub(r'<w:style [^>]*w:styleId="' + sid + r'"[^>]*>.*?</w:style>', sub, xml, count=1, flags=re.S)


def polish(xml: str) -> str:
    """House style for the submission: the template's headings, ruled tables, quiet captions."""
    xml = set_style(xml, "Table", TABLE_STYLE)
    # headings keep the team template's own (black) styling; declare outline levels so a
    # table of contents can be built outside Word too (update_toc.py)
    for lvl, sid in enumerate(("Heading1", "Heading2", "Heading3", "Heading4")):
        xml = add_props(xml, sid, ppr=f'<w:outlineLvl w:val="{lvl}"/>')
    for sid in ("TableCaption", "ImageCaption"):
        xml = add_props(xml, sid, rpr='<w:color w:val="555555"/><w:sz w:val="19"/><w:szCs w:val="19"/>')
    xml = add_props(xml, "ImageCaption", ppr='<w:jc w:val="center"/>')
    for sid in ("CaptionedFigure", "Figure"):
        xml = add_props(xml, sid, ppr='<w:jc w:val="center"/>')
    return xml


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
        merged = polish(merged)
        with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in tz.infolist():
                data = merged.encode("utf-8") if item.filename == "word/styles.xml" else tz.read(item)
                zout.writestr(item, data)
    print(f"added {len(add)} styles -> {OUT}")


if __name__ == "__main__":
    main()
