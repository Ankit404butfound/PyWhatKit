import time
import webbrowser as web
import pyautogui as pg
import wikipedia
import requests
from bs4 import BeautifulSoup
import pyttsx3

eng = pyttsx3.init()
eng.setProperty("rate",115)
last = time.time()

def sendwhatmsg(phone_no, message, time_hour, time_min):
    '''Sends whatsapp message to a particulal number at given time'''
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
        raise Exception("Call time must be greater than one minute")

    else:
        sleeptm = lefttm-60
        time.sleep(sleeptm)
        web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
        time.sleep(60)
        pg.press('enter')

def info(topic,lines=3,speak=None):
    '''Gives information on the topic'''
    spe = wikipedia.summary(topic, sentences = lines)
    print(spe)
    if speak is not None:
        eng.say(spe)
        eng.runAndWait()
    
def playonyt(title):
    '''Opens YouTube video with following title'''
    url = 'https://www.youtube.com/results?q=' + title
    sc = requests.get(url)
    sctext = sc.text
    soup = BeautifulSoup(sctext,"html.parser")
    songs = soup.findAll("div",{"class":"yt-lockup-video"})
    song = songs[0].contents[0].contents[0].contents[0]
    songurl = song["href"]
    web.open("https://www.youtube.com"+songurl)

def search(topic):
    '''Searches about the topic on Google'''
    link = 'https://www.google.com/search?q={}'.format(topic)
    web.open(link)

try : 
    requests.get("https://www.google.com")
    current = time.time()
    tyme = current-last
        
except Exception:
    exc = ("NO INTERNET - Searcher needs active internet connection")
    raise Exception(exc)

if tyme >= 5:
        raise Warning("INTERNET IS SLOW, extraction of information might take longer time")
#Made by Ankit Raj Mahapatra ;-)
