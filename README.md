
![logo](https://github.com/Ankit404butfound/PyWhatKit/raw/master/Images/logo.png?raw=true)


  
[PyWhatKit](https://pypi.org/project/pywhatkit/) is a Python library with various helpful features. It is an easy-to-use library which does not require you to do some additional setup. Currently, it has about 100k+ downloads and counting, and new updates are released frequently with various bug fixes.

# Links

- ### Have some query or suggestions or want to become a beta tester, join our discord server - [Discord invite link](https://discord.gg/uwznv4jKgk)
- ### Help us test an upcoming feature - https://pywhatkit.herokuapp.com/remote-kit

# Installation

This library can be installed by the pip command, open you command prompt and type in the following command...

`pip install pywhatkit`

# Functions of this library

First import the library using the command `import pywhatkit as kit` and then proceed to call the functions

## kit.sendwhatmsg()

This function can be used to send WhatsApp message at certain time  
  
![](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/sendwhatmsg.png)  

### The parameters are

**phone\_num** (required) - Phone number of target with country code  
**message** (required) - Message that you want to sendwhatmsg  
**time\_hour** (required) - Hours at which you want to send message in 24 hour format  
**time\_min** (required) - Minutes at which you want to send message  
**wait\_time** (optional, val=20) - Seconds after which the message will be sent after opening the web  
**print\_waitTime** (optional, val=True) - Will print the remaining time if set to true  

### Some common errors

**CountryCodeException** - Check if the phone number passed into the parameter has [country code](https://en.wikipedia.org/wiki/List_of_country_calling_codes)  
**Message not getting delivered** - Check internet speed and increase wait\_time to 30 or above
**CallTimeException** - The web takes some time to load so some delay is required, make sure the seconds left is greater than the wait\_time  
**SyntaxError** - Make sure the first two parameters are string and the rest are int

  

## kit.playonyt()

This function can be used to search and play a particular video on YouTube by using just the keyword, like "Shape of You song"  
  
![](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/playonyt.png)  

### The parameters are

**topic** (required) - Topic or title that is related to the video

#### Some common errors

**Video not opening** - Make sure the topic exists, or you have provided proper spelling

  

## kit.search()

This function can be used to make a Google search for any term  
  
![](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/search.PNG)

### The parameters are

**topic** (required) - Topic or title that you want to search

  

## kit.info()

This function can be used to fetch information about any topic  
  
![](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/info.PNG)

### The parameters are

**topic** (required) - Topic or title that you want to get information about  
**lines** (optional, val=3) - Number of lines that you want to print about it

#### Some common errors

**Not returning paragraph** - Make sure the topic exists, and you are providing specific title

  

## kit.image\_to\_ascii\_art()

This function can be used to convert any image to ASCII art  
  
![](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/asciiart.PNG)

### The parameters are

**imgpath** (required) - Path to the image that you want to convert  
**output\_file** (optional, val=pywhatkit\_asciiart.txt") - File where you want to save the output characters

#### Some common errors

**File not found** - Make sure that the path of the image is valid

  

## kit.text\_to\_handwriting()

This function can be used to convert text to handwritten characters, the character sets has been written by me  
  
![](https://raw.githubusercontent.com/Ankit404butfound/PyWhatKit/master/Images/text_to_handwriting.PNG)

### The parameters are

**string** (required) - String that you want to convert to handwritten text  
**save\_to** (optional, val = "pywhatkit.png") - Path where the image will be saved  
**rgb** (optional, val = \[0,0,138\]) - Color of the handwritten character in rgb format

## Some other functions

```python
pywhatkit.showHistory() # Will show information of all the messages sent using this library

pywhatkit.shutdown(time=100) # Will shutdown the system

pywhatkit.cancelShutdown() # Will cancel the scheduled shutdown

pywhatkit.tutorial_hindi/english() # Will open a tutorial on how to use this library on YouTube in respective language

pywhatkit.help.<function>() # For more information

```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
For more detailed information see [this](https://github.com/Ankit404butfound/PyWhatKit/blob/master/CONTRIBUTING.mdhttps://github.com/Ankit404butfound/PyWhatKit/blob/master/CONTRIBUTING.md)

## License

MIT
