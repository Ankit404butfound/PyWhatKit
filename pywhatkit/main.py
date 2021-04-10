import time
import webbrowser as web
import pyautogui as pg
import wikipedia
import requests
import os
import smtplib
from urllib.parse import quote
from .exceptions import *


last = time.time()
pg.FAILSAFE = False
sleeptm = "None, You can use this function to print the remaining time in seconds."
path = ""
curpth = os.getcwd()


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
    file = open("pywhatkit_dbs.txt","a",encoding='utf-8')
    file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s"%(date,time_write,phone_no,message))
    file.write("\n--------------------\n")
    file.close()
    sleeptm = lefttm-wait_time
    if print_waitTime :
        print(f"In {prnt_sleeptm()} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleeptm)
    parsedMessage = quote(message)
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
    time.sleep(2)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(wait_time-2)
    pg.press('enter')


def sendwhatmsg_to_group(group_id, message, time_hour, time_min, wait_time=20, print_waitTime=True):
    """Schedule message to be sent in a group
Group ID is something that is in its invite linek,
https://chat.whatsapp.com/AB123CDEFGHijklmn, here AB123CDEFGHijklmn is group ID"""
    if time_hour not in range(0,25) or time_min not in range(0,60):
        print("Invalid time format")

    timehr = time_hour
    
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
    file = open("pywhatkit_dbs.txt","a",encoding='utf-8')
    file.write("Date: %s\nTime: %s\nGroup_id: %s\nMessage: %s"%(date,time_write,group_id,message))
    file.write("\n--------------------\n")
    file.close()
    sleeptm = lefttm-wait_time
    if print_waitTime :
        print(f"In {sleeptm} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleeptm)
    web.open('https://web.whatsapp.com/accept?code='+group_id)
    time.sleep(2)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(wait_time-2)
    pg.typewrite(message+"\n")
    

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




'''  function to send message using email to any person  
      before using this function you have to enable less secure app in your email's privacy setting 
        my_mail = mail id of sender
        my_pass = password of sender
        mail_to = reciver's mail id
        content = message that you want to send
        ''' 
try:
    def sendMail(my_mail, my_pass, mail_to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(my_mail, my_pass) # eneter your email and password but you have to enable <less secure app> in your email privacy setting
        server.sendmail(my_mail, mail_to, content) # eneter your email, reciver email, content to send
        server.close()
except Exception as e:
    print("e")


def search(topic):
    '''Searches about the topic on Google'''
    link = 'https://www.google.com/search?q={}'.format(topic)
    web.open(link)



try : 
    requests.get("https://www.google.com")
    current = time.time()
    tyme = current-last
        
except Exception:
    raise InternetException("NO INTERNET - Pywhatkit needs active internet connection")

if tyme >= 5:
        raise Warning("INTERNET IS SLOW, extraction of information might take longer time")

try :
    file = open("pywhatkit_dbs.txt","r",encoding='utf-8')
    file.close()

except:
    file = open("pywhatkit_dbs.txt","w",encoding='utf-8')
    file.write("--------------------\n")
    file.close()
    file = None
