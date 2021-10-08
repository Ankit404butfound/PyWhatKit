# Version 5.2
# Status: Stable
# Documentation: https://github.com/Ankit404butfound/PyWhatKit/wiki
# Report Bugs and Feature Requests here: https://github.com/Ankit404butfound/PyWhatKit/issues
# For further Information, Join our Discord: https://discord.gg/62Yf5mushu

__VERSION__ = "Version 5.2 (Stable)"

from pywhatkit.ascii_art import image_to_ascii_art
from pywhatkit.handwriting import text_to_handwriting
from pywhatkit.mail import send_mail, send_hmail
from pywhatkit.whats import (
    sendwhatmsg,
    sendwhatmsg_to_group,
    sendwhatmsg_instantly,
    sendwhats_image,
    open_web,
)
from pywhatkit.sc import shutdown, cancel_shutdown
from pywhatkit.misc import show_history, playonyt, info, search
from pywhatkit.webss import web_ss

from platform import system

if system().lower() in ("darwin", "windows"):
    from pywhatkit.misc import take_screenshot
