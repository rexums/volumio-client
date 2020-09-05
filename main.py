import tkinter
import requests
import webbrowser
import tkinter.messagebox
import sys
import json


debug = "false"

url = 'https://discord.com/oauth2/authorize?client_id=665854713845121025&permissions=8&scope=bot'
color = "#9e6cf5"
apiurl = "http://admin.rexjohannes.ovh:3000/"
botname = "Unique-Music"

root = tkinter.Tk()
root.title(botname)
root.iconphoto(False, tkinter.PhotoImage(file='icon.png'))
root.configure(background=color)


v = tkinter.IntVar()
v.set(0)

languages = [
    ("RexRadio:",0),
    ("ILoveRadio:", 1),
    ("ILove2Dance:",2),
    ("ILoveMashup:",3),
    ("ReyFM:",4),
    ("ZoneRadio:",5),
    ("MashupFM:", 6),
    ("89RTL:", 7)
#    ("Stream:", 8),
#    ("YouTube:", 9)
]

def open():
    webbrowser.open(url)
    if debug == "true":
        print("Invite Me! executed")

def exiting():
    sys.exit()

def onlystop():
    m = requests.get(apiurl + "?action=leave&channel=" + channelid.get())
    tkinter.messagebox.showinfo(botname,m.json()["response"])
    if debug == "true":
        print("Stop executed")
        print(m.text)

def volume():
    m = requests.get(apiurl + "?action=volume&channel=" + channelid.get() + "&volume=" + vol.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Volume executed")
        print(m.text)

def np():
    m =requests.get(apiurl + "?action=status&channel=" + channelid.get())
    tkinter.messagebox.showinfo(botname, m.json()["title"])
    if debug == "true":
        print("Now Playing executed")
        print(m.text)

def other():
    tkinter.messagebox.showinfo(botname,'Bot by rexjohannes98 and f1nniboy')
    m = requests.get(apiurl + "?action=stats")
    tkinter.messagebox.showinfo(botname,m.json()["guilds"] + " - Server\n" + m.json()["users"] + " - User\n" + m.json()["channels"] + " - Channel")
    if debug == "true":
        print("Stats and Credits executed")
        print(m.text)

def youtube():
    m = requests.get(apiurl + "?action=play&channel=" + channelid.get() + "&search=" + yt2.get())
    tkinter.messagebox.showinfo(botname, m.json()["title"])
    if debug == "true":
        print("Executed YouTube")
        print(m.text)

def stream():
    m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=" + yt.get())
    tkinter.messagebox.showinfo(botname, m.json()["response"])
    if debug == "true":
        print("Executed Stream")
        print(m.text)



def radios():
    root2 = tkinter.Tk()
    root2.title(botname)
    root2.configure(background=color)
    root.iconphoto(False, tkinter.PhotoImage(file='icon.png'))

    tkinter.Label(root2,
                  text="""Choose your Radio:""",
                  justify=tkinter.LEFT,
                  background="#cf2dc1",
                  padx=20).pack()

    for val, language in enumerate(languages):
        tkinter.Radiobutton(root2,
                            text=language,
                            padx=20,
                            variable=v,
                            command=ShowChoice,
                            bg=color,
                            fg="black",
                            value=val).pack(anchor=tkinter.W)

    root2.mainloop()


def ShowChoice():
    i = v.get()
    if i == 0:
        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=https://stream.laut.fm/rexradio")
        tkinter.messagebox.showinfo(botname, m.json()["response"])
    if i == 1:
        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=https://streams.ilovemusic.de/iloveradio1.mp3")
        tkinter.messagebox.showinfo(botname, m.json()["response"])
    if i == 2:
        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=https://streams.ilovemusic.de/iloveradio2.mp3")
        tkinter.messagebox.showinfo(botname, m.json()["response"])
    if i == 3:
        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=https://streams.ilovemusic.de/iloveradio5.mp3")
        tkinter.messagebox.showinfo(botname, m.json()["response"])
    if i == 4:
        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=https://reyfm-stream04.radiohost.de/reyfm-original_mp3-320")
        tkinter.messagebox.showinfo(botname, m.json()["response"])
    if i == 5:
        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=https://stream01.zoneradio.de/zoneradio_hq")
        tkinter.messagebox.showinfo(botname, m.json()["response"])
    if i == 6:
        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=https://stream.laut.fm/mashupfm")
        tkinter.messagebox.showinfo(botname, m.json()["response"])
    if i == 7:
        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=http://stream.89.0rtl.de/live/mp3-128/direktlinkHP/")
        tkinter.messagebox.showinfo(botname, m.json()["response"])
#    if i == 8:
#        m = requests.get(apiurl + "?action=radio&channel=" + channelid.get() + "&stream=" + yt.get())
#        tkinter.messagebox.showinfo(botname, m.json()["response"])
#    if i == 9:
#        m = requests.get(apiurl + "?action=play&channel=" + channelid.get() + "&search=" + yt2.get())
#        tkinter.messagebox.showinfo(botname, m.json()["title"])

    if debug == "true":
        print("Playing...")
        print(i)

label13 = tkinter.Label(text="Unique-Music",
                      background=color,
                      padx=15)
label13.pack()

tkinter.Button(root,
    text="Radios",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=radios,
    fg="black").pack()

tkinter.Button(root,
    text="Stream",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=stream,
    fg="black").pack()

tkinter.Button(root,
    text="YouTube",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=youtube,
    fg="black").pack()

label = tkinter.Label(text="ChannelID",
                      background=color)
channelid = tkinter.Entry()
channelid.insert(1, "637374099471204353")
label.pack()
channelid.pack()



vollabel = tkinter.Label(text="Volume",
                      background=color)
vol = tkinter.Entry()
vol.insert(1, "30")
vollabel.pack()
vol.pack()



#tkinter.Label(root,
#         text="""Choose your Radio:""",
#         justify = tkinter.LEFT,
#         background="#cf2dc1",
#         padx = 20).pack()

#for val, language in enumerate(languages):
#    tkinter.Radiobutton(root,
#                  text=language,
#                  padx = 20,
#                  variable=v,
#                  command=ShowChoice,
#                  bg=color,
#                  fg="black",
#                  value=val).pack(anchor=tkinter.W)


label2 = tkinter.Label(text="Stream Link",
                      background=color)
yt = tkinter.Entry()
yt.insert(1, "https://reyfm-stream04.radiohost.de/reyfm-original_mp3-320")
label2.pack()
yt.pack()

label5 = tkinter.Label(text="YouTube",
                      background=color)
yt2 = tkinter.Entry()
yt2.insert(1, "NCS Polka")
label5.pack()
yt2.pack()

label23 = tkinter.Label(text="Control",
                      background=color,
                      padx=50)
label23.pack()

tkinter.Button(root,
    text="Volume",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=volume,
    fg="black").pack()

tkinter.Button(root,
    text="Now Playing",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=np,
    fg="black").pack()

label22 = tkinter.Label(text="Misc",
                      background=color,
                      padx=60)
label22.pack()


tkinter.Button(root,
    text="Stop",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=onlystop,
    fg="black").pack()


tkinter.Button(root,
    text="Exit",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=exiting,
    fg="black").pack()


tkinter.Button(root,
    text="Stats + Credits",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=other,
    fg="black").pack()

tkinter.Button(root,
    text="Invite Me!",
    width=20,
    justify=tkinter.RIGHT,
    height=1,
    bg="#cf2dc1",
    command=open,
    fg="black").pack()


root.mainloop()