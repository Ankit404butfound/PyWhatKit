import time
from platform import system
from webbrowser import open
from urllib.parse import quote
import pyperclip 
"""
import pyperclip pyperclip is an in-built module in python for copying text
we will use it for issue #111 as they are saying that accent and pyautugui only
supports english https://github.com/Ankit404butfound/PyWhatKit/issues/111 this is the full link
"""
import requests
from pyautogui import hotkey, alert, typewrite, press, size, click

from pywhatkit.core.exceptions import InternetException


def check_number(number: str) -> bool:
    """Checks the Number to see if contains the Country Code"""

    return "+" in number or "_" in number


def close_tab(wait_time: int = 2) -> None:
    """Closes the Currently Opened Browser Tab"""

    time.sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif system().lower() in "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} not supported!")
    press("enter")


def check_connection() -> None:
    """Check the Internet connection of the Host Machine"""

    try:
        requests.get("https://google.com")
    except requests.RequestException:
        raise InternetException(
            f"Error while connecting to the Internet. Make sure you are connected to the Internet!"
        )


def check_window() -> None:
    """Check if the browser Window is maximized or not"""

    open("https://www.google.com")
    alert(
        "If the browser's window is not maximized,\nMaximise and then close it if you want,\nor send message "
        "functions will not work",
        "Pywhatkit",
    )


def send_message(message: str, receiver: str, wait_time: int) -> None:
    """Parses and Sends the Message"""

    if check_number(receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)

    if not check_number(receiver):
        # typewrite(message) I removed this line because we do not need this anymore
        pyperclip.copy(message) # copy the message
        hotkey("ctrl", 'v') # paste the message with accent
        # and done
    time.sleep(wait_time)
    press("enter")
