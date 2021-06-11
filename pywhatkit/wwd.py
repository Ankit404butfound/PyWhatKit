import webbrowser as web
from typing import NoReturn


def tutorial_hindi() -> NoReturn:
    """Watch tutorial on how to use this library on YouTube in Hindi"""
    web.open("https://youtu.be/Fy7hmZ_YDjQ")

    # Previously, it was this video https://www.youtube.com/watch?v=3hUi0qfrWWo&t=3s


def tutorial_english() -> NoReturn:
    """Watch tutorial on how to use this library on YouTube in English"""
    web.open("https://youtu.be/nAjbapi4Qk8")


def developer_contact() -> NoReturn:
    """Contact information of developer for feedbacks"""
    print("Message me on Telegram, username - Tag_kiya_kya\nOr email me at ankitrajjitendra816@gmail.com.")


def join_discord() -> NoReturn:
    """Opens the invite link for the discord server"""
    web.open("https://discord.gg/NSdZknvDdH")
