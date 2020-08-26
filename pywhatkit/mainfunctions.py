import time
import webbrowser as web
import pyautogui as pg
import wikipedia
import requests
from bs4 import BeautifulSoup
import platform
import os
from PIL import Image

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

def sendwhatmsg(phone_no, message, time_hour, time_min, wait_time=20, print_waitTime=True):
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

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm

    if lefttm < wait_time:
        raise CallTimeException("Call time must be greater than wait_time as web.whatsapp.com takes some time to load")
    
    date = "%s:%s:%s"%(curr.tm_mday,curr.tm_mon,curr.tm_year)
    time_write = "%s:%s"%(timehr,time_min)
    file = open("pywhatkit_dbs.txt","a")
    file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s"%(date,time_write,phone_no,message))
    file.write("\n--------------------\n")
    file.close()
    sleeptm = lefttm-wait_time
    if print_waitTime :
        print(f"In {prnt_sleeptm()} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleeptm)
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
    time.sleep(2)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(wait_time-2)
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

def image_to_ascii_art(imgpath,output_file="pywhatkit_asciiart.txt"):
    """Converts the given image to ascii art and save it to uotput_file"""
    # pass the image as command line argument
    image_path = imgpath
    img = Image.open(image_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    # new size of image
    # print(img.size)

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["*","S","#","&","@","$","%","*","!",":","."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    # write to a text file.
    with open(output_file, "w") as f:
        f.write(ascii_image)
    return ascii_image

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

2. CallTimeException("Call time must be greater than wait time as web.whatsapp.com takes some time to load")
-> Make sure the there is a difference of at least <wait time> seconds between current time and time you want to send message at.

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
1. Removed selenium dependent functions
2. Added pywhatkit.text_to_handwriting() which will convert text to handwritten characters.
3. Added pywhatkit.image_to_ascii_art() which will convert image to ascii art.""")
    file.write("--------------------\n")
    file.close()
    file = None
    #Useless part, it increments a counter when someone downloads this library. 
##    num = int(requests.get("http://rajma.000webhostapp.com/manager1.php?action=read").text.split("-")[0])
##    nothing = requests.get(f"http://rajma.000webhostapp.com/manager1.php?action=write&data={num+1}-")
#end
