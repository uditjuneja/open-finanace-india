import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
import pytesseract

from .config import CHAR_SET


def basic_captcha(url, headers=None, CHAR_SET=CHAR_SET):
    response = requests.get(url, headers=headers)
    im = Image.open(BytesIO(response.content))

    captcha = pytesseract.image_to_string(im)

    s = ""
    for i in captcha:
        if i in CHAR_SET:
            s += i
    if s:
        im.save(f"{s}.png")
    return s
