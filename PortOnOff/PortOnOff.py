from tkinter import *
import tkinter
import os
import subprocess
import requests

def openPort():
    os.system("""netsh advfirewall firewall set rule name="block ftg connection" new enable=no""")
    labelStatus.config( text = "port OPEN", bg = "lightgreen")

def closePort():
    os.system("""netsh advfirewall firewall set rule name="block ftg connection" new enable=yes""")
    labelStatus.config (text = "port CLOSED", bg = "red")

def startNew():
    subprocess.Popen(r"""start C:\Users\akims.parahins\FtgRestTest\server_xe10_3\ftgserver.exe -f -aftgwin -cftg20db.ini """, shell=True)



def openAndClose(r, entry, start = False):
    try:
        time = int(entry.get())
    except:
        entry.delete(0, len(entry.get()))
        entry.insert(0, "NaN")
        return

    openPort()
    if (start):
        startNew()
    r.after(time, closePort)
    


r = Tk() 
r.title('1323') 


requestNum = IntVar(r, value = 0)

labelStatus = Label(r, text= "port status unknown")
labelStatus.grid(row = 0, column = 0)

buttonOpen = Button(r, text='Open', width=25, command=openPort)
buttonClose = Button(r, text='Close', width=25, command=closePort)
buttonStart = Button(r, text = 'Start new', width=25, command=startNew)

buttonOpen.grid(row = 1, column = 0) 
buttonClose.grid(row = 2, column = 0) 
buttonStart.grid(row = 3, column = 0) 

#start and close
entryStartAndCloseAfter = Entry(r)
buttonStartAndClose = Button(r, text = "Start and close after", width = 25, command = lambda: openAndClose(r, entryStartAndCloseAfter, start = True))
entryStartAndCloseAfter.grid(row = 4, column = 1)
buttonStartAndClose.grid(row = 4, column = 0)

#open and close
entryOpenAndCloseAfter = Entry(r)
buttonOpenAndClose = Button(r, text = "Open and close after", width = 25, command = lambda: openAndClose(r, entryOpenAndCloseAfter))
entryOpenAndCloseAfter.grid(row = 5, column = 1)
buttonOpenAndClose.grid(row = 5, column = 0)


r.mainloop() 
