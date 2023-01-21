from DirIterator import DirIterator
from PdfConverter import PdfConverter

if __name__ == "__main__":
    rootdir = './root'
    mddir = "markdown"
    pdfdir = "pdf"

    it = DirIterator(rootdir, mddir, pdfdir)
    list = it.get_to_convert()
    print(list)

    conv = PdfConverter(list)
    conv.convert()