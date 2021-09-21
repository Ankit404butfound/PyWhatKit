import requests


def text_to_handwriting(
    string: str, save_to: str = "pywhatkit.png", rgb: tuple = (0, 0, 138)
) -> None:
    """Convert the given String to Handwritten Characters"""

    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s"
        % (string, rgb[0], rgb[1], rgb[2])
    ).content
    with open(save_to, "wb") as file:
        file.write(data)
        file.close()
