import time
import webbrowser as web
from datetime import datetime
from typing import List, Optional, Tuple, TypeVar, Union
from urllib.parse import quote

import pyautogui as pg

from pywhatkit.core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()

T = TypeVar("T")


def input_to_list(value_input: Union[T, List[T]]) -> List[T]:
    if type(value_input) is list:
        return value_input
    if type(value_input) is tuple:
        return [value_input]
    if type(value_input) is str:
        # Make sure that we don't convert it into a list of chars
        return [value_input]
    # For numbers, sets, etc, convert to a list
    return list(value_input)


def _log_message_sent(*, message: str, receiver: str) -> None:
    log.log_message(_time=time.localtime(), receiver=receiver, message=message)


def send_many_messages(*, messages: List[str], receiver: str, wait_time: int) -> None:
    for i, message in enumerate(messages):
        if i == 0:
            core.send_message(message, receiver, wait_time)
        else:
            core.send_another_message(
                message=message, receiver=receiver, wait_time=wait_time
            )
        _log_message_sent(receiver=receiver, message=message)


# Custom message type in case we want to create a new format later, like images that need a path and a caption
Message = str
MessageInput = Union[Message, List[Message]]


def sendwhatmsg_instantly(
    phone_no: str,
    messages: MessageInput,
    wait_time: int = 20,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""
    messages = input_to_list(messages)

    # Check once the phone number
    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country code missing from phone_no")

    send_many_messages(messages=messages, receiver=phone_no, wait_time=wait_time)
    if tab_close:
        core.close_tab(wait_time=close_time)


def _wait_until_time(*, target_time: Tuple[int, int], wait_time: int):
    "Waits until the given hour"
    time_hour, time_min = target_time
    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} seconds web.whatsapp.com will open and after {wait_time} seconds message will "
        f"be delivered!"
    )
    time.sleep(sleep_time)


def sendwhatmsg(
    phone_no: str,
    messages: MessageInput,
    time_hour: int,
    time_min: int,
    wait_time: int = 20,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Sends one or many WhatsApp Messages"""
    messages = input_to_list(messages)

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country code missing from Phone Number!")

    _wait_until_time(time=(time_hour, time_min), wait_time=wait_time)

    send_many_messages(messages=messages, receiver=phone_no, wait_time=wait_time)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group(
    group_id: str,
    messages: MessageInput,
    time_hour: Optional[int] = None,
    time_min: Optional[int] = None,
    wait_time: int = 20,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send one or more WhatsApp Messages to a Group.

    If an time is defined, this will wait for the correct time before sending the messages.
    """
    messages = input_to_list(messages)

    if time_hour is not None and time_min is not None:
        _wait_until_time(target_time=(time_hour, time_min), wait_time=wait_time)
    elif (time_hour is None) != (time_min is None):
        raise Exception(
            f"Invalid time: some elements are not defined {time_hour}h{time_min}"
        )

    send_many_messages(messages=messages, receiver=group_id, wait_time=wait_time)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhats_image(
    receiver: str,
    img_path: str,
    caption: str = " ",
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    sendwhats_image(receiver, [(img_path, caption)], wait_time, tab_close, close_time)


Image = Tuple[str, str]
ImageInput = Union[Image, List[Image]]


def sendwhats_images(
    receiver: str,
    images: ImageInput,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send one or more Images to a WhatsApp Contact"""
    images = input_to_list(images)

    if (
        not receiver.isalpha()
        and not receiver.isalnum()
        and not core.check_number(number=receiver)
    ):
        raise exceptions.CountryCodeException("Country Code missing from Phone Number!")

    for (img_path, caption) in images:
        current_time = time.localtime()
        core.send_image(
            path=img_path, caption=caption, receiver=receiver, wait_time=wait_time
        )
        log.log_image(
            _time=current_time, path=img_path, receiver=receiver, caption=caption
        )
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
