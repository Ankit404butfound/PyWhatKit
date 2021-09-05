import time
import os
import pathlib
from datetime import datetime
from urllib.parse import quote
from platform import system
from typing import Optional

import webbrowser as web
import pyautogui as pg

from pywhatkit.core import log, core, exceptions

pg.FAILSAFE = False

core.check_connection()


def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 20,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country code missing from phone_no")

    web.open(
        "https://web.whatsapp.com/send?phone=" + phone_no + "&text=" + quote(message)
    )
    time.sleep(wait_time)
    pg.press("enter")
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg(
    phone_no: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 20,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Sends a WhatsApp Message"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country code missing from Phone Number!")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}", "%H:%M"
    ) - datetime.strptime(f"{current_time.tm_hour}:{current_time.tm_min}", "%H:%M")

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} seconds web.whatsapp.com will open and after {wait_time} seconds message will "
        f"be delivered"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=phone_no, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group(
    group_id: str,
    message: str,
    time_hour: Optional[int] = None,
    time_min: Optional[int] = None,
    wait_time: int = 20,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group"""

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid time format")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}", "%H:%M"
    ) - datetime.strptime(f"{current_time.tm_hour}:{current_time.tm_min}", "%H:%M")

    if left_time.total_seconds() < wait_time:
        raise exceptions.CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load"
        )

    sleep_time = left_time.total_seconds() - wait_time
    print(
        f"In {sleep_time} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhats_image(
    phone_no: str,
    img_path: str,
    caption: str = " ",
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send Image to a WhatsApp Contact"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code missing from Phone Number!")

    web.open("https://web.whatsapp.com/send?phone=" + phone_no + "&text=" + caption)
    time.sleep(5)
    if system().lower() == "linux":
        if pathlib.Path(img_path).suffix in (".PNG", ".png"):
            os.system(f"xclip -selection clipboard -target image/png -i {img_path}")
        elif pathlib.Path(img_path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(f"xclip -selection clipboard -target image/jpg -i {img_path}")
        else:
            print(f"The file format {pathlib.Path(img_path).suffix} is not supported!")
            return
        time.sleep(2)
        pg.hotkey("ctrl", "v")
    elif system().lower() == "windows":
        import win32clipboard
        from io import BytesIO

        from PIL import Image

        image = Image.open(img_path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        time.sleep(2)
        pg.hotkey("ctrl", "v")
    elif system().lower() == "darwin":
        if pathlib.Path(img_path).suffix in (".jpg", ".jpeg", ".JPG", ".JPEG"):
            width, height = pg.size()
            pg.click(width / 2, height / 2)
            os.system(
                f"osascript -e 'set the clipboard to (read (POSIX file \"{img_path}\") as JPEG picture)'"
            )
        else:
            print(f"The file format {pathlib.Path(img_path).suffix} is not supported!")
            return
        time.sleep(2)
        pg.hotkey("command", "v")
    else:
        print(f"{system().lower()} not supported!")
        return
    time.sleep(wait_time)
    pg.press("enter")
    if tab_close:
        core.close_tab(wait_time=close_time)


def open_web() -> bool:
    """Opens WhatsApp Web"""

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True
