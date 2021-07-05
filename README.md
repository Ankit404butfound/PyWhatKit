
# ![logo](https://github.com/Ankit404butfound/PyWhatKit/raw/master/Images/logo.png?raw=true)

[PyWhatKit](https://pypi.org/project/pywhatkit/) is a Python library with various helpful features. It is an easy to use library which does not requires you to do some additional setup.

# Links

- ## Join our discord server - <https://discord.gg/uwznv4jKgk>

- ## Help us test an upcoming feature - [Here](https://pywhatkit.herokuapp.com/remote-kit)

- ## Detailed documentation - [Wiki](https://github.com/Ankit404butfound/PyWhatKit/wiki)

# Installation

This library can be installed by the pip command, open your command prompt and type in the following command...

`pip3 install pywhatkit`

# Functions of this library

First import the library using the command `import pywhatkit as kit` and then proceed to call the functions:
## **kit.sendwhats_image(...)**

This function can be used to send Image or Gif or videos to anyone
![image](https://user-images.githubusercontent.com/54436840/124421022-38977580-dd7e-11eb-87cd-df34811d016e.png)
### The parameters are

**phone\_num** (required) - Phone number of target with country code
**image\_path** (required) - Path to image or gif or video
**caption** (required) - The text that should appear below images
**phone\_num** (required) - Phone number of target with country code
**wait\_time** (optional, val = 20) - Seconds after which the message will be sent after opening the web


## **kit.sendwhatmsg(...)**

This function can be used to send WhatsApp message at certain time, **kit.sendwhatmsg_instantly(...)** can be used to send message instantly while **kit.sendwhatmsg_to_group(...)** can be used to send message to group.

![SendWhatMsg](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/sendwhatmsg.png)  

### The parameters are

**phone\_num** (required) - Phone number of target with country code  
**message** (required) - Message that you want to sendwhatmsg  
**time\_hour** (required) - Hours at which you want to send message in 24 hour format  
**time\_min** (required) - Minutes at which you want to send message  
**wait\_time** (optional, val = 20) - Seconds after which the message will be sent after opening the web  
**print\_wait_time** (optional, val = True) - Will print the remaining time if set to true  
**tab_close** (optional, val = False) - True if you want to close the tab after sending the message

### Some common errors

**CountryCodeException** - Check if the phone number passed into the parameter has [country code](https://en.wikipedia.org/wiki/List_of_country_calling_codes)  
**Message not getting delivered** - Check internet speed and increase wait\_time to 30 or above  
**CallTimeException** - The web takes some time to load so some delay is required, make sure the seconds left is greater than the wait\_time  
**SyntaxError** - Make sure the first two parameters are string and the rest are int

## **kit.playonyt(...)**

This function can be used to search and play a particular video on YouTube by using just the keyword, like "Shape of You song".  

![PlayonYT](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/playonyt.png)  

### The parameters are

**topic** (required) - Topic or title that is related to the video.  
**use_api** (optional, val = False) - Use web-API instead.  
**open_video** (optional, val = True) - Opens video in your browser if set to True.  

#### Some common errors

**Video not opening** - Make sure the topic exists or you have provided proper spelling, **set use_api to True**.

## **kit.search(...)**

This function can be used to make a google search for any term.  

![Search Google](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/search.PNG)

### The parameters are

**topic** (required) - Topic or title that you want to search

## **kit.info(...)**

This function can be used to fetch information about any topic.  

![Wikipedia](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/info.PNG)

### The parameters are

**topic** (required) - Topic or title that you want to get information about  
**lines** (optional, val = 3) - Number of lines that you want to print about it  
**return_value** (optional, val = False) - True if you want to return the result

#### Some common errors

**Not returning paragraph** - Make sure the topic exists and you are providing specific title

## **kit.image\_to\_ascii\_art(...)**

This function can be used to convert any image to ASCII art.  

![ASCII Art](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/asciiart.PNG)

### The parameters are

**imgpath** (required) - Path to the image that you want to convert  
**output\_file** (optional, val = "pywhatkit\_asciiart.txt") - File where you want to save the output characters

#### Some common errors

**File not found** - Make sure that the path of the image is valid

## **kit.text\_to\_handwriting(...)**

This function can be used to convert text to hand written characters, the character sets has been written by me.  

![Text to Handwriting](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/text_to_handwriting.PNG)

### The parameters are

**string** (required) - String that you want to convert to handwritten text  
**save\_to** (optional, save_to = "pywhatkit.png") - Path where the image will be saved  
**rgb** (optional, val = \(0,0,138\)) - Color of the handwritten character in rgb format

## **Some Other Functions**

```python
pywhatkit.show_history() # Will show information of all the messages sent using this library

pywhatkit.shutdown(time=100) # Will shutdown the system

pywhatkit.cancel_shutdown() # Will cancel the scheduled shutdown

pywhatkit.tutorial_hindi/english() # Will open a tutorial on how to use this library on YouTube in respective language

pywhatkit.join_discord() # Will redirect you to our Discord server

pywhatkit.help.<function>() # For more information about a function

```

## **Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
For more detailed information see [this](https://github.com/Ankit404butfound/PyWhatKit/blob/master/CONTRIBUTING.md).

## **License**

MIT
