from src.config.argument_parser import ArgumentParser
from src.config.class_loader import ClassLoader
from src.destination.format_pdf import FormatPdf
from src.pdf_merge import PdfMerge


def main():
    config = ArgumentParser().get_configuration_model()

    source = ClassLoader(config).load()
    source.convert_to(dest_format=FormatPdf())
    source.merge()


if __name__ == '__main__':
    main()
