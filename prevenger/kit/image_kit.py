import base64
import os
import sys
from PIL import Image


def data_uri_encode():
    raise NotImplementedError


def data_uri_decode():
    raise NotImplementedError


def b64_encode(s: str) -> str:
    return base64.b64encode(s)


def b64_decode(s: str) -> str:
    return base64.b64decode(s)


def save_as_jpg(infile, outfile):
    try:
        Image.open(infile).save(outfile)
    except IOError:
        print("cannot convert", infile)


def save_thumbnail(infile, outfile):
    size = (128, 128)
    try:
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(outfile, "JPEG")
    except IOError:
        print("cannot create thumbnail for", infile)


def create_qrcode(content, width):
    pass
