import webbrowser as web

baseurl = "https://pywhatkit.herokuapp.com/#"


def sendwhatmsg() -> None:
    web.open(f"{baseurl}sendwhatmsg")


def playonyt() -> None:
    web.open(f"{baseurl}playonyt")


def search() -> None:
    web.open(f"{baseurl}search")


def info() -> None:
    web.open(f"{baseurl}info")


def image_to_ascii_art() -> None:
    web.open(f"{baseurl}asciiart")


def text_to_handwriting() -> None:
    web.open(f"{baseurl}handwriting")
