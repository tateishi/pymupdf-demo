from msilib.schema import Directory
from pathlib import Path
import io


import fitz
from PIL import Image


from config import DIRECTORY, FILENAME, ROTATE


def extract_image_from_document(doc, xref, rotate=False):
    image_data = doc.extract_image(xref)
    with Image.open(io.BytesIO(image_data['image'])) as image:
        image.load()
        if rotate:
            image = image.transpose(Image.Transpose.ROTATE_90)
        return image


def save_image_from_document(directory, filename, rotate=False):
    directory = directory if isinstance(directory, Path) else Path(directory)
    filename = filename if isinstance(filename, Path) else Path(filename)
    pathname = directory / filename

    with fitz.open(pathname) as doc:
        for i, page in enumerate(doc, start=1):
            for j, (xref, *_) in enumerate(page.get_images(), start=1):
                image = extract_image_from_document(doc, xref, rotate=rotate)
                image.save(directory / f'{pathname.stem}-{i}-{j}.png')


def main():
    save_image_from_document(DIRECTORY, FILENAME, ROTATE)


if __name__ == '__main__':
    main()
