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
        # print(request.get_json())
        return "ok"
    return """<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <meta name='viewport'
     content='width=device-width, initial-scale=1.0, maximum-scale=1.0,
     user-scalable=0' >
    <script type="text/javascript" charset="utf-8">
    function init() {
        var touchzone = document.getElementById("zone");
        touchzone.addEventListener("touchend", clicke, false);
        touchzone.addEventListener("touchmove", handle, false);
        touchzone.addEventListener("touchstart", tostart, false);
        var scrollzone = document.getElementById("scroll");
        scrollzone.addEventListener("touchmove", scrollmove, false);
        scrollzone.addEventListener("touchstart", tostart, false);
    }

function scrollmove(event){
  var a    = event.touches[0].pageX;
  var b     = event.touches[0].pageY;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  };
  xhttp.open("POST", "scroller", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("a="+a+"&b="+b);
}


function tostart(event){
  var a    = event.touches[0].pageX;
  var b     = event.touches[0].pageY;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  };
  xhttp.open("POST", "tstart", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("a="+a+"&b="+b);
}

function clicke(event) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  };
  var a = event.changedTouches[0].pageY;
  xhttp.open("POST", "click", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("a="+a);
}

function dragm() {
    var btn = document.getElementById("drag");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    };
    xhttp.open("POST", "dradhandler", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();

    if (btn.innerHTML == "Drag mouse"){
        btn.innerHTML = "Move mouse";
    }
    else{
        btn.innerHTML = "Drag mouse";
    }
}

function sendData(a,b,g) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  };
  xhttp.open("POST", "handler", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("a="+a+"&b="+b);
}


 function handle(event) {
  var alpha    = event.touches[0].pageX;
  var beta     = event.touches[0].pageY;
  sendData(alpha,beta);
}


function on_input(){
  var data = document.getElementById("inpfield").value;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  };
  xhttp.open("POST", "typed", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("data="+data);
}
function enter_but(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  };
  xhttp.open("POST", "enter", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("data="+"data");
}




    </script>

    <meta name="" content="">
    <title></title>
  <style>
  .center{
    position: fixed;
    background-color: rgb(230,230,230);
    width:80%;
    height:400px;
    top:300px;
    left:46%;
    color:rgb(200,200,200);
    font-weight:bold;
    transform: translate(-50%,-50%);
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
   }
   html{
   touch-action:pan-down
   }

   .scrollarea{
    position: fixed;
    background-color: rgb(230,230,230);
    width:30px;
    height:400px;
    top:300px;
    left:92.05%;
    color:rgb(200,200,200);
    font-weight:bold;
    transform: translate(-50%,-50%);
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    text-align:center;
   }


  </style>
  </head>
  <body onload="init()">
  <p style="text-align:center;">Type on PC
  <input id="inpfield"type="text" oninput=on_input()></input>
  <button type="button" onclick="enter_but()">Enter</button></p>
  <div style="text-align:center;">
      <button id="drag" type="button" onclick="dragm()">Drag mouse</button>
  </div>
    <div class="center" id="zone">
        <p align="center"><br><br><br><br><br><br>Left click area<br><br><br><br><br><br><hr></p>
        <p align="center"><br>Right click area</p>
    </div>
    <div class="scrollarea" id="scroll">
       <p><br><br><br><br><br>S<br>C<br>R<br>O<br>L<br>L</p>
    </div>
  </body>
</html>"""


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
