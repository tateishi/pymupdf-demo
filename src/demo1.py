from msilib.schema import Directory
from pathlib import Path
import io
# import configparser


import fitz
from PIL import Image


from config import DIRECTORY

FILENAME = 'data1.pdf'
PATHNAME = DIRECTORY / FILENAME

doc = fitz.open(PATHNAME)

def extract_image_from_document(doc, xref):
    image_data = doc.extract_image(xref)
    image = Image.open(io.BytesIO(image_data['image']))
    return image.transpose(Image.Transpose.ROTATE_90)


for i, page in enumerate(doc):
    for j, (xref, *_) in enumerate(page.get_images()):
        image = extract_image_from_document(doc, xref)
        image.save(DIRECTORY / f'{PATHNAME.stem}-{i}-{j}.png')

doc.close()
