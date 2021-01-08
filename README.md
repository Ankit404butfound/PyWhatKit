![alt text](https://github.com/Ankit404butfound/PyWhatKit/blob/master/Images/logo.png?raw=true)

## Project description

PyWhatKit is a Python library for Sending whatsapp message at certain time, it has several other features too.

### Read detailed description here - https://pywhatkit.herokuapp.com/
### Request new feature here - https://pywhatkit.herokuapp.com/request-feature

## Download

[![Downloads](https://pepy.tech/badge/pywhatkit/month)](https://pepy.tech/project/pywhatkit/month)

## Note

Now you can schedule WhatsApp message and turn off the computer, the message will be automatically delivered at the scheduled time.
```python
from pywhatkit import headless_pwk as pwk
pwk.sendwhatmsg("+919876543210","Hi",15,25) #You will need to scan the QR code, please do read the comments in the file
```

## Installation

`pip install pywhatkit`

## Usage

Import the library using the following command.

`import pywhatkit`

#### This will open web.whatsapp.com at 14:59:40 and message will be sent at exactly 15:00:00

`pywhatkit.sendwhatmsg("+919876543210","This is a message",15,00)`

#### This will give wikipedia summary about the topic using the Wikipedia API

`pywhatkit.info("Python",lines=3)`

#### This will convert any given image to ASCII art, see my profile picture

`pywhatkit.image_to_ascii_art(path_to_image,output_file)`

#### This will convert that text to handwritten font with color combination 0,0,0 in RGB form

`pywhatkit.text_to_handwriting(text,rgb=[0,0,0])`

Something like this

![alt text](https://qphs.fs.quoracdn.net/main-qimg-6cb9c5263774b71a7905741ece958cc9)

#### This will play the first video that appears upon searching "Python" on YouTube

`pywhatkit.playonyt("Python")`

#### This will perform a Google search about Python

`pywhatkit.search("Python")`

### Some other functions
```python
pywhatkit.showHistory()#Will show information of all the messages sent using this library

pywhatkit.shutdown(time=100)#Will shutdown the system in 100 seconds

pywhatkit.cancelShutdown()#Will cancel the scheduled shutdown

pywhatkit.watch_tutorial_in_english/hindi()#Will open a tutorial on how to use this library on YouTube in respective language

pywhatkit.sendMail(my_mail, my_pass, mail_to, content):  #to send a mail to anybody. 

pywhatkit.help() #For more information

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
