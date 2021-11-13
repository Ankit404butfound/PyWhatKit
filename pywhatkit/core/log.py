import os
import time

from pywhatkit.core.core import check_number


def format_message(message: str) -> str:
    """Formats the Message to remove redundant Spaces and Newline chars"""
    msg_l = message.split(" ")
    new = []
    for x in msg_l:
        if "\n" in x:
            x = x.replace("\n", "")
            new.append(x) if not len(x) == 0 else None

        elif len(x) != 0:
            new.append(x)

    return " ".join(new)


def log_message(_time: time.struct_time, receiver: str, message: str) -> None:
    """Logs the Message Information after it is Sent"""

    if not os.path.exists("PyWhatKit_DB.txt"):
        file = open("PyWhatKit_DB.txt", "w+")
        file.close()

    message = format_message(message)

    with open("PyWhatKit_DB.txt", "a", encoding="utf-8") as file:
        if check_number(receiver):
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Phone Number: {receiver}\nMessage: {message}"
            )
        else:
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Group ID: {receiver}\nMessage: {message}"
            )
        file.write("\n--------------------\n")
        file.close()


def log_image(_time: time.struct_time, path: str, receiver: str, caption: str) -> None:
    """Logs the Image Information after it is Sent"""

    if not os.path.exists("PyWhatKit_DB.txt"):
        file = open("PyWhatKit_DB.txt", "w+")
        file.close()

    caption = format_message(caption)

    with open("PyWhatKit_DB.txt", "a", encoding="utf-8") as file:
        if check_number(number=receiver):
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Phone Number: {receiver}\nImage: {path}\nCaption: {caption}"
            )

        else:
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Group ID: {receiver}\nImage: {path}\nCaption: {caption}"
            )
        file.write("\n--------------------\n")
        file.close()
