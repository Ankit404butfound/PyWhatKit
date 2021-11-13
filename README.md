![image](https://media.discordapp.net/attachments/842794167134453820/882227960613048350/unknown.png?width=1440&height=420)

![image](https://flat.badgen.net/github/stars/Ankit404butfound/Pywhatkit)
![image](https://flat.badgen.net/github/forks/Ankit404butfound/Pywhatkit)
![image](https://flat.badgen.net/github/open-issues/Ankit404butfound/Pywhatkit)
![image](https://flat.badgen.net/github/open-prs/Ankit404butfound/Pywhatkit)
![image](https://flat.badgen.net/github/commits/Ankit404butfound/Pywhatkit)
![image](https://flat.badgen.net/github/license/Ankit404butfound/Pywhatkit)
![image](https://flat.badgen.net/github/contributors/Ankit404butfound/Pywhatkit)
![image](https://flat.badgen.net/github/release/Ankit404butfound/Pywhatkit)
<!-- ![logo](https://github.com/Ankit404butfound/PyWhatKit/raw/master/Images/logo.png?raw=true) -->

[PyWhatKit](https://pypi.org/project/pywhatkit/) is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Currently, it has about 300k+ downloads and counting. New updates are released frequently with new features and bug fixes.

# Links

- **Have some query or suggestions or want to become a beta tester, join our discord server - [Discord invite link](https://discord.gg/62Yf5mushu)**
- **Help us test an upcoming feature - [here](https://pywhatkit.herokuapp.com/remote-kit)**
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
