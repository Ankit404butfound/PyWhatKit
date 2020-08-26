import re
import urllib.request
import string
import os
import cv2
import numpy as np
from PIL import Image

width = 50
height = 0
newwidth = 0
arr = string.ascii_letters
arr = arr + string.digits + "+,.-? "

def getimg(case,col):
    global width,height,back
    img = cv2.imread("ChrImages/%s.png"%case)
    img[np.where((img!=[255,255,255]).all(axis=2))] = col
    cv2.imwrite("ChrImages/chr.png",img)
    cases = Image.open("ChrImages/chr.png")
    back.paste(cases,(width,height))
    newwidth = cases.width
    width = width + newwidth

def download():
    """Downloads all images of handwritten characters,\nthey are written by the author of this library"""
    def down(char):
        url = "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/%s"%char
        imglink=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp,-1)
        cv2.imwrite(r"ChrImages\%s"%char,img)
        print(".",end="")
    try:
        getimg("zback")
        print("Images already downloaded!")
    except:
        print("Please wait! Downloading images...",end="")
        if not os.path.exists("ChrImages"):
            os.makedirs("ChrImages")
        for letter in arr:
            if letter == " ":
                letter = "zspace"
            if letter.isupper():
                letter = "c"+letter.lower()
            if letter == ",":
                letter = "coma"
            if letter == ".":
                letter = "fs"
            if letter == "?":
                letter = "que"
            try:
                down(letter+".png")
            except:
                down(letter+".PNG")
        down("zback.png")
        print("\nDownload Complete!")

def text_to_handwriting(string,rgb=[0,0,138]):
    """Convert the texts passed into handwritten characters"""
    try:
        global arr, width, height, back
        #rgb.reverse() not working, IDK why.
        back = Image.open("ChrImages\zback.png")
        rgb = [rgb[2],rgb[1],rgb[0]]
        count = -1
        lst = string.split()
        for letter in string:
            if width + 150 >= back.width or ord(letter) == 10:
                height = height + 227
                width = 50
            if letter in arr:
                if letter == " ":
                    count += 1
                    letter = "zspace"
                    wrdlen = len(lst[count+1])
                    if wrdlen*110 >= back.width-width:
                        width = 50
                        height = height+227
                    
                elif letter.isupper():
                    letter = "c"+letter.lower()
                elif letter == ",":
                    letter = "coma"
                elif letter == ".":
                    letter = "fs"
                elif letter == "?":
                    letter = "que"
                    
                getimg(letter,rgb)
                
        back.show()
        back.close()
        back = Image.open("ChrImages\zback.png")
        #rgb = [0,0,138]
        width = 50
        height = 0
        newwidth = 0
    except:
        print("Images not found")
        download()
        print("Now call the function again")

