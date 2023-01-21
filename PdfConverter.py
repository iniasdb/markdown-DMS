from rinoh.backend import pdf
from rinoh.frontend.commonmark import CommonMarkReader
from rinoh.templates import Article
import os.path as path

class PdfConverter:
    
    def __init__(self, to_convert) -> None:
        self.to_convert = to_convert
        self.reader = CommonMarkReader()


    def convert(self):
        for file in self.to_convert:
            mdfilepath = path.join("./root/markdown", file)+".md"
            pdffilepath = path.join("./root/pdf", file)

            with open(mdfilepath, 'rb') as file:
                document_tree = self.reader.parse(file)
                document = Article(document_tree, backend=pdf)
                document.render(pdffilepath)