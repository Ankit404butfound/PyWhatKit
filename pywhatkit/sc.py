import platform
import os
try:
    import winerror
except ImportError or ModuleNotFoundError:
    pass


def shutdown(time: int = 20) -> None:
    """Gives a shutdown request to the system with the specified time"""

    # For Windows, time should be given in seconds
    # For MacOS and Linux based distributions, time should be given in minutes

    osname = platform.system()
    if "window" in osname.lower():
        cont = f"shutdown -s -t {time}"
        error_code = os.system(cont)
        # Here 1115 is the error code of scheduled shutdown.
        if error_code in [winerror.ERROR_SHUTDOWN_IN_PROGRESS, 1115]:
            print(
                "A shutdown process has already been scheduled...\nIgnoring this process")
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


def cancel_shutdown() -> None:
    """Will cancel the scheduled shutdown"""

    osname = platform.system()
    if "window" in osname.lower():
        error_code = os.system("shutdown /a")
        if error_code == winerror.ERROR_NO_SHUTDOWN_IN_PROGRESS:
            print(
                "ShutDown cancellation process has been aborted! [NO shutdown scheduled]")
        else:
            print("ShutDown has been cancelled")

    elif "linux" in osname.lower():
        os.system("shutdown -c")
        print("Shutdown has been Cancelled!")

    elif "darwin" in osname.lower():
        os.system("killall shutdown")
        print("Shutdown has been Cancelled!")

    else:
        raise Warning(
            f"This function is for Windows and Linux only, can't execute on: {osname}")
