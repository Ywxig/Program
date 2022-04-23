import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
import webbrowser as wb
import os
import random


class randomSimbol():
        
        def SibNoD():
                r = random.randint(0, 2)
                sibol = [' + ', ' - ', ' * ']          
                return str(sibol[r])
        
        def Sib():
                r = random.randint(0, 3)
                sibol = [' + ', ' - ', ' * ', ' / ']          
                return str(sibol[r])

