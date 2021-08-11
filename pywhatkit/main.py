import time
import os
import pathlib
from urllib.parse import quote
from typing import Union, Optional
from platform import system

import webbrowser as web
import pyautogui as pg
import wikipedia
import requests

from .exceptions import *

if system().lower() in ("windows", "darwin"):
    from PIL import ImageGrab


    def take_screenshot(file_name: str = 'pywhatkit_screenshot') -> None:
        """Take Screenshot, you can change the filename as per your Wish"""

        screen = ImageGrab.grab()
        screen.show(title=file_name)
        screen.save(f'{file_name}.png')
else:
    pass

last = time.time()
pg.FAILSAFE = False
sleep_time = "None, You can use this function to print the remaining time in seconds."
path = ""
current_path = os.getcwd()


def print_sleep_time() -> Union[str, int]:
    """Prints the sleep time"""

    return sleep_time


def check_window() -> None:
    """Check if the browser Window is maximized or not"""

    web.open("https://www.google.com")
    pg.alert("If the browser's window is not maximized,\nMaximise and then close it if you want,\nor send message "
             "functions will not work", "Pywhatkit")


def sendwhatmsg_instantly(phone_no: str, message: str, wait_time: int = 20,
                          tab_close: bool = False, close_time: int = 3) -> None:
    """Send WhatsApp Message Instantly"""

    if "+" not in phone_no:
        raise CountryCodeException("Country code missing from phone_no")

    parsed_message = quote(message)
    web.open('https://web.whatsapp.com/send?phone=' +
             phone_no + '&text=' + parsed_message)
    time.sleep(2)
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    time.sleep(wait_time - 2)
    pg.press('enter')
    if tab_close:
        close_tab(wait_time=close_time)


def sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 20,
                tab_close: bool = False, close_time: int = 3) -> None:
    """Sends a WhatsApp Message"""
    # Phone number should be given as a string
    # If the browser Window is not maximized this function won't work
    # Use check_window to check this

    global sleep_time
    if "+" not in phone_no:
        raise CountryCodeException("Country code missing from phone_no")
    timehr = time_hour

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format")

    if time_hour == 0:
        time_hour = 24
    call_sec = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + (current_minute * 60) + current_second
    left_time = call_sec - current_to_second

    if left_time <= 0:
        left_time = 86400 + left_time

    if left_time < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s" % (current_time.tm_mday, current_time.tm_mon, current_time.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    with open("pywhatkit_dbs.txt", "a", encoding='utf-8') as file:
        file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s" %
                   (date, time_write, phone_no, message))
        file.write("\n--------------------\n")
    sleep_time = left_time - wait_time
    print(
        f"In {print_sleep_time()} seconds web.whatsapp.com will open and after {wait_time} seconds message will "
        f"be delivered")
    time.sleep(sleep_time)
    parsed_message = quote(message)
    web.open('https://web.whatsapp.com/send?phone=' +
             phone_no + '&text=' + parsed_message)
    time.sleep(2)
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    time.sleep(wait_time - 2)
    pg.press('enter')
    if tab_close:
        close_tab(wait_time=close_time)


def sendwhatmsg_to_group(group_id: str, message: str, time_hour: int, time_min: int, wait_time: int = 20,
                         tab_close: bool = False, close_time: int = 3) -> None:
    """Send WhatsApp Message to a Group"""
    # Group ID is in the group's invite link
    # https://chat.whatsapp.com/AB123CDEFGHijklmn, here AB123CDEFGHijklmn is group ID

    if time_hour not in range(25) or time_min not in range(60):
        print("Invalid time format")

    timehr = time_hour

    if time_hour == 0:
        time_hour = 24
    call_second = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + (current_minute * 60) + current_second
    left_time = call_second - current_to_second

    if left_time <= 0:
        left_time = 86400 + left_time

    if left_time < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s" % (current_time.tm_mday, current_time.tm_mon, current_time.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    with open("pywhatkit_dbs.txt", "a", encoding='utf-8') as file:
        file.write("Date: %s\nTime: %s\nGroup_id: %s\nMessage: %s" %
                   (date, time_write, group_id, message))
        file.write("\n--------------------\n")
    sleep_time = left_time - wait_time
    print(f"In {sleep_time} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleep_time)
    web.open('https://web.whatsapp.com/accept?code=' + group_id)
    time.sleep(2)
    width, height = pg.size()
    time.sleep(wait_time - 2)
    pg.click(width / 2, height - height / 10)
    pg.typewrite(message + "\n")
    if tab_close:
        close_tab(wait_time=close_time)


def sendwhats_image(phone_no: str, img_path: str, caption: str = " ", wait_time: int = 15,
                    tab_close: bool = False, close_time: int = 3) -> None:
    """Send Image to a WhatsApp Contact"""

    if '+' not in phone_no:
        raise CountryCodeException("Please provide country code!")

    web.open('https://web.whatsapp.com/send?phone=' +
             phone_no + '&text=' + caption)
    time.sleep(5)
    if system().lower() == "linux":
        if pathlib.Path(img_path).suffix in (".PNG", ".png"):
            os.system(
                f"xclip -selection clipboard -target image/png -i {img_path}")
        elif pathlib.Path(img_path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(
                f"xclip -selection clipboard -target image/jpg -i {img_path}")
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
        image.convert('RGB').save(output, "BMP")
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
            os.system(f"osascript -e 'set the clipboard to (read (POSIX file \"{img_path}\") as JPEG picture)'")
        else:
            print(f"The file format {pathlib.Path(img_path).suffix} is not supported!")
            return
        time.sleep(2)
        pg.hotkey("command", "v")
    else:
        print(f"{system().lower()} not supported!")
        return
    time.sleep(wait_time)
    pg.press('enter')
    if tab_close:
        close_tab(wait_time=close_time)


def info(topic: str, lines: int = 3, return_value: bool = False) -> Optional[str]:
    """Gives information on the topic"""

    spe = wikipedia.summary(topic, sentences=lines)
    print(spe)
    if return_value:
        return spe


def close_tab(wait_time: int = 2) -> None:
    """Closes the Currently Opened Browser Tab"""

    time.sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        pg.hotkey("ctrl", "w")
    elif system().lower() in "darwin":
        pg.hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} not supported!")
    pg.press("enter")


def playonyt(topic: str, use_api: bool = False, open_video: bool = True) -> Union[str]:
    """Play a YouTube Video"""
    # use_api uses the pywhatkit playonyt API to get the url for the video
    # use the api only if the function is not working properly on its own

    if use_api:
        response = requests.get(
            f"https://pywhatkit.herokuapp.com/playonyt?topic={topic}")
        if open_video:
            web.open(response.content.decode('ascii'))
        return response.content.decode('ascii')
    else:
        url = 'https://www.youtube.com/results?q=' + topic
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count - 5] == "/results":
            raise Exception("No video found.")

        # print("Videos found, opening most recent video")
        if open_video:
            web.open("https://www.youtube.com" + lst[count - 5])
        return "https://www.youtube.com" + lst[count - 5]


def open_web() -> bool:
    """Opens WhatsApp Web"""

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True


def search(topic: str) -> None:
    """Searches about the topic on Google"""

    link = 'https://www.google.com/search?q={}'.format(topic)
    web.open(link)


try:
    requests.get("https://www.google.com")
    current = time.time()
    _time = current - last
except Exception:
    raise InternetException(
        "NO INTERNET - Pywhatkit needs active internet connection")

if _time >= 5:
    raise Warning(
        "INTERNET IS SLOW, extraction of information might take longer time")

try:
    file = open("pywhatkit_dbs.txt", "r", encoding='utf-8')
    file.close()
except FileNotFoundError:
    with open("pywhatkit_dbs.txt", "w", encoding="utf-8") as file:
        file.write("--------------------\n")
        file = None
