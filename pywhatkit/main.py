import time
import webbrowser as web
import pyautogui as pg
import wikipedia
import requests
import os
import smtplib
from urllib.parse import quote
from .exceptions import *
from PIL import ImageGrab

last = time.time()
pg.FAILSAFE = False
sleep_time = "None, You can use this function to print the remaining time in seconds."
path = ""
current_path = os.getcwd()


class print_execution_time:
    """it returns the execution time of your code.example:-
    timer = print_execution_time()
    timer.start()
    #your code
    timer.end_timer()
    print(timer.return_exe_time())"""

    def start_timer(self):
        global start
        start = time.time()

    def end_timer(self):
        global end
        end = time.time()

    def return_exe_time(self):
        return end - start


def print_sleep_time() -> str:
    return sleep_time


def takescreenshot(file_name='pywhatkit_screenshot'):
    screen = ImageGrab.grab()
    screen.show()
    screen.save(f'{file_name}.png')


def check_window() -> None:
    web.open("https://www.google.com")
    pg.alert("If the browser's window is not maximised,\nMaximise and then close it if you want,\nor sendwhatmsg() "
             "function will not work", "Pywhatkit")


def sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 20,
                print_wait_time: bool = True, browser: str = None) -> None:
    # Sends a message at a specific time
    # Phone number should be given as a string
    # If the browser Window is not maximized this function won't work
    # Use check_window to check this

    if browser.lower() not in ["chrome", "firefox", "brave", "opera"]:
        raise InvalidBrowserName(
            "Browser name can be firefox, chrome, brave, opera")

    global sleep_time
    if "+" not in phone_no:
        raise CountryCodeException("Country code missing from phone_no")
    timehr = time_hour

    if time_hour not in range(0, 25) or time_min not in range(0, 60):
        print("Invalid time format")

    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour * 3600) + (time_min * 60)

    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr * 3600) + (currmin * 60) + (currsec)
    lefttm = callsec - currtotsec

    if lefttm <= 0:
        lefttm = 86400 + lefttm

    if lefttm < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s" % (curr.tm_mday, curr.tm_mon, curr.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    file = open("pywhatkit_dbs.txt", "a", encoding='utf-8')
    file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s" %
               (date, time_write, phone_no, message))
    file.write("\n--------------------\n")
    file.close()
    sleep_time = lefttm - wait_time
    if print_wait_time:
        print(
            f"In {print_sleep_time()} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleep_time)
    parsedMessage = quote(message)
    web.open('https://web.whatsapp.com/send?phone=' +
             phone_no + '&text=' + parsedMessage)
    time.sleep(2)
    width, height = pg.size()
    if browser:
        whats = pg.getWindowsWithTitle(browser)[0]
        whats.maximize()
        whats.activate()
    pg.click(width / 2, height / 2)
    time.sleep(wait_time - 2)
    pg.press('enter')


def sendwhatmsg_to_group(group_id: str, message: str, time_hour: int, time_min: int, wait_time: int = 20,
                         print_wait_time: bool = True) -> None:
    # Group ID is in the group's invite link
    # https://chat.whatsapp.com/AB123CDEFGHijklmn, here AB123CDEFGHijklmn is group ID
    if time_hour not in range(0, 25) or time_min not in range(0, 60):
        print("Invalid time format")

    timehr = time_hour

    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour * 3600) + (time_min * 60)

    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr * 3600) + (currmin * 60) + (currsec)
    lefttm = callsec - currtotsec

    if lefttm <= 0:
        lefttm = 86400 + lefttm

    if lefttm < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s" % (curr.tm_mday, curr.tm_mon, curr.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    file = open("pywhatkit_dbs.txt", "a", encoding='utf-8')
    file.write("Date: %s\nTime: %s\nGroup_id: %s\nMessage: %s" %
               (date, time_write, group_id, message))
    file.write("\n--------------------\n")
    file.close()
    sleeptm = lefttm - wait_time
    if print_wait_time:
        print(
            f"In {sleeptm} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleeptm)
    web.open('https://web.whatsapp.com/accept?code=' + group_id)
    time.sleep(2)
    width, height = pg.size()
    whats = pg.getWindowsWithTitle("WhatsApp")[0]
    whats.maximize()
    whats.activate()
    time.sleep(wait_time - 2)
    pg.click(width / 2, height - height / 10)
    pg.typewrite(message + "\n")


def info(topic: str, lines: int = 3) -> None:
    # Gives information on the topic
    spe = wikipedia.summary(topic, sentences=lines)
    print(spe)


def playonyt(topic: str, use_api: bool = False) -> str:
    # use_api uses the pywhatkit playonyt API to get the url for the video
    # Only to be used if the function is not working properly on its own

    if use_api is True:
        response = requests.get(
            f"https://mypywhatkit.herokuapp.com/playonyt?topic={topic}")
        web.open(response.content.decode('ascii'))
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
        web.open("https://www.youtube.com" + lst[count - 5])
        return "https://www.youtube.com" + lst[count - 5]


def search(topic: str) -> None:
    """Searches about the topic on Google"""
    link = 'https://www.google.com/search?q={}'.format(topic)
    web.open(link)


try:
    requests.get("https://www.google.com")
    current = time.time()
    tyme = current - last
except Exception:
    raise InternetException(
        "NO INTERNET - Pywhatkit needs active internet connection")

if tyme >= 5:
    raise Warning(
        "INTERNET IS SLOW, extraction of information might take longer time")


try:
    file = open("pywhatkit_dbs.txt", "r", encoding='utf-8')
    file.close()
except FileNotFoundError:
    file = open("pywhatkit_dbs.txt", "w", encoding='utf-8')
    file.write("--------------------\n")
    file.close()
    file = None
