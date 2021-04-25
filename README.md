![logo](https://github.com/Ankit404butfound/PyWhatKit/blob/master/Images/logo.png?raw=true)

## *Project Description*

PyWhatKit is a Python library for Sending WhatsApp message at certain time, it has several other features too.
It is one of the safest tools for scheduling WhatsApp messages.

## *Useful Links*

### Read detailed description here - https://pywhatkit.herokuapp.com/

### Request new feature here - https://pywhatkit.herokuapp.com/request-feature

### Have some query or suggestions, join our discord server - [here](https://discord.com/channels/@me/830257036478119946/830370312653766727)

## *Downloads*

[![Downloads](https://pepy.tech/badge/pywhatkit/month)](https://pepy.tech/project/pywhatkit/month)

## *Installation*

`pip3 install pywhatkit`

## *Usage*

Import the library using the following command.

`import pywhatkit`
>

- This will open web.whatsapp.com at 14:59:40 and message will be sent at exactly 15:00:00

    `pywhatkit.sendwhatmsg("+919876543210","This is a message",15,00)`

- This will give wikipedia summary about the topic using the Wikipedia API

    `pywhatkit.info("Python",lines=3)`

- This will convert any given image to ASCII art, see my profile picture

    `pywhatkit.image_to_ascii_art(path_to_image,output_file)`

- This will convert that text to handwritten font with color combination 0,0,0 in RGB form

    `pywhatkit.text_to_handwriting(text,rgb=[0,0,0])`

<br>

![character to handwriting](https://qphs.fs.quoracdn.net/main-qimg-6cb9c5263774b71a7905741ece958cc9)

- This will play the first video that appears upon searching "Python" on YouTube

    `pywhatkit.playonyt("Python")`

- This will perform a Google search about Python

    `pywhatkit.search("Python")`

### Some other functions

```python
pywhatkit.showHistory() # Will show information of all the messages sent using this library

pywhatkit.shutdown(time=100) # Will shutdown the system

pywhatkit.cancelShutdown() # Will cancel the scheduled shutdown

pywhatkit.watch_tutorial_in_english/hindi() # Will open a tutorial on how to use this library on YouTube in respective language

pywhatkit.sendMail(my_mail, my_pass, mail_to, content) # To send a mail to anybody.

pywhatkit.help() # For more information

```

## *Contributing*

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
For more detailed information see [this](https://github.com/Ankit404butfound/PyWhatKit/blob/master/CONTRIBUTING.mdhttps://github.com/Ankit404butfound/PyWhatKit/blob/master/CONTRIBUTING.md)

## *License*

MIT
