def show_history() -> None:
    """Prints the information of all the sent messages using this program"""

    with open("pywhatkit_dbs.txt", "r") as f:
        content = f.read()

    if content == "--------------------":
        content = None
    print(content)
