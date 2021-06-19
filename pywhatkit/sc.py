import platform
import os
from typing import NoReturn
import winerror 
osname = platform.system()


def shutdown(time: int = 20) -> NoReturn:
    """
    Gives a shutdown request to the system with the specified time

    Args:
    `time`: Governs the time for shutdown. Taken as `int` in unit `seconds`. `Specified default value is 20`
    """
    # For Windows, time should be given in seconds
    # For MacOS and Linux based distributions, time should be given in minutes
    global osname
    osname = platform.system()
    if "window" in osname.lower():
        cont = f"shutdown -s -t {time}"
        ErrorCode = os.system(cont)
        if ErrorCode == winerror.ERROR_SHUTDOWN_IN_PROGRESS or ErrorCode == 1115:# Here 1115 is the error code of scheduled shutdown.
            print("A shutdown process has already been scheduled...\nIgnoring this process")

        else:
            print(f"Your System will shutdown in {time} seconds")

    elif "linux" in osname.lower():
        cont = f"shutdown -h {time}"
        os.system(cont)

    elif "darwin" in osname.lower():
        cont = f"shutdown -h -t {time}"
        os.system(cont)

    else:
        raise Warning(
            "This function is for Windows, Mac and Linux users only, can't execute on {}".format(osname))


def cancel_shutdown() -> NoReturn:
    """
    Will cancel the scheduled shutdown
    """
    global osname
    osname = platform.system()
    if "window" in osname.lower():
        cont = "shutdown /a"
        ErrorCode = os.system(cont)
        if ErrorCode == winerror.ERROR_NO_SHUTDOWN_IN_PROGRESS:
            print("ShutDown cancellation process has been aborted! [NO shutdown scheduled]")
        else:
            print("ShutDown has been cancelled")

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
            f"This function is for Windows and Linux only, can't execute on: {osname}")
