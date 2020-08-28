# PyWhatKit

# Project description

pywhatkit is a Python library for Sending whatsapp message at certain time, it has several other features too.

Installation
`
pip install pywhatkit
`
# Usage
`
import pywhatkit

pywhatkit.sendwhatmsg_with_selenium("+919876543210","This is a message",15,00)#Will send message with most of the processes hidden

pywhatkit.send_file("+919876543210","Path to file",15,00)#Will send file to number with most of the processes hidden

pywhatkit.sendwhatmsg("+919876543210","This is a message",15,00)#Will open web.whatsapp.com at 14:59 and message will be sent at exactly 15:00

pywhatkit.info("Python",lines=3,speak=None)#Will give information about the topic

pywhatkit.playonyt("Python")#Will play the first YouTube video having "Python" in it

pywhatkit.search("Python")#Will perform a Google search

pywhatkit.showHistory()#Will show information of all the messages sent using this library

pywhatkit.shutdown(time=100)#Will shutdown the system in 100 seconds

pywhatkit.cancelShutdown()#Will cancel the scheduled shutdown

pywhatkit.watch_tutorial_in_english/hindi()#Will open a tutorial on how to use this library on YouTube in respective language

pywhatkit.help() #For more information
`
# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# License
MIT
