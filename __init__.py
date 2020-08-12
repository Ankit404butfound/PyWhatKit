import time
import webbrowser as web
import pyautogui as pg
import wikipedia
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import platform
import os

last = time.time()
pg.FAILSAFE = False
sleeptm = "None, You can use this function to print the remaining time in seconds."
path = ""
headless_mode = True
curpth = os.getcwd()

class CountryCodeException(Exception):
    pass

class CallTimeException(Exception):
    pass

class InternetException(Exception):
    pass

class ChromedriverNotFound(Exception):
    pass

class FilePathException(Exception):
    pass

def watch_tutorial_in_Hindi():
    """Watch tutorial on how to use this library on YouTube in Hindi"""
    web.open("https://youtu.be/Fy7hmZ_YDjQ")
    #Previously, it was this video https://www.youtube.com/watch?v=3hUi0qfrWWo&t=3s
    
def watch_tutorial_in_English():
    """Watch tutorial on how to use this library on YouTube in English"""
    web.open("https://youtu.be/nAjbapi4Qk8")

def developer_contact():
    """Contach information of developer for feedbacks"""
    print("Message me on Telegram, username - Tag_kiya_kya\nOr email me at ankitrajjitendra816@gmail.com.")

def showHistory():
    """Prints the information of all last sent messages using this program"""
    file = open("pywhatkit_dbs.txt","r")
    content = file.read()
    file.close()
    if content == "--------------------":
        content = None
    print(content)

def add_driver_path(path):
    """Add path of of selenium driver
Warning! This will clear pywhatkit.history()"""
    try:
        driver = webdriver.Chrome(path)
        driver.quit()
        file = open("pywhatkit_dbs.txt","w")
        file.write("selpath : "+path+"\n")
        file.write("--------------------\n")
        file.close()
    except:
        raise ChromedriverNotFound("Driver not found at %s"%path)

def shutdown(time = 20):
    """Will shutdown the computer in given seconds
For Windows and Linux only"""
    global osname
    osname = platform.system()
    if "window" in osname.lower():
        cont = "shutdown -s -t %s"%time
        os.system(cont)

    elif "linux" in osname.lower():
        cont = "shutdown -h %s"%time
        os.system(cont)

    elif "darwin" in osname.lower():
        cont = "shutdown -h -t %s"%time
        os.system(cont)

    else:
        raise Warning("This function is for Windows, Mac and Linux users only, can't execute on %s"%osname)

def cancelShutdown():
    """Will cancel the scheduled shutdown"""
    if "window" in osname.lower():
        cont = "shutdown/a"
        os.system(cont)

    elif "linux" in osname.lower():
        cont = "shutdown -c"
        os.system(cont) 

    else:
        raise Warning("This function is for Windows and Linux only, can't execute on: %s"%osname)

def prnt_sleeptm():
    return sleeptm

def check_window():
    web.open("https://www.google.com")
    pg.alert("If the browser's window is not maximised\nMaximise and then close it if you want,\nor sendwhatmsg() function will not work","Pywhatkit")

def load_QRcode():
    """Will load the web whatsapp, you need to scan the QR code
This is one time only, session will be saved
***You must call pywhatkit.add_driver_path(path) before callig this function"""
    global curpth
    with open("pywhatkit_dbs.txt") as file:
        for lines in file:
            if "selpath" in lines:
                path = lines.replace("selpath : ","")
                path = path.strip()
    options = webdriver.ChromeOptions()
    pth = os.getcwd()+'./pywhatkit'
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")
    options.add_argument('--user-data-dir=%s/pywhatkit_data'%curpth)
    url = ("https://web.whatsapp.com")
    driver = webdriver.Chrome(path,options=options)
    driver.get(url)
    while True:
        try:
            driver.find_element_by_xpath('//div[@id="pane-side"]')
            print("Scanning complete!")
            print("Please close console window manually")
            break
        except:
            pass

def sendwhatmsg_with_selenium(phone_no, message, time_hour, time_min, print_messages=True):
    """Same as sendwhatmsg() function, but this will not open chrome
Most of the process will be hidden, only a console will open
***If this is the first time\nYou must call pywhatkit.load_QRcode() and pywhatkit.add_driver_path(path)\nbefore claing this function or you will get error
Make sure whatsapp web is not already opened or you might get your number banned"""
    global sleeptm, path, headless_mode, curpth
    if "+" not in phone_no:
        raise CountryCodeException("Country code missing from phone_no")
    timehr = time_hour

    with open("pywhatkit_dbs.txt") as file:
        for lines in file:
            if "selpath" in lines:
                path = lines.replace("selpath : ","")
    path = path.strip()

    if time_hour not in range(0,25) or time_min not in range(0,60):
        print("Invalid time format")

    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)+(time_min*60)
    
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm

    if lefttm < 60:
        raise CallTimeException("Call time must be greater than one minute as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s"%(curr.tm_mday,curr.tm_mon,curr.tm_year)
    time_write = "%s:%s"%(timehr,time_min)
    file = open("pywhatkit_dbs.txt","a")
    file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s"%(date,time_write,phone_no,message))
    file.write("\n--------------------\n")
    file.close()
    sleeptm = lefttm-60
    if print_messages:
        print(f"In {prnt_sleeptm()+60} seconds message will be delivered")
    time.sleep(sleeptm)
    
    options=webdriver.ChromeOptions()
    
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")
    options.add_argument('--user-data-dir=%s/pywhatkit_data'%curpth)
    if headless_mode:
        options.add_argument("--headless")
    driver = webdriver.Chrome(path,options=options)
    url = ('https://web.whatsapp.com/send?phone='+phone_no)
    driver.get(url)
    time.sleep(45)
    msg_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    time.sleep(14)
    msg_box.send_keys(message+"\n")
    if print_messages:
        print("Message sent\nYou may close the console window now")

def send_file(phone_no, path_to_file, time_hour, time_min, print_messages=True):
    """Send file of any format (png, mp3, txt etc)"""
    global sleeptm, path, headless_mode, curpth
    if "+" not in phone_no:
        raise CountryCodeException("Country code missing from phone_no")
    timehr = time_hour

    if not os.path.exists(path_to_file):
        raise FilePathException("No file found at %s"%path_to_file)

    with open("pywhatkit_dbs.txt") as file:
        for lines in file:
            if "selpath" in lines:
                chrpath = lines.replace("selpath : ","")
    chrpath = chrpath.strip()

    if time_hour not in range(0,25) or time_min not in range(0,60):
        print("Invalid time format")

    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)+(time_min*60)
    
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm

    if lefttm < 60:
        raise CallTimeException("Call time must be greater than one minute as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s"%(curr.tm_mday,curr.tm_mon,curr.tm_year)
    time_write = "%s:%s"%(timehr,time_min)
    file = open("pywhatkit_dbs.txt","a")
    file.write("Date: %s\nTime: %s\nPhone number: %s\nAttachment: %s"%(date,time_write,phone_no,path_to_file))
    file.write("\n--------------------\n")
    file.close()
    sleeptm = lefttm-60
    if print_messages:
        print(f"In {prnt_sleeptm()+60} seconds message will be delivered")
    time.sleep(sleeptm)
    options = webdriver.ChromeOptions()
    pth = os.getcwd()+'./pywhatkit'
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")
    options.add_argument('--user-data-dir=%s/pywhatkit_data'%curpth)
    if headless_mode:
        options.add_argument("--headless")
    url = ('https://web.whatsapp.com/send?phone='+phone_no)
    driver = webdriver.Chrome(chrpath,options=options)
    driver.get(url)
    time.sleep(40)
    driver.find_element_by_xpath('//span[@data-icon="clip"]').click()
    time.sleep(1)
    attch = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    attch.send_keys(path_to_file)
    time.sleep(10)
    snd = driver.find_element_by_xpath('//span[@data-icon="send"]')
    time.sleep(4)
    snd.click()
    if print_messages:
        print("Message sent\nIf it is a big file, it might take longer time to be delivered\nClose console only after message gets delivered.")

def sendwhatmsg(phone_no, message, time_hour, time_min, print_waitTime=True):
    '''Sends whatsapp message to a particulal number at given time
Phone number should be in string format not int
***This function will not work if the browser's window is minimised,
first check it by calling 'check_window()' function'''
    global sleeptm
    if "+" not in phone_no:
        raise CountryCodeException("Country code missing from phone_no")
    timehr = time_hour

    if time_hour not in range(0,25) or time_min not in range(0,60):
        print("Invalid time format")
    
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)+(time_min*60)
    
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm

    if lefttm < 60:
        raise CallTimeException("Call time must be greater than one minute as web.whatsapp.com takes some time to load")
    
    date = "%s:%s:%s"%(curr.tm_mday,curr.tm_mon,curr.tm_year)
    time_write = "%s:%s"%(timehr,time_min)
    file = open("pywhatkit_dbs.txt","a")
    file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s"%(date,time_write,phone_no,message))
    file.write("\n--------------------\n")
    file.close()
    sleeptm = lefttm-60
    if print_waitTime :
        print(f"In {prnt_sleeptm()} seconds web.whatsapp.com will open and after 60 seconds message will be delivered")
    time.sleep(sleeptm)
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
    time.sleep(2)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(58)
    pg.press('enter')
    
def info(topic,lines=3):
    '''Gives information on the topic'''
    spe = wikipedia.summary(topic, sentences = lines)
    print(spe)
    
def playonyt(topic):
    """Will play video on following topic, takes about 10 to 15 seconds to load"""
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        raise Exception("No video found.")
    
    #print("Videos found, opening most recent video")
    web.open("https://www.youtube.com"+lst[count-5])
    return "https://www.youtube.com"+lst[count-5]

def search(topic):
    '''Searches about the topic on Google'''
    link = 'https://www.google.com/search?q={}'.format(topic)
    web.open(link)

def help():
    """User manual of pywhatkit library"""
    print("""
SOME COMMON ERRORS and HOW TO FIX THEM:

1. CountryCodeException("Country code missing from phone_no")
-> To Fix this issue you need to add country code to the phone number, it satrts with "+".

2. CallTimeException("Call time must be greater than one minute as web.whatsapp.com takes some time to load")
-> Make sure the there is a difference of at least 60 seconds between current time and time you want to send message at.

3. Driver not found error
-> To fix this issue you need to download the driver of your respective browser.
-> You can download if from the given link : https://chromedriver.chromium.org/downloads
-> After downloading extract them and open the downloaded file and search for an application named chromedrive, copy its path,
   for windows, it should look like this - C:/Users/.../chromedriver.exe.
-> Call pywhatkit.add_driver_path(path) and pass the copied path as argument, if path is valid, a black window along with chrome will open and close.

NOTE : You must have Chrome browser installed, I will add support for other browsers soon.
""")

try : 
    requests.get("https://www.google.com")
    current = time.time()
    tyme = current-last
        
except Exception:
    raise InternetException("NO INTERNET - Pywhatkit needs active internet connection")

if tyme >= 5:
        raise Warning("INTERNET IS SLOW, extraction of information might take longer time")

try :
    file = open("pywhatkit_dbs.txt","r")
    file.close()

except:
    file = open("pywhatkit_dbs.txt","w")
    print("""Hello from the creator of pywhatkit, Ankit Raj Mahapatra.\nKindly do report bugs if any
What's new:
1. Fixed playonyt() function, now you no longer need chromedriver and this version is the fastest of all.
2. Added pywhatkit.help() for fixing some common errors.""")
    file.write("--------------------\n")
    file.close()
    file = None
    #Useless part, it increments a counter when someone downloads this library. 
##    num = int(requests.get("http://rajma.000webhostapp.com/manager1.php?action=read").text.split("-")[0])
##    nothing = requests.get(f"http://rajma.000webhostapp.com/manager1.php?action=write&data={num+1}-")
#end
