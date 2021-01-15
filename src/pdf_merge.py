from __future__ import annotations

import os
from PyPDF2 import PdfFileMerger
import comtypes.client


class PdfMerge:
    pptx_code: int = 32
    docx_code: int = 17
    doc_code: int = 16
    _clear_pdfs: bool = False

    def __init__(self, dir_name: str = None):
        self.dir_name = self._validate_path(dir_name)

    def _validate_path(self, dir_name: str) -> str:
        if dir_name is None:
            return os.getcwd()
        if not os.path.isdir(dir_name):
            raise NotADirectoryError(f'Path {dir_name} is not a valid directory')
        return dir_name
        # return os.path.join(os.getcwd(), dir_name)

    def _doc_to_docx(self):
        pass

    def _choose_file_format(self):
        pass

    def to_pdf(self) -> PdfMerge:
        pptxs = [a for a in os.listdir(os.path.join(self.dir_name)) if a.endswith(".pptx")]
        docs = [a for a in os.listdir(os.path.join(self.dir_name)) if a.endswith(".doc")]
        if docs:
            self._doc_to_docx()
        docs = [a for a in os.listdir(os.path.join(self.dir_name)) if a.endswith(".docx")]

        if pptxs is None and docs is None:
            return self

        self._clear_pdfs = True
        file_format = self.docx_code if docs else self.pptx_code

        for doc in docs:
            out_file = os.path.join(self.dir_name, doc[:-5] + '.pdf')
            path = os.path.join(self.dir_name, doc)
            word = comtypes.client.CreateObject('Word.Application')

            file = word.Documents.Open(path)
            try:
                file.SaveAs(out_file, FileFormat=file_format)
            except Exception as e:
                print(e)
            finally:
                file.Close()
                word.Quit()

        return self

    def _convert_pptx(self):
        pass

    def merge(self) -> PdfMerge:
        pdfs = [a for a in os.listdir(os.path.join(self.dir_name)) if a.endswith(".pdf")]

        merger = PdfFileMerger()

        for pdf in pdfs:
            merger.append(os.path.join(self.dir_name, pdf), 'rb')

        with open(os.path.join(self.dir_name, 'merge.pdf'), "wb") as merged_pdf:
            merger.write(merged_pdf)

        merger.close()
        if self._clear_pdfs:
            for pdf in pdfs:
                os.remove(os.path.join(self.dir_name, pdf))

        return self
