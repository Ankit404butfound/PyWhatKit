# Version 5.2
# Status: Stable
# Documentation: https://github.com/Ankit404butfound/PyWhatKit/wiki
# Report Bugs and Feature Requests here: https://github.com/Ankit404butfound/PyWhatKit/issues

import pywhatkit.help
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
