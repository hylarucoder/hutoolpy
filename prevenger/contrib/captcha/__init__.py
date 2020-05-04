import uuid
import random

from PIL import ImageFilter
from captcha.image import ImageCaptcha, random_color


def random_text(length=4):
    return "".join(random.sample("0123456789", length))


def gen_id():
    return uuid.uuid4().hex


class CustomImageCaptcha(ImageCaptcha):
    def generate_image(self, chars):
        """Generate the image of the given characters.
        :param chars: text to be generated.
        """
        background = random_color(238, 255)
        color = random_color(10, 200, random.randint(220, 255))
        im = self.create_captcha_image(chars, color, background)
        im = im.filter(ImageFilter.SMOOTH)
        return im
