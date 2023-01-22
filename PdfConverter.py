from rinoh.backend import pdf
from rinoh.frontend.commonmark import CommonMarkReader
from rinoh.templates import Article
from rinoh.document import DocumentTree
from rinoh.styleds import *

import os.path as path
from pathlib import Path as pathlib

class PdfConverter:
    
    def __init__(self) -> None:
        self.reader = CommonMarkReader()

    def create_table_of_contents_pdf(self, all_files):
        self.create_toc_md_file(all_files)

        with open("./root/markdown/toc.md", 'rb') as file:
            document_tree = self.reader.parse(file)

        document = Article(document_tree, backend=pdf)
        document.render("./root/pdf/toc")
    
    def create_toc_md_file(self, all_files):
        with open("./root/markdown/toc.md", "w+") as f:
            lastdir = ""
            for file in all_files:
                parts = pathlib(file).parts
                parts_list = list(parts)

                parts_list[1] = "pdf"
                parts_pdf = tuple(parts_list)
                file_pdf = pathlib(*parts_pdf)

                parts_list.pop(0)
                parts_list.pop(0)
                filename = parts_list[-1]
                parts = tuple(parts_list)
                
                dir = path.split(pathlib(*parts))[0]

                if not dir == lastdir:
                    level = "#"*(len(parts)-1)
                    f.write("\r\n"+level+" "+dir+" "+level)
                lastdir = dir

                f.write("\r\n**"+filename+"**")

                summary = self.get_summary(file)

                f.write("\r\n"+summary)
            f.close()

    def get_summary(self, file) -> str:
        summary = ""
        
        with open(file, "r", encoding="utf-8") as f:
            content = f.read().split("\n")
        
        if content[0].lower() == "# summary #":
            for line in content:
                if line.lower() == "# summary #":
                    continue
                if "<endsummary>" in line:
                    break
                else:
                    summary+= line
        else:
            summary = "No summary for this document."

        return summary

    def convert(self, to_convert):
        for file in to_convert:
            parts = pathlib(file).parts
            parts_list = list(parts)
            parts_list[1] = "pdf"
            parts = tuple(parts_list)

            pdffilepath = pathlib(*parts)

            with open(file, 'rb') as file:
                document_tree = self.reader.parse(file)
                document = Article(document_tree, backend=pdf)
                document.render(pdffilepath)