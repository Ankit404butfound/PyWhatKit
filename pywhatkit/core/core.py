import time
import pyperclip
from platform import system
from webbrowser import open
from urllib.parse import quote

import requests
from pyautogui import hotkey, alert, press, click, size

from pywhatkit.core.exceptions import InternetException


def check_number(number: str) -> bool:
    """Checks the Number to see if contains the Country Code"""

    return "+" in number or "_" in number


def close_tab(wait_time: int = 2) -> None:
    """Closes the Currently Opened Browser Tab"""

    time.sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif system().lower() == "darwin":
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
        pyperclip.copy(message)
    width, height = size()
    time.sleep(wait_time)
    click(width / 2, height / 2)
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")
    press("enter")
