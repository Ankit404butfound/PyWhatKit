import os
import time
import pathlib
import pyperclip
from platform import system
from webbrowser import open
from urllib.parse import quote

import requests
from pyautogui import hotkey, press, click, size

from pywhatkit.core.exceptions import InternetException


WIDTH, HEIGHT = size()


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


def _web(receiver: str, message: str) -> None:
    """Opens WhatsApp Web based on the Receiver"""
    if check_number(number=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)


def send_message(message: str, receiver: str, wait_time: int) -> None:
    """Parses and Sends the Message"""

    _web(receiver=receiver, message=message)
    if not check_number(number=receiver):
        pyperclip.copy(message)
    time.sleep(wait_time)
    click(WIDTH / 2, HEIGHT / 2)
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")
    press("enter")


def copy_image(path: str) -> None:
    """Copy the Image to Clipboard based on the Platform"""

    if system().lower() == "linux":
        if pathlib.Path(path).suffix in (".PNG", ".png"):
            os.system(f"copyq copy image/png - < {path}")
        elif pathlib.Path(path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(f"copyq copy image/jpeg - < {path}")
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    elif system().lower() == "windows":
        import win32clipboard
        from io import BytesIO

        from PIL import Image

        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
    elif system().lower() == "darwin":
        if pathlib.Path(path).suffix in (".jpg", ".jpeg", ".JPG", ".JPEG"):
            os.system(
                f"osascript -e 'set the clipboard to (read (POSIX file \"{path}\") as JPEG picture)'"
            )
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    else:
        raise Exception(f"Unsupported System: {system().lower()}")


def send_image(path: str, caption: str, receiver: str, wait_time: int) -> None:
    """Sends the Image to a Contact or a Group based on the Receiver"""

    copy_image(path=path)
    _web(message=caption, receiver=receiver)

    time.sleep(wait_time)
    click(WIDTH / 2, HEIGHT / 2)
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")

    if not check_number(number=receiver):
        pyperclip.copy(caption)
        hotkey("ctrl", "v")
    press("enter")
