"""Fill the Word table-of-contents field with LibreOffice (headless) and save the .docx again.

Usage: python3 01_Report/assembly/update_toc.py <file.docx> [...]
Word still shows the same field; it simply arrives filled in, with page numbers.
"""
import subprocess
import sys
import time
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue


def prop(name, value):
    p = PropertyValue()
    p.Name, p.Value = name, value
    return p


def main() -> None:
    office = subprocess.Popen(["soffice", "--headless", "--norestore", "--nologo",
                               "--accept=socket,host=localhost,port=2002;urp;"],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        resolver = uno.getComponentContext().ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", uno.getComponentContext())
        for _ in range(60):
            try:
                ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
                break
            except Exception:
                time.sleep(0.5)
        desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        for f in sys.argv[1:]:
            url = Path(f).resolve().as_uri()
            doc = desktop.loadComponentFromURL(url, "_blank", 0, (prop("Hidden", True),))
            idx = doc.getDocumentIndexes()
            n = idx.getCount()
            for _ in range(2):  # second pass settles page numbers once the contents' length is known
                for i in range(n):
                    idx.getByIndex(i).update()
                doc.refresh()
            doc.storeToURL(url, (prop("FilterName", "MS Word 2007 XML"),))
            doc.close(True)
            print("updated", f, n, "index(es)")
    finally:
        office.terminate()


if __name__ == "__main__":
    main()
