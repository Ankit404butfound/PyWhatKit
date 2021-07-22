import webbrowser as web


def tutorial_hindi() -> None:
    """Watch tutorial on how to use this library on YouTube in Hindi"""

    web.open("https://youtu.be/o6WV9zFJg1o")


def tutorial_english() -> None:
    """Watch tutorial on how to use this library on YouTube in English"""

    web.open("https://youtu.be/vpfrwpO_HKY")


def developer_contact() -> None:
    """Contact information of developer for feedbacks"""

    link = "https://github.com/Ankit404butfound/PyWhatKit"
    print(f"You can reach out to us on GitHub {link} for help regarding any issues related to the module.")


def join_discord() -> None:
    """Opens the invite link for the discord server"""

    web.open("https://discord.gg/62Yf5mushu")
