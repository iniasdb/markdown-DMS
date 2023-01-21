from DirIterator import DirIterator
from PdfConverter import PdfConverter

if __name__ == "__main__":
    rootdir = './root'
    mddir = "markdown"
    pdfdir = "pdf"

    it = DirIterator(rootdir, mddir, pdfdir)
    to_convert = it.get_to_convert()
    all_files = it.get_all_files()

    conv = PdfConverter()
    conv.convert(to_convert)
    conv.create_table_of_contents_pdf(all_files)