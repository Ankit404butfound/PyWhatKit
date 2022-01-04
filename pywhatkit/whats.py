import time
import webbrowser as web
from datetime import datetime
from typing import Optional
from urllib.parse import quote

import pyautogui as pg

from pywhatkit.core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()


def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 4)
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg(
    phone_no: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send a WhatsApp Message at a Certain Time"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=phone_no, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group(
    group_id: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group at a Certain Time"""

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group_instantly(
    group_id: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group Instantly"""

    current_time = time.localtime()

    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhats_image(
    receiver: str,
    img_path: str,
    caption: str = "",
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send Image to a WhatsApp Contact or Group at a Certain Time"""

    if (not receiver.isalnum()) and (not core.check_number(number=receiver)):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    current_time = time.localtime()
    core.send_image(
        path=img_path, caption=caption, receiver=receiver, wait_time=wait_time
    )
    log.log_image(_time=current_time, path=img_path, receiver=receiver, caption=caption)
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
