def showHistory():
    """Prints the information of all last sent messages using this program"""
    with open("pywhatkit_dbs.txt","r") as f:
        content = f.read()

    if content == "--------------------":
        content = None
    print(content)
