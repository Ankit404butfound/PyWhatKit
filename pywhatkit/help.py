import webbrowser as web

baseurl = "https://github.com/Ankit404butfound/PyWhatKit/wiki/"


def sendwhatmsg() -> None:
    """Open the Help Page for Sending WhatsApp Messages"""
    web.open(f"{baseurl}Sending-WhatsApp-Messages")


def misc_functions() -> None:
    """Playonyt, search, info, take_screenshot, show_history, open_web help page"""
    web.open(f"{baseurl}Miscellaneous-Functions")


def image_to_ascii_art() -> None:
    """Open the Help Page for image_to_ascii_art function"""
    web.open(f"{baseurl}ASCII-Art")


def text_to_handwriting() -> None:
    """Open the Help Page for text_to_handwriting function"""
    web.open(f"{baseurl}Text-to-Handwriting")


def exceptions() -> None:
    """Open the help page for the Exceptions within this library"""
    web.open(f"{baseurl}Exception")


def mail() -> None:
    """Open the help page for send_mail and send_hmail function"""
    web.open(f"{baseurl}Sending-a-Mail")


def shutdown() -> None:
    """Open the help page for shutdown and cancel_shutdown function"""
    web.open(f"{baseurl}Shutdown-and-CancelShutdown")
