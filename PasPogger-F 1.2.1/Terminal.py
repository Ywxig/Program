import tkinter
from tkinter import tix
from tkinter.constants import *
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
import CONFIG
import ComsolDrow

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

ButtonColorBG = opttinList[22]
ButtonColorFG = opttinList[23]

CanvasBG = opttinList[24]

class Info:

    def WriteInfoSoftware():
        info = 'Software version 1.2 \n A program for working with the Pascal programming language! created to help you learn and speed up writing low-level code!' 
        return info

    def WriteInfoDevoloper():
        info = 'Program created \n "A student for students!" designed by Dmitry Zimnov\n discord:Ywxig#8564\n email: d.zimnov@gmail.com' 
        return info

class Write:

    def TextForFile(text, FailName):
        Ret = FailName + ' | ' + text
        return Ret

    class Logs:

        def ErrorLog(FailName, TapeError):
            if TapeError == 'Sintacsis':
                TextError = 'Syntacsis there is a SYNTAX ERROR in YOUR CODE!'

            if TapeError == 'Name':
                TextError = 'Name there is a NAME ERROR in YOUR CODE!'

            if TapeError == 'Save':
                TextError = 'Name there is a Save ERROR in YOUR CODE!'

            Ret = "[!ERROR!]" + FailName + ' | Error in your code! ' + TextError
            return Ret            

        def SucsessLog(FailName, TapeSucecss):
            if TapeSucecss == 'Save':
                TextError = 'Success! Save'

            if TapeSucecss == 'Opiraton':
                TextError = 'Success! Opiraton'

            Ret = "[!SUCESS!]" + FailName + ' | ' + TextError
            return Ret 


program_l = []
c = ''

def Main():

    def CP(event):
        Gen('r')
    #Создали окно root!
    term = tkinter.Tk()
    term.title("terminal 1.1")
    term[ 'bg' ] = MainBG
    term.geometry('270x460')
    term.iconbitmap(TerminalIco)

    termtext = tkinter.Text(term, width=400, height=400, wrap="word", bg=MainTextBG, fg=MainTextFG, font=Font)
    termtext.pack()

    termtext.bind('<space>', CP) 

    def Gen(_format):
        #file = open('TOKENHUB.token', _format)
        if _format == 'r':
                global c
                global program_l
                fin = termtext.get('1.0' ,END)
                s_f = fin.split('\n')
                b_f = fin.split('.')
                n = -1
                for i in s_f:
                        n = n + 1
                        st = str(s_f[n])
                        block = st.split('.')
                        #print(block)

                        if block[0] == 'begin':
                                p = 'begin'
                                program_l.append(p)
                                print(program_l)

                        if block[0] == 'name':
                                name = block[1]
                                p = 'Program ' + name + ';'
                                program_l.append(p)
                                print(program_l)

                        if block[0] == 'read':
                                Sap = block[1]
                                Sap_l = Sap.split(',')
                                vv = ', '.join(Sap_l)
                                p = "readln(" + Sap + ");"    
                                program_l.append(p)
                                print(program_l)

                        if block[0] == 'print':
                                Sap = block[1]
                                p = "writeln(" + Sap + ");"    
                                program_l.append(p)
                                print(program_l)

                        if block[0] == 'math':
                                Sap = block[1]
                                
                                if Sap == 'Dis':
                                        p = 'rezalt := sqr(a) - 4 * a * c;'
                                else:
                                        p = 'rezalt:=' + Sap + ';'    
                                program_l.append(p)
                                print(program_l)
                                
                        if block[0] == 'var':
                                
                                varable = block[1]
                                tup = block[2]
                                var_l = varable.split(',')
                                vv = ', '.join(var_l)
                                
                                if tup == 'str':
                                        v = 'string'
                                        
                                if tup == 'int':
                                        v = 'integer'
                                        
                                if tup == 'float':
                                        v = 'real'
                                                
                                p = 'var ' + vv + ' : ' + v + ';\n      rezalt : real;'    
                                program_l.append(p)
                                print(program_l)
                                
                        if block[0] == 'avar':
                                        varable = block[1]
                                        tup = block[2]
                                        var_l = varable.split(',')
                                        vv = ', '.join(var_l)

                                        if tup == 'str':
                                                v = 'string'
                                        
                                        if tup == 'int':
                                                v = 'integer'
                                        
                                        if tup == 'float':
                                                v = 'real'
                                        
                                        p = '      ' + vv + ' : ' + v + ';'
                                        program_l.append(p)
                                        print(program_l)                                
                
                        
                        if block[0] == 'cls':
                                termtext.delete('1.0', tkinter.END)

                        if block[0] == 'clear':
                                program_l = []

                        if block[0] == 'ReadMe':
                                typ = block[1]
                                name = block[2]
                                css = block[3]                         
                                if typ == 'html':                                        
                                        if css == 'PythonDoc':
                                                cc = "h1{    font-family: 'Lucida Grande', Arial, sans-serif;\n    background-color: white;\n    font-weight: normal;\n    color: #1a1a1a;\n    margin: 0;\n    border: 0;\n    padding: 0.3em 0;\n    font-size: 1.625rem;}\np {    font-family: 'Lucida Grande', Arial, sans-serif;\n    color: #222222;\n    font-size: 0.875rem;\n    hyphens: auto;\n    text-align: left;\n    line-height: 1.4;}\na {    font-family: 'Lucida Grande', Arial, sans-serif;\n    text-align: left !important;\n    hyphens: auto;\n    line-height: 150%;\n    text-decoration: none;\n    font-size: 1.3em;\n    color: #0072aa;}\nb {    font-family: 'Lucida Grande', Arial, sans-serif;\n    color: #222222;\n    font-size: 0.875rem;\n    hyphens: auto;    text-align: left;\n    line-height: 1.4;}\ni {font-family: 'Lucida Grande', Arial, sans-serif;\n    color: #222222;\n    text-align: left !important;\n    hyphens: auto;\n    line-height: 150%;\n    font-style: italic;\n    padding-top: 5px;\n    font-size: 90%;}\n"
                                                File = open('ReadMeDir/PythonDoc.css', 'w')
                                                tet = '<!DOCTYPE html>\n<html>\n<head>\n       <title>ReadMe</title>\n<link href="PythonDoc.css" rel="stylesheet" type="text/css"/>\n</head>\n<body>\n\n<h1>Welcom to your ReadMe!</h1> \n<p>Insert your text!</p>\n\n</body>\n</html>\n'
                                                File.write(cc)
                                                file = open('ReadMeDir/' + name + '.html', 'w')
                                                file.write(tet)
                                                termtext.delete('1.0', tkinter.END)

                        if block[0] == 'Code':
                                name = block[1]
                                file = open('Progarmm/' + str(name) + '.txt', 'r')
                                c = file.read()
                                print(c)
                                program_l = []
                                program_l.append(str(c))

                        if block[0] == 'Print':
                                txt = block[1]
                                c = "Program P1;\nvar a, b, c, rezalt : real;\nbegin\n\n\nwriteln('" +  txt +  "');\n\nend.\n"                              

                        if block[0] == 'MathSample':
                                Var = block[1]
                                Sample = block[2]
                                c = "Program P1;\nvar " + str(Var) + ",rezalt : real;\nbegin\n\n\nwriteln('Введите деситичьные числа a, b, c: ');\nreadln(a, b, c);\nrezalt := " +  str(Sample) +  ";\nwriteln('Ответ = ', rezalt);\n\nend.\n"
                                return c

                        if block[0] == 'Drow':
                                Sip = block[1]

                                if Sip == 'Feet':
                                        case = block[3]
                                        size = block[2]
                                        txt = ComsolDrow.Drow.Feet(int(size), case, ' ')
                                        c = "Program P1;\n\nbegin\n\n\n" +  txt +  "\n\nend.\n"
                                        return c
                                
                                if Sip == 'Spurce':
                                        case = block[3]
                                        size = block[2]
                                        txt = ComsolDrow.Drow.Spruce(int(size), case, ' ')
                                        c = "Program P1;\n\nbegin\n\n\n" +  txt +  "\n\nend.\n"
                                        return c
                file = open('Buff.bup', 'w')
                p = '\n'.join(program_l)
                file.write(str(p))
