import tkinter
import urllib

def updateCheck(self):
    update = False

    updateWindow = Tkinter.Toplevel()
    updateWindow.title(string="Update Checker")
    updateWindow.resizable(False, False)

    #Gets downloaded version
    versionSource = open('version.txt', 'r')
    versionContents = versionSource.read()

    #gets newest version
    updateSource = urllib.urlopen("http://www.suturesoft.com/Updates/craftbook.txt")
    updateContents = updateSource.read()

    #checks for updates
    for i in range(0,20):
        if updateContents[i] != versionContents[i]:
            dataLabel = Tkinter.Label(updateWindow,text="\n\nThere are data updates availible.\n\n")
            dataLabel.pack()
            update = True
            break
    for i in range(22,42):
        if updateContents[i] != versionContents[i]:
            versionLabel = Tkinter.Label(updateWindow,text="\n\nThere are version updates availible.\n\n")
            versionLabel.pack()
            update = True
            break
    if update == False:
        versionLabel = Tkinter.Label(updateWindow,text="\n\nYou are already running the most up to date version.\n\n")
        versionLabel.pack()