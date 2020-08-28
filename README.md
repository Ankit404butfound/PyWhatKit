# PyWhatKit

## Project description

**PyWhatKit is a Python library for Sending whatsapp message at certain time, it has several other features too.**

## Installation
```
pip install pywhatkit
````
## Usage
```
import pywhatkit

pywhatkit.sendwhatmsg("+919876543210","This is a message",15,00)#Will open web.whatsapp.com at 14:59 and message will be sent at exactly 15:00

pywhatkit.info("Python",lines=3,speak=None)#Will give information about the topic

pywhatkit.image_to_ascii_art(path_to_image,output_file)#Will convert that image to ASCII art

pywhatkit.text_to_handwriting(text,rgb=[0,0,0])#Will convert that text to handwritten font with color combination 0,0,0 in RGB form

pywhatkit.playonyt("Python")#Will play the first YouTube video having "Python" in it

pywhatkit.search("Python")#Will perform a Google search

pywhatkit.showHistory()#Will show information of all the messages sent using this library

pywhatkit.shutdown(time=100)#Will shutdown the system in 100 seconds

pywhatkit.cancelShutdown()#Will cancel the scheduled shutdown

pywhatkit.watch_tutorial_in_english/hindi()#Will open a tutorial on how to use this library on YouTube in respective language

pywhatkit.help() #For more information
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
