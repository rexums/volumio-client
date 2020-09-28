import tkinter
import requests
import webbrowser
import tkinter.messagebox
import sys
from tkinter import *

try:
    import rpc

    client_id = '756479035009269770'
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)

    activity = {
        "state": "unique-music.xyz",
        "details": "Get the bot now!",
        "assets": {
            "large_text": "Unique-Music",
            "large_image": "logo"
        }
    }
    rpc_obj.set_activity(activity)
except:
    pass

debug = "false"

url = 'https://discord.com/oauth2/authorize?client_id=665854713845121025&permissions=8&scope=bot'
color = "#CCEEFF"
apiurl = "https://api.unique-music.xyz/"
botname = "Unique-Music"
botwebsite = "https://unique-music.xyz/"
support = "https://discord.gg/gCPFbBM"
github = "https://github.com/rexjohannes/unique-player/"
download = botwebsite + "main.py"
status = "https://unique-music.instatus.com"
bcolor = "#F7819F"

try:
    F = open("session.txt", "r")
except:
    pass

ver = requests.get(botwebsite + "version.txt")
vers = ver.text
vers = int(vers)

root = tkinter.Tk()
root.title(botname)
root.configure(background=color)

try:
    root.iconphoto(False, tkinter.PhotoImage(file='icon.png'))
except:
    pass

try:
    requests.get(apiurl)
except:
    tkinter.messagebox.showinfo(botname, "Servers are offline")
    sys.exit()


#tabControl = ttk.Notebook(root)
#tab1 = tkinter.Frame(tabControl)
#tab2 = tkinter.Frame(tabControl)
#tab3 = tkinter.Frame(tabControl)
#tab4 = tkinter.Frame(tabControl)
#tab5 = tkinter.Frame(tabControl)
#tab6 = tkinter.Frame(tabControl)

#tabControl.add(tab1, text ='Login')
#tabControl.add(tab2, text ='Main')
#tabControl.add(tab3, text ='Config')
#tabControl.add(tab4, text ='Control')
#tabControl.add(tab5, text ='Player')
#tabControl.add(tab6, text ='Misc')

#tabControl.pack()

def open():
    webbrowser.open(url)
    if debug == "true":
        print("Invite Me! executed")

def exiting():
    sys.exit()

def onlystop():
    m = requests.get(apiurl + "leave?session=" + session.get())
    tkinter.messagebox.showinfo(botname,m.json()["response"])
    if debug == "true":
        print("Stop executed")
        print(m.text)

def volume():
    m = requests.get(apiurl + "volume?session=" + session.get() + "&volume=" + vol.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Volume executed")
        print(m.text)

def np():
    m = requests.get(apiurl + "status?session=" + session.get())
    tkinter.messagebox.showinfo(botname, m.json()["title"])
    if debug == "true":
        print("Now Playing executed")
        print(m.text)

def other():
    m = requests.get(apiurl + "stats")
    tkinter.messagebox.showinfo(botname,m.json()["guilds"] + " - Server\n" + m.json()["users"] + " - User\n" + m.json()["channels"] + " - Channel\n"+ m.json()["cpu"] + " - CPU\n" + m.json()["ram"] + " - RAM\n" + m.json()["botUptime"] + " - Bot-Uptime\n" + m.json()["ping"] + " - Ping")
    if debug == "true":
        print("Stats executed")
        print(m.text)

def credits():
    tkinter.messagebox.showinfo(botname,'Bot by rexjohannes98 and f1nniboy')
    if debug == "true":
        print("Credits executed")


def youtube():
    m = requests.get(apiurl + "play?session=" + session.get() + "&search=" + yt2.get())
    tkinter.messagebox.showinfo(botname, m.json()["title"])
    if debug == "true":
        print("Executed YouTube")
        print(m.text)

def dmnp():
    m = requests.get(apiurl + "notifications?session=" + session.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed DM NP")
        print(m.text)


def stream():
    m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=" + yt.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed Stream")
        print(m.text)


def skip():
    m = requests.get(apiurl + "playlist?session=" + session.get() + "&task=skip")
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed Skip")
        print(m.text)

def shuffle():
    m = requests.get(apiurl + "playlist?session=" + session.get() + "&task=shuffle")
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed shuffle")
        print(m.text)

def clearplaylist():
    m = requests.get(apiurl + "playlist?task=clear&session=" + session.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed clear")
        print(m.text)

def playl():
    try:
        m = requests.get(apiurl + "playlist?task=list&session=" + session.get())
        videos = ""
        for video in m.json()["videos"]:
            videos += video["title"] + "\n"
        tkinter.messagebox.showinfo(botname, videos)
    except:
        tkinter.messagebox.showinfo(botname, "An unknown error occurred")


def website():
    webbrowser.open(botwebsite)

def statuus():
    webbrowser.open(status)

def changelog():
    try:
        m = requests.get(botwebsite + "changelog.txt")
        tkinter.messagebox.showinfo(botname, m.text)
    except:
        tkinter.messagebox.showinfo(botname, "An unknown error occurred")

def login():
    webbrowser.open(apiurl + "login")

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
                   text="Skip",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=skip,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Pause",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=pause,
                   fg="black").pack()

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

    root3.mainloop()



tkinter.Button(root,
    text="Login",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    background=bcolor,
    command=login,
    fg="black").pack()

label333 = tkinter.Label(root,
                         text="Session",
width=20,
                      background=color)
session = tkinter.Entry(root,
                        fg="black")

try:
    session.insert(1, F.read())
except:
    session.insert(1,"")
label333.pack()
session.pack()

def radios():
    root3 = tkinter.Tk()
    root3.title(botname)
    root3.configure(background=color)

    def rexradio():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=https://stream.laut.fm/rexradio")
        tkinter.messagebox.showinfo(botname, m.json()["response"])

    def iloveradio():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=https://streams.ilovemusic.de/iloveradio1.mp3")
        tkinter.messagebox.showinfo(botname, m.json()["response"])

    def ilove2dance():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=https://streams.ilovemusic.de/iloveradio2.mp3")
        tkinter.messagebox.showinfo(botname, m.json()["response"])

    def ilovemashup():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=https://streams.ilovemusic.de/iloveradio5.mp3")
        tkinter.messagebox.showinfo(botname, m.json()["response"])

    def reyfm():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=https://reyfm-stream04.radiohost.de/reyfm-original_mp3-320")
        tkinter.messagebox.showinfo(botname, m.json()["response"])

    def zoneradio():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=https://stream01.zoneradio.de/zoneradio_hq")
        tkinter.messagebox.showinfo(botname, m.json()["response"])

    def mashupfm():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=https://stream.laut.fm/mashupfm")
        tkinter.messagebox.showinfo(botname, m.json()["response"])

    def rtl():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=http://stream.89.0rtl.de/live/mp3-128/direktlinkHP/")
        tkinter.messagebox.showinfo(botname, m.json()["response"])

    def cyt():
        m = requests.get(apiurl + "stream?session=" + session.get() + "&stream=http://stream.laut.fm/cytradio")
        tkinter.messagebox.showinfo(botname, m.json()["response"])


    tkinter.Label(root3,
                  text="""Radios:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    tkinter.Button(root3,
                   text="RexRadio",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=rexradio,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="ILoveRadio",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=iloveradio,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="ILove2Dance",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=ilove2dance,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="ILoveMashup",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=ilovemashup,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="ReyFM",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=reyfm,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="ZoneRadio",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=zoneradio,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="MashupFM",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=mashupfm,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="89.0 RTL",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=rtl,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="CytRadio",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=cyt,
                   fg="black").pack()

    root3.mainloop()


#def radios():

#    root2 = tkinter.Tk()
#    root2.title(botname)
#    root2.configure(background=color)

#    v = tkinter.IntVar()
#    v.set(0)

#    languages = [
#        ("RexRadio:", 0),
#        ("ILoveRadio:", 1),
#        ("ILove2Dance:", 2),
#        ("ILoveMashup:", 3),
#        ("ReyFM:", 4),
#        ("ZoneRadio:", 5),
#        ("MashupFM:", 6),
#        ("89RTL:", 7),
#        ("CytRadio:", 8)
#    ]

#    def ShowChoice():
#        i = v.get()
#        if i == 0:
#            m = requests.get(
#                apiurl + "stream&session=" + session.get() + "&stream=https://stream.laut.fm/rexradio")
#            tkinter.messagebox.showinfo(botname, m.json()["response"])
#        if i == 1:
#            m = requests.get(
#                apiurl + "stream&session=" + session.get() + "&stream=https://streams.ilovemusic.de/iloveradio1.mp3")
 #           tkinter.messagebox.showinfo(botname, m.json()["response"])
#        if i == 2:
#            m = requests.get(
#                apiurl + "stream&session=" + session.get() + "&stream=https://streams.ilovemusic.de/iloveradio2.mp3")
#            tkinter.messagebox.showinfo(botname, m.json()["response"])
#        if i == 3:
#            m = requests.get(
#                apiurl + "stream&session=" + session.get() + "&stream=https://streams.ilovemusic.de/iloveradio5.mp3")
#            tkinter.messagebox.showinfo(botname, m.json()["response"])
#        if i == 4:
#            m = requests.get(
#                apiurl + "stream&session=" + session.get() + "&stream=https://reyfm-stream04.radiohost.de/reyfm-original_mp3-320")
#            tkinter.messagebox.showinfo(botname, m.json()["response"])
#        if i == 5:
#            m = requests.get(
#                apiurl + "stream&session=" + session.get() + "&stream=https://stream01.zoneradio.de/zoneradio_hq")
#            tkinter.messagebox.showinfo(botname, m.json()["response"])
#        if i == 6:
#            m = requests.get(
#                apiurl + "stream&session=" + session.get() + "&stream=https://stream.laut.fm/mashupfm")
#            tkinter.messagebox.showinfo(botname, m.json()["response"])
#        if i == 7:
#            m = requests.get(
#                apiurl + "stream&session=" + session.get() + "&stream=http://stream.89.0rtl.de/live/mp3-128/direktlinkHP/")
#            tkinter.messagebox.showinfo(botname, m.json()["response"])
#        if i == 8:
#            m = requests.get(
#                apiurl + "radio&session=" + session.get() + "&stream=http://stream.laut.fm/cytradio")
#            tkinter.messagebox.showinfo(botname, m.json()["response"])

 #       if debug == "true":
#            print("Playing...")
#            print(i)

#    tkinter.Label(root2,
#                  text="""Choose your Radio:""",
#                  justify=tkinter.LEFT,
#                  background=bcolor,
#                  padx=20).pack()

 #   for val, language in enumerate(languages):
#        tkinter.Radiobutton(root2,
#                            text=language,
#                            padx=20,
#                            variable=v,
#                            command=ShowChoice,
#                            bg=color,
#                            fg="black",
#                            value=val).pack(anchor=tkinter.W)




 #   root2.mainloop()

def moreinfo():
    root3 = tkinter.Tk()
    root3.title(botname)
    root3.configure(background=color)

    tkinter.Label(root3,
                  text="""Misc""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    tkinter.Button(root3,
                   text="Contact",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=feedback,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Stats",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=other,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Credits",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=credits,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Website",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=website,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Changelog",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=changelog,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="DM NP",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=dmnp,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Status",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=statuus,
                   fg="black").pack()



def ytplaylist():
    m = requests.get(apiurl + "playlist?session=" + session.get() + "&task=youtube&id=" + yt3.get())
    requests.get(apiurl + "volume?session=" + session.get() + "&volume=" + vol.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print(m.text)

def pause():
    m = requests.get(apiurl + "pause?session=" + session.get())
    tkinter.messagebox.showinfo(botname, m.json()["respone"])
    if debug == "true":
        print(m.text)

def charts():
    m = requests.get(apiurl + "playlist?session=" + session.get() + "&task=youtube&id=PLxhnpe8pN3TmtjcQM7zcYAKhQXPdOHS3Y")
    requests.get(apiurl + "volume?session=" + session.get() + "&volume=" + vol.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print(m.text)

def spotify():
    m = requests.get(apiurl + "playlist?task=spotify&id=" + sp.get() + "&session=" + session.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print(m.text)


def ncspl():
    m = requests.get(apiurl + "playlist?session=" + session.get() + "&task=youtube?id=PLRBp0Fe2GpglvwYma4hf0fJy0sWaNY_CL")
    requests.get(apiurl + "volume&session=" + session.get() + "&volume=" + vol.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print(m.text)

def edmm():
    m = requests.get(apiurl + "playlist?session=" + session.get() + "&task=youtube&id=PLiD_zu1g02Hi748eJrWnkE-6LhKxOFQz6")
    requests.get(apiurl + "volume?session=" + session.get() + "&volume=" + vol.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print(m.text)

def lists():
    root3 = tkinter.Tk()
    root3.title(botname)
    root3.configure(background=color)

    tkinter.Label(root3,
                  text="""Playlists:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    tkinter.Button(root3,
                   text="Charts",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=charts,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="NCS",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=ncspl,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="EDM Mashup",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=edmm,
                   fg="black").pack()

    root3.mainloop()

def feedback():
    root3 = tkinter.Tk()
    root3.title(botname)
    root3.configure(background=color)

    tkinter.Label(root3,
                  text="""Feedback:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    feed = tkinter.Entry(root3)
    feed.insert(1, "I like the Bot")
    feed.pack()


    tkinter.Label(root3,
                  text="""Suggestion:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    sug = tkinter.Entry(root3)
    sug.insert(1, "Add Twitch Support")
    sug.pack()


    tkinter.Label(root3,
                  text="""Bug:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    bug = tkinter.Entry(root3)
    bug.insert(1, "This Windows has no Icon")
    bug.pack()

    def sendfeed():
        m = requests.get(apiurl + "feedback?message=" + feed.get() + "&session=" + session.get())
        tkinter.messagebox.showinfo(botname, m.json()["response"])
        if debug == "true":
            print(m.text)

    def sendsug():
        m = requests.get(apiurl + "suggestions?message=" + sug.get() + "&session=" + session.get())
        tkinter.messagebox.showinfo(botname, m.json()["response"])
        if debug == "true":
            print(m.text)

    def sendbug():
        m = requests.get(apiurl + "bugs?message=" + bug.get() + "&session=" + session.get())
        tkinter.messagebox.showinfo(botname, m.json()["response"])
        if debug == "true":
            print(m.text)

    def suppo():
        webbrowser.open(support)



    tkinter.Button(root3,
                   text="Send Feedback",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=sendfeed,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Send Suggestion",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=sendsug,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Send Bug",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=sendbug,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Support Server",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=suppo,
                   fg="black").pack()

    root3.mainloop()


tkinter.Label(root,
              text="Unique-Music",
              background=color,
              padx=15).pack()

tkinter.Button(root,
               text="YouTube",
               width=20,
               justify=tkinter.RIGHT,
               height=1,
               bg=bcolor,
               command=youtube,
               fg="black").pack()

#tkinter.Button(root,
#               text="Radio",
#               width=20,
#               justify=tkinter.RIGHT,
#               height=1,
#               bg=bcolor,
#               command=radios,
#               fg="black").pack()

def addmore():
    root3 = tkinter.Tk()
    root3.title(botname)
    root3.configure(background=color)

    tkinter.Label(root3,
                  text="""Players:""",
                  justify=tkinter.LEFT,
                  background=color,
                  padx=20).pack()

    tkinter.Button(root3,
                   text="Stream",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=stream,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Radios",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=radios,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="YouTubePlaylist",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=ytplaylist,
                   fg="black").pack()

    tkinter.Button(root3,
                   text="Spotify",
                   width=20,
                   justify=tkinter.RIGHT,
                   height=1,
                   bg=bcolor,
                   command=spotify,
                   fg="black").pack()

    root3.mainloop()


tkinter.Button(root,
               text="More",
               width=20,
               justify=tkinter.RIGHT,
               height=1,
               bg=bcolor,
               command=addmore,
               fg="black").pack()


vollabel = tkinter.Label(root,
                         text="Volume",
                      background=color)
vol = tkinter.Entry(root)
vol.insert(1, "30")
vollabel.pack()
vol.pack()


label2 = tkinter.Label(root,
                       text="Stream Link",
                      background=color)
yt = tkinter.Entry(root)
yt.insert(1, "https://reyfm-stream04.radiohost.de/reyfm-original_mp3-320")
label2.pack()
yt.pack()

label5 = tkinter.Label(root,
                       text="YouTube",
                      background=color)
yt2 = tkinter.Entry(root)
yt2.insert(1, "NCS Polka")
label5.pack()
yt2.pack()

label10 = tkinter.Label(root,
                        text="YouTube Playlist",
                      background=color)
yt3 = tkinter.Entry(root)
yt3.insert(1, "https://www.youtube.com/playlist?list=PLiD_zu1g02Hi748eJrWnkE-6LhKxOFQz6")
label10.pack()
yt3.pack()

label12 = tkinter.Label(root,
                        text="Spotify",
                      background=color)
sp = tkinter.Entry(root)
sp.insert(1, "2lfAwrTGw2rbXLJf7elpo9")
label12.pack()
sp.pack()


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
               text="Stop",
               width=20,
               justify=tkinter.RIGHT,
               height=1,
               bg=bcolor,
               command=onlystop,
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

#tkinter.Button(root,
#    text="Lyrics",
#    width=20,
#    justify=tkinter.RIGHT,
#    height=1,
#    bg="#cf2dc1",
#    command=,
#    fg="black").pack()



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
    text="More",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=moreinfo,
    fg="black").pack()

tkinter.Button(root,
    text="Invite Me!",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg=bcolor,
    command=open,
    fg="black").pack()

if vers == 5:
    pass

else:
    m = tkinter.messagebox.askokcancel(botname, "Did you want to Download the latest Version?")
    if m == True:
        webbrowser.open(download)

if debug == "true":
    print(vers)


root.mainloop()
