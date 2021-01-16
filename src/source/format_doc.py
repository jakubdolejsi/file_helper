from __future__ import annotations
from src.destination.destination_type import DestinationType
from src.source.source_type import SourceType

import os
import comtypes.client


class FormatDoc(SourceType):

    code: int = 17

    def register_this_type(self, name):
        self.type_name = name

    def convert_to(self, dest_format: DestinationType) -> FormatDoc:
        docs = self.load_source_files()
        print(f'docs: {docs}')

        for doc in docs:
            out_file = os.path.join(self.config.source, doc[:-4] + '.pdf')
            source_file = os.path.join(self.config.source, doc)
            word = comtypes.client.CreateObject('Word.Application')

            file = word.Documents.Open(source_file)
            try:
                file.SaveAs(out_file, FileFormat=self.code)
            except Exception as e:
                print(e)
            finally:
                file.Close()
                word.Quit()

        return self

    def get_out_file(self, f):
        pass

