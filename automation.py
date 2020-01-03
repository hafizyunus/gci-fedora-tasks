import os
from tkinter import *
from tkinter import ttk
import webbrowser

class task:
    def __init__(self, master):
        master.title('Tasks')

        style = ttk.Style(mainWin)
        style.configure("TButton", font=('wasy10', 20), padding=10)

        # ***** Frame *****

        self.mainFrame = Frame(master, width=500, height=500)
        self.mainFrame.grid(row=0,column=0)

        # ***** Stuff in Frame *****

        self.twitter = ttk.Button(self.mainFrame, text='Open Twitter', style='TButton' ,command=self.openTwitter)
        self.twitter.grid(row=1, column=1, pady=10)

        self.spotify = ttk.Button(self.mainFrame, text='Open Spotify', style='TButton' ,command=self.openSpotify)
        self.spotify.grid(row=2, column=1, pady=10)

        self.github = ttk.Button(self.mainFrame, text='Open GitHub', style='TButton' ,command=self.openGithub)
        self.github.grid(row=3, column=1, pady=10)

        self.exit = ttk.Button(self.mainFrame, text='Exit', style='TButton', command=master.destroy)
        self.exit.grid(row=4, column=1, pady=10)

        self.lSpace = Label(self.mainFrame, width=14, height=2)
        self.lSpace.grid(row=0, column=0)

    def openTwitter(self):
        webbrowser.open('https://twitter.com/home')

    def openSpotify(self):
        os.startfile(r'C:\Users\hafiz\Desktop\Spotify.lnk')

    def openGithub(self):
        webbrowser.open('https://github.com/')

mainWin = Tk()
mainWin.resizable(False,False)
mainWin.maxsize(400,400)
mainWin.minsize(400,400)
app = task(mainWin)
mainWin.mainloop()