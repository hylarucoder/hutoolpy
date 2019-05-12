"""
port from: https://bitbucket.org/akorn/wheezy.captcha

Copyright (C) 2011 by Andriy Kornatskyy

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import random

from PIL import Image
from PIL import ImageFilter
from PIL.ImageColor import getrgb
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype

T_SEQUENCE = tuple([t / 20.0 for t in range(21)])
beziers = {}


def pascal_row(n):
    """ Returns n-th row of Pascal's triangle
    """
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n // 2 + 1):
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
    if n & 1 == 0:
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result))
    return result


def make_bezier(n):
    """ Bezier curves:
        http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
    """
    try:
        return beziers[n]
    except KeyError:
        combinations = pascal_row(n - 1)
        result = []
        for t in T_SEQUENCE:
            tpowers = (t ** i for i in range(n))
            upowers = ((1 - t) ** i for i in range(n - 1, -1, -1))
            coefs = [c * a * b for c, a, b in zip(combinations, tpowers, upowers)]
            result.append(coefs)
        beziers[n] = result
        return result


def captcha(drawings, width=200, height=75):
    def render(text):
        image = Image.new("RGB", (width, height), (255, 255, 255))
        for drawing in drawings:
            image = drawing(image, text)
            assert image
        return image

    return render


# region: captcha drawers


def background(color="#EEEECC"):
    color = getrgb(color)

    def drawer(image, text):
        Draw(image).rectangle([(0, 0), image.size], fill=color)
        return image

    return drawer


def smooth_filter():
    def drawer(image, text):
        return image.filter(ImageFilter.SMOOTH)

    return drawer


def curve_filter(color="#5C87B2", width=4, number=6):
    if not callable(color):
        c = getrgb(color)

        def color():
            return c

    def drawer(image, text):
        dx, height = image.size
        dx = dx / number
        path = [(dx * i, random.randint(0, height)) for i in range(1, number)]
        bcoefs = make_bezier(number - 1)
        points = []
        for coefs in bcoefs:
            points.append(
                tuple(
                    sum([coef * p for coef, p in zip(coefs, ps)]) for ps in zip(*path)
                )
            )
        draw = Draw(image)
        draw.line(points, fill=color(), width=width)
        return image

    return drawer


def noise_filter(number=50, color="#EEEECC", level=2):
    if not callable(color):
        c = getrgb(color)

        def color():
            return c

    def drawer(image, text):
        width, height = image.size
        dx = width / 10
        width = width - dx
        dy = height / 10
        height = height - dy
        draw = Draw(image)
        for i in range(number):
            x = int(random.uniform(dx, width))
            y = int(random.uniform(dy, height))
            draw.line(((x, y), (x + level, y)), fill=color(), width=level)
        return image

    return drawer


def draw_chars(fonts, font_sizes=None, drawings=None, color="#5C87B2", squeeze_factor=0.8):
    fonts = tuple(
        [truetype(name, size) for name in fonts for size in font_sizes or (65, 70, 75)]
    )
    if not callable(color):
        c = getrgb(color)

        def color():
            return c

    def drawer(image, chars):
        draw = Draw(image)
        char_images = []
        for c in chars:
            font = random.choice(fonts)
            c_width, c_height = draw.textsize(c, font=font)
            char_image = Image.new("RGB", (c_width, c_height), (0, 0, 0))
            char_draw = Draw(char_image)
            char_draw.text((0, 0), c, font=font, fill=color())
            char_image = char_image.crop(char_image.getbbox())
            for drawing in drawings:
                char_image = drawing(char_image, c)
            char_images.append(char_image)
        width, height = image.size
        offset = int(
            (
                    width
                    - sum(int(i.size[0] * squeeze_factor) for i in char_images[:-1])
                    - char_images[-1].size[0]
            )
            / 2
        )
        for char_image in char_images:
            c_width, c_height = char_image.size
            mask = char_image.convert("L").point(lambda i: i * 1.97)
            image.paste(char_image, (offset, int((height - c_height) / 2)), mask)
            offset += int(c_width * squeeze_factor)
        return image

    return drawer


# region: text drawers


def warp_filter(dx_factor=0.27, dy_factor=0.21):
    def drawer(image, text):
        width, height = image.size
        dx = width * dx_factor
        dy = height * dy_factor
        x1 = int(random.uniform(-dx, dx))
        y1 = int(random.uniform(-dy, dy))
        x2 = int(random.uniform(-dx, dx))
        y2 = int(random.uniform(-dy, dy))
        image2 = Image.new(
            "RGB", (width + abs(x1) + abs(x2), height + abs(y1) + abs(y2))
        )
        image2.paste(image, (abs(x1), abs(y1)))
        width2, height2 = image2.size
        return image2.transform(
            (width, height),
            Image.QUAD,
            (x1, y1, -x1, height2 - y2, width2 + x2, height2 + y2, width2 - x2, -y1),
        )

    return drawer


def offset_filter(dx_factor=0.1, dy_factor=0.2):
    def drawer(image, text):
        width, height = image.size
        dx = int(random.random() * width * dx_factor)
        dy = int(random.random() * height * dy_factor)
        image2 = Image.new("RGB", (width + dx, height + dy))
        image2.paste(image, (dx, dy))
        return image2

    return drawer


def rotate_filter(angle=25):
    def drawer(image, text):
        return image.rotate(random.uniform(-angle, angle), Image.BILINEAR, expand=1)

    return drawer


def create_wheezy_captcha(chars, width: int = 200, height: int = 75) -> Image:
    default_font_path = os.path.dirname(os.path.dirname(__file__)) + "/assets/helvetica.ttf"
    captcha_image = captcha(
        drawings=[
            background(),
            draw_chars(
                fonts=[default_font_path],
                drawings=[warp_filter(), rotate_filter(), offset_filter()],
            ),
            curve_filter(),
            noise_filter(),
            smooth_filter(),
        ],
        width=width,
        height=height,
    )
    image = captcha_image(chars)
    return image
