![image](https://media.discordapp.net/attachments/842794167134453820/882227960613048350/unknown.png?width=1440&height=420)

[![image](https://flat.badgen.net/github/stars/Ankit404butfound/Pywhatkit)](https://github.com/Ankit404butfound/PyWhatKit/stargazers)
[![image](https://flat.badgen.net/github/forks/Ankit404butfound/Pywhatkit)](https://github.com/Ankit404butfound/PyWhatKit/network/members)
[![image](https://flat.badgen.net/github/open-issues/Ankit404butfound/Pywhatkit)](https://github.com/Ankit404butfound/PyWhatKit/issues)
[![image](https://flat.badgen.net/github/open-prs/Ankit404butfound/Pywhatkit)](https://github.com/Ankit404butfound/PyWhatKit/pulls)
[![image](https://flat.badgen.net/github/commits/Ankit404butfound/Pywhatkit)](https://github.com/Ankit404butfound/PyWhatKit/commits/master)
[![image](https://flat.badgen.net/github/license/Ankit404butfound/Pywhatkit)](https://github.com/Ankit404butfound/PyWhatKit/LICENCE)
[![image](https://flat.badgen.net/github/contributors/Ankit404butfound/Pywhatkit)](https://github.com/Ankit404butfound/PyWhatKit/graphs/contributors)
[![image](https://flat.badgen.net/github/release/Ankit404butfound/Pywhatkit)](https://github.com/Ankit404butfound/PyWhatKit/releases)
<!-- ![logo](https://github.com/Ankit404butfound/PyWhatKit/raw/master/Images/logo.png?raw=true) -->

###### I am a bit busy these days and not able to maintain this project properly, if you are passionate about programming and knows a bit about the internal workings of this library and is willing to contribute and improve the project, contact me on Discord or Email, I will give you push access to the repo and release access to the PyPi project. Beginners are always welcomed as long as you don't break the new release 😂😅.

[PyWhatKit](https://pypi.org/project/pywhatkit/) is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Currently, it is one of the most popular library for WhatsApp and YouTube automation. New updates are released frequently with new features and bug fixes.

# Links

- **Join our discord server - https://discord.gg/62Yf5mushu**
- **Documentation - [Wiki](https://github.com/Ankit404butfound/PyWhatKit/wiki)**

## Installation and Supported Versions

PyWhatKit is available on PyPi:

```bash
python3 -m pip install pywhatkit
```

```bash
pip3 install pywhatkit
```

PyWhatKit officially supports Python 3.8+.

## Cloning the Repository

```bash
git clone https://github.com/Ankit404butfound/PyWhatKit.git
```
## What's new in v5.4?
```
Fix Flask import error
```
## What's new in v5.3?
```py
import pywhatkit
pywhatkit.start_server()
```
### This method can be used to remotely control your PC using your phone (Windows only)
- Make sure your PC and your phone are on same network, on your PC, Open Network and Internet Settings > Properties > Network Profile, make sure it's set to Private.
- Run the above code and then open command prompt and type `ipconfig`.
- Search for `IPv4 Address` and on your phone's browser type this address and append `:8000` at the end, example `192.168.0.1:8000`.
- Try moving you finger and you should notice your cursor moving too.
- You can also type and scroll too, enjoy.
- More information here https://pywhatkit.herokuapp.com/remote-kit with the raw code.

## Features

- Sending Message to a WhatsApp Group or Contact
- Sending Image to a WhatsApp Group or Contact
- Converting an Image to ASCII Art
- Converting a String to Handwriting
- Playing YouTube Videos
- Sending Mails with HTML Code
- Install and Use

## Usage

```py
import pywhatkit

# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("PyWhatKit")
```

For more Examples and Functions, have a look at the [Wiki](https://github.com/Ankit404butfound/PyWhatKit/wiki).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Be sure to read the [Guidelines](https://github.com/Ankit404butfound/PyWhatKit/blob/master/CONTRIBUTING.md) before Contributing.

## License

MIT.
For more information see [this](https://github.com/Ankit404butfound/PyWhatKit/blob/master/LICENSE)
