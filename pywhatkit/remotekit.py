import logging
import sys
import threading

import pyautogui as p
from flask import Flask, request

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

cli = sys.modules["flask.cli"]
cli.show_server_banner = lambda *x: None

app = Flask("app")

p.FAILSAFE = False
moving = False
drag = False
type_data = ""
old_data = ""
coords = (0, 0)
lastcords = (0, 0)
lstmcord = (0, 0)
lstlen = 0
coords = [(0, 0)]

@app.route("/", methods=["GET", "POST"])
def send() -> str:
    # print("here")
    if request.method == "POST":
        webelement = open("web.html","r").read()
        # print(request.get_json())
        return "ok"
    return webelement


@app.route("/handler", methods=["POST"])
def handle() -> str:
    global moving, cordlst, lastcords
    lst = []
    a = request.form["a"]
    b = request.form["b"]
    a = float(a)
    b = float(b)
    moving = True
    coords = (a, b)
    lx, ly = lastcords
    cx, cy = coords
    # print(cx,cy)
    # p.moveRel((cx-lx)/2,(cy-ly)/2)
    threading.Thread(target=lambda: p.moveRel((cx - lx) * 2, (cy - ly) * 2)).start()
    lastcords = coords
    return "1"


@app.route("/scroller", methods=["POST"])
def scrollerr() -> str:
    global moving, cordlst, lastcords2
    a = request.form["a"]
    b = request.form["b"]
    a = float(a)
    b = float(b)
    coords = (a, b)
    lx, ly = lastcords2
    cx, cy = coords
    if cy < ly:
        threading.Thread(target=lambda: p.scroll(50)).start()
    if cy > ly:
        threading.Thread(target=lambda: p.scroll(-50)).start()
    lastcords2 = coords
    return "1"


@app.route("/tstart", methods=["POST"])
def startt() -> str:
    global lastcords, lastcords2
    # print("end")
    a = request.form["a"]
    b = request.form["b"]
    # print(a,b)
    a = float(a)
    b = float(b)
    lastcords = (a, b)
    lastcords2 = (a, b)
    return "1"


@app.route("/click", methods=["POST"])
def do_click() -> str:
    global moving
    if not moving:
        a = request.form["a"]
        # print(a)
        a = float(a)
        if a < 400:
            p.click()
        if a >= 400:
            p.rightClick()

    moving = False
    return "1"


@app.route("/typed", methods=["POST"])
def typeit() -> str:
    global type_data, old_data
    data = request.form["data"]
    type_data = str(data)
    if len(type_data) > len(old_data):
        p.typewrite(type_data[len(type_data) - 1])
    else:
        p.press("backspace", len(old_data) - len(type_data))
    old_data = type_data
    return "1"


@app.route("/enter", methods=["POST"])
def slashN() -> str:
    p.press("enter")
    return "1"


@app.route("/dradhandler", methods=["POST"])
def ghasit_mouse() -> str:
    global drag
    # print(drag)
    if drag == True:
        drag = False
        p.mouseUp()

    else:
        drag = True
        p.mouseDown()

    return "1"


def start_server(port=8000, print_msg=True):
    if print_msg:
        print("Server started at local_ip_of_this_pc:%s" % port)
        print("Print Ctrl+C to exit")
    app.run(host="0.0.0.0", port=port)


# app.run(host='0.0.0.0')
#
#
# def main():
#     app.run(host="192.168.43.17", port=33)
#
#
# if __name__ == "__main__":
#     main()
#     app.run(host='localhost')
