import platform
import os

osname = platform.system()

def shutdown(time = 20):
    """Will shutdown the computer in given seconds
For Windows and Linux only"""
    
    if "window" in osname.lower():
        cont = "shutdown -s -t %s"%time
        os.system(cont)

    elif "linux" in osname.lower():
        cont = "shutdown -h %s"%time
        os.system(cont)

    elif "darwin" in osname.lower():
        cont = "shutdown -h -t %s"%time
        os.system(cont)

    else:
        raise Warning("This function is for Windows, Mac and Linux users only, can't execute on %s"%osname)

def cancelShutdown():
    """Will cancel the scheduled shutdown"""
    if "window" in osname.lower():
        cont = "shutdown /a"
        os.system(cont)

    elif "linux" in osname.lower():
        cont = "shutdown -c"
        os.system(cont) 

    elif "darwin" in osname.lower():
        cont = "killall shutdown"
        os.system(cont)

    else:
        raise Warning("This function is for Windows and Linux only, can't execute on: %s"%osname)
