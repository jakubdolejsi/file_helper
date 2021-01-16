from src.config.argument_parser import ArgumentParser
from src.pdf_merge import PdfMerge


def main():
    m = ArgumentParser().get_configuration_model()
    print(m.destination)
    exit()
    PdfMerge(dir_name='C:\\Users\\jakub\\Documents\\projects\\file_helper\\tests').to_pdf().merge()


if __name__ == '__main__':
    main()
