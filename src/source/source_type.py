import os

from PyPDF2 import PdfFileMerger

from src.config.configuration import Configuration
from src.destination.destination_type import DestinationType


class SourceType:

    def __init__(self, config: Configuration):
        self.config = config
        self.type_name = None

    def register_this_type(self, name):
        pass

    def _validate_paths(self):
        pass

    def convert_to(self, dest_format: DestinationType):
        return self

    def merge(self):
        pdfs = [a for a in os.listdir(os.path.join(self.config.source)) if a.endswith(".pdf")]

        merger = PdfFileMerger()


        for pdf in pdfs:
            merger.append(os.path.join(self.config.source, pdf), 'rb')

        with open(os.path.join(self.config.destination, 'merge.pdf'), "wb") as merged_pdf:
            merger.write(merged_pdf)

        merger.close()
        for pdf in pdfs:
            os.remove(os.path.join(self.config.destination, pdf))

        return self

    def load_source_files(self):
        return [f for f in os.listdir(os.path.join(self.config.source)) if f.endswith('.' + self.config.extension)]
