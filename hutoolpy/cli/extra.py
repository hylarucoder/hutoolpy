import base64

import typer

from hutoolpy.extra.captcha import CustomImageCaptcha
from hutoolpy.random import rand_letters_digits

group_extra = typer.Typer()


@group_extra.command(short_help="create wheezy captcha")
def captcha():
    chars = rand_letters_digits(5)
    image_data = CustomImageCaptcha().generate(chars)
    image_data_b64 = base64.b64encode(image_data.getvalue()).decode("utf-8")
    print(image_data_b64)
