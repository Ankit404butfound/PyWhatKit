import sys
import pywhatkit

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f"Args: <phone number> <msg1> [<msg2> [...]]")
        sys.exit(0)

    phone_number = sys.argv[1]
    messages = sys.argv[2:]
    pywhatkit.sendwhatmsg_instantly(
        phone_number, 
        messages,
        tab_close=True)
