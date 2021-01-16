from __future__ import annotations
import os
from argparse import Namespace


class Configuration(object):

    def __init__(self, args: Namespace):
        self.__source = args.source
        self.__destination = args.destination

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    def validate(self) -> Configuration:
        if self.__source is None:
            self.default_source()
        if self.__destination is None:
            self.default_destination()

        if not os.path.isdir(self.__source):
            raise NotADirectoryError(f'Source path {self.__source} is not a valid path')
        if not os.path.isdir(self.__destination):
            raise NotADirectoryError(f'Destination path {self.__destination} is not a valid path')
        return self

    def default_source(self):
        self.__source = os.getcwd()

    def default_destination(self):
        self.__destination = os.getcwd()
