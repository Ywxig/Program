#Command

import tkinter
from tkinter import tix
from tkinter.constants import *
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
file = open('opt.txt', 'r')

option = file.read()
opttinList = option.split('/')

MainBG = opttinList[0]
MainTextBG = opttinList[1]
MainTextFG = opttinList[2]
Font = opttinList[3]
MainSize = opttinList[4]
InfoSize = opttinList[5]
MainIco = opttinList[6]
ShowTerminol = opttinList[7]
ShowTerminolOnCanvas = opttinList[8]
ShowButton = opttinList[9]
NAME_PROGRAM = opttinList[10]
NAME_INFO_WIN = opttinList[11]

KeyWord = opttinList[12]
LogikKeyWord = opttinList[13]
Sigle = opttinList[14]
Double = opttinList[15]
VarLight = opttinList[16]

GenCase = opttinList[17]
GenHtml = opttinList[18]

TerminalIco = opttinList[19]
TerminaTextBG = opttinList[20]
TerminaTextFG = opttinList[21]

class IntCommand:
    def SUMM():
        COM1 = tkinter.Tk()
        COM1.title("=Summ")
        COM1[ 'bg' ] = MainBG
        COM1.geometry('250x90')
        COM1.iconbitmap(MainIco)

        a = Entry(COM1)
        a.place(x=0, y=0)

        b = Entry(COM1)
        b.place(x=0, y=25)

        Acept = Button(COM1, text='Принять', command=IntCommand.SUMM)
        Acept.place(x=0, y=50)

        mainloop()

IntCommand.SUMM()     