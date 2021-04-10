import webbrowser as web

baseurl = "https://pywhatkit.herokuapp.com/#"

def sendwhatmsg():
    web.open(f"{baseurl}sendwhatmsg")

def playonyt():
    web.open(f"{baseurl}playonyt")

def search():
    web.open(f"{baseurl}search")

def info():
    web.open(f"{baseurl}info")

def image_to_ascii_art():
    web.open(f"{baseurl}asciiart")

def text_to_handwriting():
    web.open(f"{baseurl}handwriting")
