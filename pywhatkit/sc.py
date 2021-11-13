import os
import platform

try:
    import winerror
except ImportError or ModuleNotFoundError:
    pass

osname = platform.system()


def shutdown(time: int = 20) -> None:
    """Schedules a Shutdown after the Specified Time"""

    if "window" in osname.lower():
        cont = f"shutdown -s -t {time}"
        error_code = os.system(cont)
        if error_code in [winerror.ERROR_SHUTDOWN_IN_PROGRESS, 1115]:
            print("A Shutdown Process has already been Scheduled!")
        else:
            print(f"Your System will Shutdown in {time} Seconds!")

    elif "linux" in osname.lower():
        cont = f"shutdown -h {time}"
        os.system(cont)
        print(f"Your System will Shutdown in {time} Minutes!")

    elif "darwin" in osname.lower():
        cont = f"shutdown -h -t {time}"
        os.system(cont)
        print(f"Your System will Shutdown in {time} Minutes!")

    else:
        raise Warning(
            f"Available on Windows, Mac and Linux only, can't Execute on {osname}"
        )


def cancel_shutdown() -> None:
    """Cancels the Scheduled Shutdown"""

    if "window" in osname.lower():
        error_code = os.system("shutdown /a")
        if error_code == winerror.ERROR_NO_SHUTDOWN_IN_PROGRESS:
            print(
                "Shutdown Cancellation process has been Aborted! [NO Shutdown Scheduled]"
            )
        else:
            print("Shutdown has been Cancelled!")

    elif "linux" in osname.lower():
        os.system("shutdown -c")
        print("Shutdown has been Cancelled!")

    elif "darwin" in osname.lower():
        os.system("killall shutdown")
        print("Shutdown has been Cancelled!")

    else:
        raise Warning(
            f"Available on Windows, Mac and Linux only, can't Execute on {osname}"
        )
