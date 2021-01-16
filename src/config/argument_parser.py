import argparse

from src.config.configuration import Configuration


class ArgumentParser:

    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__parse()

    def __parse(self) -> None:
        self.__parser.add_argument("-s", "--source", required=False, type=str, help="Directory path of source files")
        self.__parser.add_argument("-v", "--destination", required=False, type=str, help="Destination folder for "
                                                                                         "merged files")

    def get_configuration_model(self) -> Configuration:
        args = self.__parser.parse_args()
        config = Configuration(args).validate()
        return config
