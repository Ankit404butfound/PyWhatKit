import requests
from typing import NoReturn


def text_to_handwriting(string: str, save_to: str = "pywhatkit.png", rgb: list = (0, 0, 138)) -> NoReturn:
    """Convert the given str to handwriting"""
    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (string, rgb[0], rgb[1], rgb[2])).content
    file = open(save_to, "wb")
    file.write(data)
    file.close()
