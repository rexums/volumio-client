import tkinter
import requests
import tkinter.messagebox
from tkinter import *
import wget
import os
import sys

debug = "false"

color = "#CCEEFF"
botname = "Volumio Client"
github = "https://github.com/rexums/volumio-client/"
bcolor = "#F7819F"

try:
    F = open("url.txt", "r")
except:
    pass

try:
    os.remove("icon.png")
except:
    pass
wget.download("https://github.com/rexums/volumio-client/raw/master/icon.png")

root = tkinter.Tk()
root.title(botname)
root.configure(background=color)

try:
    root.iconphoto(False, tkinter.PhotoImage(file='icon.png'))
except:
    pass

def exiting():
    sys.exit()

def play():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=play")
    tkinter.messagebox.showinfo(botname,m.json()["response"])
    if debug == "true":
        print("Play executed")
        print(m.text)

def onlystop():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=stop")
    tkinter.messagebox.showinfo(botname,m.json()["response"])
    if debug == "true":
        print("Stop executed")
        print(m.text)

def toggle():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=toggle")
    tkinter.messagebox.showinfo(botname,m.json()["response"])
    if debug == "true":
        print("toggle executed")
        print(m.text)

def volume():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=volume&volume=" + vol.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Volume executed")
        print(m.text)

def np():
    m = requests.get(url.get() + "/api/v1/getState")
    tkinter.messagebox.showinfo(botname, m.json()["title"])
    if debug == "true":
        print("Now Playing executed")
        print(m.text)

def credits():
    tkinter.messagebox.showinfo(botname,'Client by rexjohannes98')
    if debug == "true":
        print("Credits executed")



def skip():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=next")
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed Skip")
        print(m.text)

def loop():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=repeat")
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed repeat")
        print(m.text)

def prev():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=prev")
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed Prev")
        print(m.text)

def playlist():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=playplaylist&name=" + pl.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed playlist")
        print(m.text)

def shuffle():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=random")
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed shuffle")
        print(m.text)

def clearplaylist():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=clearQueue")
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed clear")
        print(m.text)

def playl():
    try:
        m = requests.get(url.get() + "/api/v1/getQueue")
        videos = ""
        for video in m.json()["queue"]:
            videos += video["title"] + "\n"
        tkinter.messagebox.showinfo(botname, videos)
    except:
        tkinter.messagebox.showinfo(botname, "An unknown error occurred")


def changelog():
    try:
        m = requests.get("https://raw.githubusercontent.com/rexums/volumio-client/master/changelog.txt")
        tkinter.messagebox.showinfo(botname, m.text)
    except:
        tkinter.messagebox.showinfo(botname, "An unknown error occurred")


def control():
    root3 = tkinter.Tk()
    root3.title(botname)
    root3.configure(background=color)

    tkinter.Label(root3,
                  text="""Control:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    tkinter.Button(root3,
                   text="Play",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=play,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Stop",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=onlystop,
                   fg="black").pack()

    tkinter.Label(root3,
                  text="""Skip:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    tkinter.Button(root3,
                   text="Prev",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=prev,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Next",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=skip,
                   fg="black").pack()

    tkinter.Label(root3,
                  text="""Pause:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    tkinter.Button(root3,
                   text="Pause",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=pause,
                   fg="black").pack()

    tkinter.Label(root3,
                  text="""Misc:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    tkinter.Button(root3,
                   text="Shuffle",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=shuffle,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Clear",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=clearplaylist,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Loop",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=loop,
                   fg="black").pack()

    root3.mainloop()

label333 = tkinter.Label(root,
                         text="Url",
width=20,
                      background=color)
url = tkinter.Entry(root,
                        fg="black")

try:
    url.insert(1, F.read())
except:
    url.insert(1,"")
label333.pack()
url.pack()


def pause():
    m = requests.get(url.get() + "/api/v1/commands/?cmd=pause")
    tkinter.messagebox.showinfo(botname, m.json()["respone"])
    if debug == "true":
        print(m.text)

def lists():
    m = requests.get(url.get() + "/api/v1/listplaylists")

    listss = ""

    for x in m.json():
        listss += x + "\n"
    tkinter.messagebox.showinfo(botname, listss)



vollabel = tkinter.Label(root,
                         text="Volume",
                      background=color)
vol = tkinter.Entry(root)
vol.insert(1, "70")
vollabel.pack()
vol.pack()

pllabel = tkinter.Label(root,
                         text="Playlist",
                      background=color)
pl = tkinter.Entry(root)
pllabel.pack()
pl.pack()

tkinter.Label(root, text="Play", background=color, padx=50).pack()

tkinter.Button(root,
    text="Play Playlist",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=playlist,
    fg="black").pack()

label23 = tkinter.Label(root,
                        text="Control",
                      background=color,
                      padx=50)
label23.pack()

tkinter.Button(root,
    text="Volume",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=volume,
    fg="black").pack()

tkinter.Button(root,
               text="Toggle",
               width=20,
               justify=tkinter.RIGHT,
               height=1,
               bg=bcolor,
               command=toggle,
               fg="black").pack()


tkinter.Button(root,
    text="More",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=control,
    fg="black").pack()

label222 = tkinter.Label(root,
                         text="Player",
                      background=color,
                      padx=55)
label222.pack()

tkinter.Button(root,
    text="Now",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=np,
    fg="black").pack()

tkinter.Button(root,
    text="Queue",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=playl,
    fg="black").pack()

tkinter.Button(root,
    text="Playlists",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=lists,
    fg="black").pack()

tkinter.Label(root,
            text="Misc",
            background=color,
            padx=60).pack()

tkinter.Button(root,
    text="Exit",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=exiting,
    fg="black").pack()

tkinter.Button(root,
               text="Credits",
               width=20,
               justify=tkinter.RIGHT,
               height=1,
               bg=bcolor,
               command=credits,
               fg="black").pack()

tkinter.Button(root,
               text="Changelog",
               width=20,
               justify=tkinter.RIGHT,
               height=1,
               bg=bcolor,
               command=changelog,
               fg="black").pack()

root.mainloop()
