import qrcode
from qrcode.image.pure import PymagingImage


def make_qrcode(text):
    return qrcode.make(text, image_factory=PymagingImage)
