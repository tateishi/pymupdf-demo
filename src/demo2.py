from pathlib import Path

from pdfminer.high_level import extract_text

from config import DIRECTORY, FILENAME, ROTATE


def extract_text_from_document(directory, filename):
    directory = directory if isinstance(directory, Path) else Path(directory)
    filename = filename if isinstance(filename, Path) else Path(filename)
    pathname = directory / filename

    text = extract_text(pathname)
    return text


def main():
    text = extract_text_from_document(DIRECTORY, FILENAME)
    print(text)


if __name__ == '__main__':
    main()
