import os
import importlib

from src.config.configuration import Configuration
from src.source.source_type import SourceType


class ClassLoader:

    def __init__(self, config: Configuration):
        self.__config = config

    def load(self) -> SourceType:
        extension = self.load_extension()
        instance = None
        for e in extension:
            file_name = 'format_' + e[1:]
            file_path = os.path.join(os.getcwd(), 'src', 'source', file_name + '.py')
            if os.path.isfile(file_path):
                cls = getattr(importlib.import_module("src.source." + file_name),
                              self.get_class_by_file_extension(e[1:]))
                instance = cls(self.__config)
                self.__config.extension = e[1:]
                break
        if instance is None:
            raise FileNotFoundError(f'File was not loaded correctly')

        return instance

    def get_class_by_file_extension(self, file: str):
        return 'Format' + file.capitalize()

    def load_extension(self):
        extensions = []
        for file in os.listdir(os.path.join(self.__config.source)):
            e = os.path.splitext(file)[1]
            if e != "":
                extensions.append(e)
        return extensions
