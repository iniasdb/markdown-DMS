import os
import os.path as path

class DirIterator:

    def __init__(self, rootdir, mddir, pdfdir) -> None:
        self._rootdir = rootdir
        self._mddir = mddir
        self._pdfdir = pdfdir
    
    def get_to_convert(self) -> list:
        pdf_dir_list = []
        pdf_file_list = []
        md_to_convert = []

        # Loop pdf dir
        for root, dirs, files in os.walk(path.join(self._rootdir, self._pdfdir)):
            for dir in dirs:
                pdf_dir_list.append(dir)
            for file in files:
                filepath = path.join(path.basename(path.normpath(root)), file)
                pdf_file_list.append(path.splitext(filepath)[0])

        # Loop md dir
        for root, dirs, files in os.walk(path.join(self._rootdir, self._mddir)):
            for dir in dirs:
                # If subdir of markdown dir is not present in pdf dir
                # Create subdir in pdf dir
                if not dir in pdf_dir_list:
                    os.mkdir(path.join(self._rootdir, self._pdfdir, dir))
            for file in files:
                name = path.splitext(path.join(path.basename(path.normpath(root)), file))[0]
                if not name in pdf_file_list:
                    md_to_convert.append(name)
        
        return md_to_convert