import platform
import os
from typing import NoReturn

osname = platform.system()


def shutdown(time: int = 20) -> NoReturn:
    """Shutdowns the machine in a given time"""
    # For Windows, time should be given in seconds
    # For MacOS and Linux based distributions, time should be given in minutes

    if "window" in osname.lower():
        cont = "shutdown -s -t %s" % time
        os.system(cont)

    elif "linux" in osname.lower():
        cont = "shutdown -h %s" % time
        os.system(cont)

    elif "darwin" in osname.lower():
        cont = "shutdown -h -t %s" % time
        os.system(cont)

    else:
        raise Warning(
            "This function is for Windows, Mac and Linux users only, can't execute on %s" % osname)


def cancel_shutdown() -> NoReturn:
    """Will cancel the scheduled shutdown"""
    if "window" in osname.lower():
        cont = "shutdown /a"
        os.system(cont)
        print("Shutdown has been Cancelled!")

    elif "linux" in osname.lower():
        cont = "shutdown -c"
        os.system(cont)
        print("Shutdown has been Cancelled!")

    elif "darwin" in osname.lower():
        cont = "killall shutdown"
        os.system(cont)
        print("Shutdown has been Cancelled!")

    else:
        raise Warning(
            "This function is for Windows and Linux only, can't execute on: %s" % osname)
