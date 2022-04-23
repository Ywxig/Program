# Tkinter Bot engen!

from msilib.schema import ComboBox
import tkinter
#from tkinter import _Relief, tix
from tkinter.constants import *
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
import webbrowser as wb
import os
import random
from pygments.lexers import PythonLexer
from pygments.token import Token
import Defain
import ComsolDrow
#import CONFIG
import Terminal

print(Defain.randomSimbol.SibNoD())

lexer = PythonLexer()

def Term():
        Terminal.Main()

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

if ShowTerminol == 'True':
        program_l = []
        c = ''

        def Main():

                def CP(event):
                        Gen('r')
                #Создали окно root!
                term = tkinter.Tk()
                term.title("terminal 1.2")
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
                                b_f = fin.split(':')
                                n = -1
                                for i in s_f:
                                        n = n + 1
                                        st = str(s_f[n])
                                        block = st.split(':')
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

                                        if block[0] == 'const':
                                                name = block[1]
                                                varable = block[1]
                                                p = str(name + ' = ' +  varable)
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
                                                p = '\n'.join(program_l)
                                                text.insert('1.0', c)


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
        Main()



File = open('UserData.txt', 'r')
UserName = File.read()


#Создали окно root!
root = tkinter.Tk()
root.title("PasPogger 1.2.1 -" + NAME_PROGRAM)
root[ 'bg' ] = MainBG
root.geometry(MainSize)
root.iconbitmap(MainIco)
cRoot = Canvas(root, background='#9000d3' ,width=2125, height=20, highlightthickness=0)
cRoot.pack(side=BOTTOM)

lang = Label(cRoot, text='Pascal', background='#9000d3', foreground='#ffffff')
lang.place(x=0, y=0)

User = Label(cRoot, text=UserName, background='#9000d3', foreground='#ffffff')
User.place(x=50, y=0)

if ShowButton == 'True':

        class Save:

                def export():
                        data = text.get('1.0', tkinter.END)
                        text_l = data.split()
                        if text_l[0] != 'Program':
                                wraitdata = 'Program Pn;\n' + data + '\n\nend.'
                                File = open('Progarmm\P.txt', 'w')
                                File.write(wraitdata)

                        else:
                                wraitdata = data
                                
                                File = open('Progarmm\P.txt', 'w')
                                File.write(wraitdata)

                def readme_txt():
                        data = text.get('1.0', tkinter.END)
                        out = asksaveasfile(mode='w', defaultextension='txt')
                        out.write(data)
                        out.close()
                def save_pas_flat(event):
                        data = text.get('1.0', tkinter.END)
                        text_l = data.split()
                        if text_l[0] != 'Program':
                                wraitdata = 'Program Pn;\n' + data + '\n\nend.'
                                out = asksaveasfile(mode='w', defaultextension='pas')
                                out.write(wraitdata)
                                out.close()
                        else:
                                pass
                def save_pas():
                        data = text.get('1.0', tkinter.END)
                        out = asksaveasfile(mode='w', defaultextension='pas')
                        out.write(data)
                        out.close()

                def readme_html():
                        data = text.get('1.0', tkinter.END)
                #file = open('TOKENHUB.token', _format)

                                        
                        out = asksaveasfile(mode='w', defaultextension='html')
                        out.write(data)
                        out.close()

        def clear():
                global t
                t = text.get('1.0', tkinter.END)
                text.delete('1.0', tkinter.END)

        def open_file():
                global FILE_NAME
                inp = askopenfile(mode="r")
                if inp is None:
                        return
                FILE_NAME = inp.name
                data = inp.read()
                text.delete('1.0', tkinter.END)
                text.insert('1.0', data)

        def search(task):      
                wb.open('https://yandex.ru/yandsearch?clid=202826&text={}'.format(task))
                
        def searc2():
                ie = CommboSearch.get()
                print(ie)
                search(ie)
                F = open('History.txt', 'a')
                F.write('/' + ie)

        FILE = open('History.txt', 'r')
        History = FILE.read()
        History_l = History.split('/')

        def printt2():
                file = open('Buff.bup', 'r')
                program = file.read()
                print('\n\n\n\n\n\n\n\n\n\n' + str(program))
                text.delete('1.0', tkinter.END)
                text.insert('1.0', program)
        

        c = Canvas(root, width=2125, height=50, background=CanvasBG, highlightthickness=0)
        c.pack(side=TOP)

        ButtonOpen = Button(c, relief=FLAT ,background=ButtonColorBG, text='Открыть', foreground=ButtonColorFG, font=Font, command=open_file)
        ButtonOpen.place(x=0, y=0)

        ButtonSave = Button(c,relief=FLAT, background=ButtonColorBG, text='Сохранить', foreground=ButtonColorFG, font=Font, command=Save.save_pas)
        ButtonSave.place(x=70, y=0)

        ButtonClear = Button(c,relief=FLAT, background=ButtonColorBG, text='Очистить', foreground=ButtonColorFG, font=Font, command=clear)
        ButtonClear.place(x=155, y=0)

        CommboSearch = ttk.Combobox(c, background=ButtonColorBG, foreground='#000000', font=Font, values=History_l)
        CommboSearch.place(x=233, y=3)

        ButtonSearch = Button(c,relief=FLAT, background=ButtonColorBG, text='Поиск', foreground=ButtonColorFG, font=Font, command=searc2)
        ButtonSearch.place(x=420, y=0)        

        ButtonPrint = Button(c,relief=FLAT, background=ButtonColorBG, text='Выписать', foreground=ButtonColorFG, font=Font, command=printt2)
        ButtonPrint.place(x=474, y=0)

if ShowTerminolOnCanvas == 'True':
        c = Canvas(root, width=125, height=40000, background=CanvasBG, highlightthickness=0)
        c.pack(side=LEFT)
        text2 = tkinter.Text(c, width=35, height=400, wrap="word", bg=TerminaTextBG, fg=TerminaTextFG, font=Font)
        text2.place(x=0, y=0)
        text2.insert('1.0','>>> Start \n')

        

        def CP(event):
                Gen('r')

        def Gen(_format):
                #file = open('TOKENHUB.token', _format)
                if _format == 'r':
                        
                        global c
                        global program_l
                        fin = text2.get('1.0' ,END)
                        s_f = fin.split('\n')
                        b_f = fin.split(':')
                        n = -1
                        for i in s_f:
                                n = n + 1
                                st = str(s_f[n])
                                block = st.split(':')
                                #print(block)

                                if block[0] == 'begin':
                                        p = 'begin'
                                        program_l.append(p)
                                        print(program_l)

                                if block[0] == 'name':
                                        name = block[1]
                                        p = 'Program P1;'
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

                                if block[0] == 'const':
                                        name = block[1]
                                        const = name.split('=')
                                        N = const[0]
                                        content = const[1]
                                        p = str(N + ' = ' +  content)
                                        program_l.append(p)
                                        print(program_l)

                                if block[0] == 'var':
                                        
                                        varable = block[1]
                                        tup = block[2]
                                        var_l = varable.split(',')
                                        vv = ', '.join(var_l)
                                        
                                        if tup == 'str':
                                                V = 'string'
                                                
                                        if tup == 'int':
                                                V = 'integer'
                                                
                                        if tup == 'float':
                                                V = 'real'
                                                        
                                        p = 'var ' + vv + ' : ' + V + ';\n      rezalt : real;'    
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
                                        text2.delete('1.0', tkinter.END)

                                if block[0] == 'clear':
                                        text.delete('1.0', END)

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
                                                        text2.delete('1.0', tkinter.END)

                                if block[0] == 'Code':
                                        name = block[1]
                                        file = open('Progarmm/' + str(name) + '.txt', 'r')
                                        c = file.read()
                                        print(c)
                                        program_l = []
                                        text.insert('1.0', c)

                                if block[0] == 'Print':
                                        txt = block[1]
                                        c = "Program P1;\nvar a, b, c, rezalt : real;\nbegin\n\n\nwriteln('" +  txt +  "');\n\nend.\n"                              
                                        text.insert('1.0', c)

                                if block[0] == 'MathSample':
                                        Var = block[1]
                                        Sample = block[2]
                                        c = "Program P1;\nvar " + str(Var) + ",rezalt : real;\nbegin\n\n\nwriteln('Введите деситичьные числа a, b, c: ');\nreadln(a, b, c);\nrezalt := " +  str(Sample) +  ";\nwriteln('Ответ = ', rezalt);\n\nend.\n"
                                        text.insert('1.0', c)

                                if block[0] == 'Drow':
                                        Sip = block[1]

                                        if Sip == 'Feet':
                                                case = block[3]
                                                size = block[2]
                                                txt = ComsolDrow.Drow.Feet(int(size), case, ' ')
                                                c = "Program P1;\n\nbegin\n\n\n" +  txt +  "\n\nend.\n"
                                                text.insert('1.0', c)
                                        
                                        if Sip == 'Spurce':
                                                case = block[3]
                                                size = block[2]
                                                txt = ComsolDrow.Drow.Spruce(int(size), case, ' ')
                                                c = "Program P1;\n\nbegin\n\n\n" +  txt +  "\n\nend.\n"
                                                text.insert('1.0', c)
                        text2.insert('1.0','>>> Done \n')

        text2.bind('<space>', CP)

#Создали текстовое поле!
text = tkinter.Text(root, width=400, height=400, wrap="word", bg=MainTextBG, fg=MainTextFG, font=Font)
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)
text.pack()





# Создаем теги с разными свойствами, которые будем присваивать соответствующим типам токенов
text.tag_add('program', "1.0", '1.7')
text.tag_add('vars', "1.0", '1.3')
text.tag_config("keyword", foreground=KeyWord)
text.tag_config("string_literal", foreground='#ae00ff')
text.tag_config("leteral_gray", foreground='#c4ff0e')

def Light():
        key_word = ['Program', 'begin']
        var_end = ['var', 'end']
        gen_case = ['!', '!r', '!d']
        gen_html = ['@', '@s', '@p']
        a = text.get(1.0,END).split()
        f = text.get(1.0,END).split('\n')
        for i in a:

                if i in gen_html:
                        text.tag_add('gen2', "1.0", '1.2')
                        text.tag_config('gen2',foreground=GenHtml)

                if i in gen_case:
                        text.tag_add('gen1', "1.0", '1.2')
                        text.tag_config('gen1',foreground=GenCase)

                if i in var_end:
                        text.tag_add('program', "1.0", '1.3')
                        text.tag_config('program',foreground=KeyWord)

                if i in key_word:
                        text.tag_add('program', "1.0", '1.7')
                        text.tag_config('program',foreground=KeyWord)

def get_text_coord(s: str, i: int):
    """
    Из индекса символа получить "координату" в виде "номер_строки_текста.номер_символа_в_строке"
    """
    for row_number, line in enumerate(s.splitlines(keepends=True), 1):
        if i < len(line):
            return f'{row_number}.{i}'
        
        i -= len(line)


# Прописываем соответствие типа токена тегу подсветки
token_type_to_tag = {
    Token.Literal.String.Single: "program",
    Token.Literal.String.Double: "leteral_gray",
    #Token.Literal.String.Keyword: "keyword",
    #Token.Literal.String.Keyword: "keyword",
    #Token.Literal.Keyword.Declaration: "keyword",
    Token.Keyword: "keyword",
    #Token.Keyword.Namespace: "keyword",
    #Token.Literal.Comment.Hashbang: "string_literal",
    #Token.Literal.Comment.Single: "string_literal",    
}


def on_edit(event):
    # Удалить все имеющиеся теги из текста
    for tag in text.tag_names():
        text.tag_remove(tag, 1.0, tkinter.END)
    
    # Разобрать текст на токены
    s = text.get(1.0, tkinter.END)
    tokens = lexer.get_tokens_unprocessed(s)
    
    for i, token_type, token in tokens:
        
        j = i + len(token)
        if token_type in token_type_to_tag:
            text.tag_add(token_type_to_tag[token_type], get_text_coord(s, i), get_text_coord(s, j))

    # Сбросить флаг редактирования текста
    text.edit_modified(0)
    Light()




def TermExp(_format):
        if _format == 'r':
                fin = text.get('1.0' ,END)
                s_f = fin.split('\n')
                b_f = fin.split('.')
                n = -1
                for i in s_f:
                        n = n + 1
                        st = str(s_f[n])
                        block = st.split('.')
                        if block[0] == 'Program':
                                name = block[1]
                                file = open('Progarmm/' + str(name) + '.txt', 'r')
                                c = file.read()
                                text.delete('1.0', tkinter.END)
                                text.insert('1.0', c)

                        if block[0] == 'Print':
                                txt = block[1]
                                c = "Program P1;\nvar a, b, c, rezalt : real;\nbegin\n\n\nwriteln('" +  txt +  "');\n\nend.\n" 
                                text.delete('1.0', tkinter.END)
                                text.insert('1.0', c)                             

                        if block[0] == 'MathSample':
                                Var = block[1]
                                Sample = block[2]
                                c = "Program P1;\nvar " + str(Var) + ",rezalt : real;\nbegin\n\n\nwriteln('Введите деситичьные числа a, b, c: ');\nreadln(a, b, c);\nrezalt := " +  str(Sample) +  ";\nwriteln('Ответ = ', rezalt);\n\nend.\n"
                                text.delete('1.0', tkinter.END)
                                text.insert('1.0', c)

                        if block[0] == 'Drow':
                                Sip = block[1]

                                if Sip == 'Feet':
                                        case = block[3]
                                        size = block[2]
                                        txt = ComsolDrow.Drow.Feet(int(size), case, ' ')
                                        c = "Program P1;\n\nbegin\n\n\n" +  txt +  "\n\nend.\n"
                                        text.delete('1.0', tkinter.END)
                                        text.insert('1.0', c)
                                
                                if Sip == 'Spurce':
                                        case = block[3]
                                        size = block[2]
                                        txt = ComsolDrow.Drow.Spruce(int(size), case, ' ')
                                        c = "Program P1;\n\nbegin\n\n\n" +  txt +  "\n\nend.\n"
                                        text.delete('1.0', tkinter.END)
                                        text.insert('1.0', c)

def CreatPas(event):
        TermExp('r')
        text_l = text.get('1.0', tkinter.END).split('\n')
        for j in text_l:
                if j == '!':
                        doc = "Program P1;\nvar a, b, c, rezalt : real;\nbegin\n\nwriteln('Введите деситичьные числа a, b, c: ');\nreadln(a, b, c);\nrezalt := sqr(b) - 4 * a * c;\nwriteln('Дискриминант = ', rezalt);\n\nend.\n"
                        text.delete('1.0', tkinter.END)
                        text.insert('1.0', doc)

                if j == '!r':
                        Sample = 'a' + Defain.randomSimbol.Sib() + 'b' + Defain.randomSimbol.Sib() + 'c'
                        doc = "Program P1;\nvar a, b, c, rezalt : real;\nbegin\n\nwriteln('Введите деситичьные числа a, b, c: ');\nreadln(a, b, c);\nrezalt := " +  Sample +  ";\nwriteln('Ответ = ', rezalt);\n\nend.\n"
                        text.delete('1.0', tkinter.END)
                        text.insert('1.0', doc)                        

                if j == '!d':
                        Sample = 'a' + Defain.randomSimbol.SibNoD() + 'b' + Defain.randomSimbol.SibNoD() + 'c' + ' / ' + 'a' + Defain.randomSimbol.SibNoD() + 'b' + Defain.randomSimbol.SibNoD() + 'c'
                        doc = "Program P1;\nvar a, b, c, rezalt : real;\nbegin\n\nwriteln('Введите деситичьные числа a, b, c: ');\nreadln(a, b, c);\nrezalt := " +  Sample +  ";\nwriteln('Ответ = ', rezalt);\n\nend.\n"
                        text.delete('1.0', tkinter.END)
                        text.insert('1.0', doc)

                if j == '@':
                        Sample = 'a' + Defain.randomSimbol.Sib() + 'b' + Defain.randomSimbol.Sib() + 'c'
                        doc = '<!DOCTYPE html>\n<html>\n<head>\n       <title>""</title>\n</head>\n<body>\n\n\n\n</body>\n</html>\n'
                        text.delete('1.0', tkinter.END)
                        text.insert('1.0', doc)

                if j == '@s':
                        Sample = 'a' + Defain.randomSimbol.Sib() + 'b' + Defain.randomSimbol.Sib() + 'c'
                        doc = '<!DOCTYPE html>\n<html>\n<head>\n       <title>""</title>\n<link href="PythonDoc.css" rel="stylesheet" type="text/css"/>\n</head>\n<body>\n\n \n\n</body>\n</html>\n'
                        text.delete('1.0', tkinter.END)
                        text.insert('1.0', doc)

                if j == '@p':
                        Sample = 'a' + Defain.randomSimbol.Sib() + 'b' + Defain.randomSimbol.Sib() + 'c'
                        doc = '<!DOCTYPE html>\n<html>\n<head>\n       <title>""</title>\n<link href="PythonDoc.css" rel="stylesheet" type="text/css"/>\n</head>\n<body><h1>Welcom too Readme</h1>\n<i></i>\n<p></p>\n</body>\n</html>\n'
                        text.delete('1.0', tkinter.END)
                        text.insert('1.0', doc)




FILE_NAME = tkinter.NONE



class Tools():

        

        def CodeMask():               
                t = text.get('1.0', tkinter.END)
                t_l = t.split('<>')

                global FILE_NAME
                inp = askopenfile(mode="r")
                if inp is None:
                        return
                FILE_NAME = inp.name
                data = inp.read()

                data_l = data.split('\n')
                del data_l[0]
                j = len(data_l)

                jj = j - 1

                print(jj)

                del t_l[1]
                
                del data_l[jj]

                dataj = '\n'.join(data_l)

                ttt = str(t_l[0] + dataj + t_l[1])

                text.delete('1.0', tkinter.END)
                text.insert('1.0', ttt)           

        def InsertCode():               
                t = text.get('1.0', tkinter.END)
                t_l = t.split('<>')

                global FILE_NAME
                inp = askopenfile(mode="r")
                if inp is None:
                        return
                FILE_NAME = inp.name
                data = inp.read()

                data_l = data.split('\n')
                del data_l[0]
                j = len(data_l)

                jj = j - 1

                print(jj)
                
                del data_l[jj]

                dataj = '\n'.join(data_l)

                ttt = str(t_l[0] + dataj + t_l[1])

                text.delete('1.0', tkinter.END)
                text.insert('1.0', ttt)
               

        def buff():
                global t
                text.insert('1.0', t)                

        def undoZ(event):
                global TEXT
                text.insert('1.0', TEXT)
                
        class Deffains():

                def Read():
                        t = text.get('1.0', tkinter.END)
                        text.delete('1.0', tkinter.END)
                        doc = "read(a);"
                        text.insert('1.0', doc)
                        text.insert('1.0', t)

                def Logic():
                        t = text.get('1.0', tkinter.END)
                        text.delete('1.0', tkinter.END)
                        doc = "if 0 = 0 then writeln('0 is 0') else writeln('0 is not 0');"
                        text.insert('1.0', doc)
                        text.insert('1.0', t)
                        
                def LogicMathSample():
                        t = text.get('1.0', tkinter.END)
                        text.delete('1.0', tkinter.END)
                        Sample = 'a' + Defain.randomSimbol.Sib() + 'b' + Defain.randomSimbol.Sib() + 'c'
                        doc = "if 0 = 0 then writeln(" + Sample + ") else writeln(" + Sample + " + 1000);"
                        text.insert('1.0', doc)
                        text.insert('1.0', t)


                def Readln():
                        t = text.get('1.0', tkinter.END)
                        text.delete('1.0', tkinter.END)
                        doc = "readln(a);"
                        text.insert('1.0', doc)
                        text.insert('1.0', t)

                def Writeln():
                        t = text.get('1.0', tkinter.END)
                        text.delete('1.0', tkinter.END)
                        doc = "writeln('');"
                        text.insert('1.0', doc)
                        text.insert('1.0', t)

                def Write():
                        t = text.get('1.0', tkinter.END)
                        text.delete('1.0', tkinter.END)
                        doc = "write('');"
                        text.insert('1.0', doc)
                        text.insert('1.0', t)

                def Save(event):
                        data = text.get('1.0', tkinter.END)
                        #file = open('TOKENHUB.token', _format)

                                
                        out = asksaveasfile(mode='w', defaultextension='html')
                        out.write(data)
                        out.close()
                        
                        Gen('r')
                        text_l = text.get('1.0', tkinter.END).split('\n')
                        

                text.bind('<Control-s>', Save) 

        def coment_up():
                doc = '{Free comment!}'
                text.insert('1.0', doc)

        def coment_down():
                t = text.get('1.0', tkinter.END)
                text.delete('1.0', tkinter.END)
                doc = '{Free comment!}'
                text.insert('1.0', doc)
                text.insert('1.0', t)
                
        def clear():
                global t
                t = text.get('1.0', tkinter.END)
                text.delete('1.0', tkinter.END)


class Save:

        def export():
                data = text.get('1.0', tkinter.END)
                text_l = data.split()
                if text_l[0] != 'Program':
                        wraitdata = 'Program Pn;\n' + data + '\n\nend.'
                        File = open('Progarmm\P.txt', 'w')
                        File.write(wraitdata)

                else:
                        wraitdata = data
                        
                        File = open('Progarmm\P.txt', 'w')
                        File.write(wraitdata)

        def readme_txt():
                data = text.get('1.0', tkinter.END)
                out = asksaveasfile(mode='w', defaultextension='txt')
                out.write(data)
                out.close()
        def save_pas_flat(event):
                data = text.get('1.0', tkinter.END)
                text_l = data.split()
                if text_l[0] != 'Program':
                        wraitdata = 'Program Pn;\n' + data + '\n\nend.'
                        out = asksaveasfile(mode='w', defaultextension='pas')
                        out.write(wraitdata)
                        out.close()
                else:
                        pass
        def save_pas():
                data = text.get('1.0', tkinter.END)
                out = asksaveasfile(mode='w', defaultextension='pas')
                out.write(data)
                out.close()

        def readme_html():
                data = text.get('1.0', tkinter.END)
        #file = open('TOKENHUB.token', _format)

                                
                out = asksaveasfile(mode='w', defaultextension='html')
                out.write(data)
                out.close()

        def export2(event):
                data = text.get('1.0', tkinter.END)
                text_l = data.split()
                if text_l[0] != 'Program':
                        wraitdata = 'Program Pn;\n' + data + '\n\nend.'
                        File = open('Progarmm\P.txt', 'w')
                        File.write(wraitdata)

                else:
                        wraitdata = data
                        
                        File = open('Progarmm\P.txt', 'w')
                        File.write(wraitdata)

        def save_pas2(event):
                data = text.get('1.0', tkinter.END)
                out = asksaveasfile(mode='w', defaultextension='pas')
                out.write(data)
                out.close()


def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
	    return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def open_file2(event):
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
	    return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def InfopROGRAM():
        W = tkinter.Tk()
        W.title("Инфо -" + NAME_INFO_WIN)
        W[ 'bg' ] = MainBG
        W.geometry(InfoSize)
        W.iconbitmap(MainIco)

        label = Label(W, text='PasPogger это простой редактор для написания кода на Pascal. Созданый для использования строго в учебных целях!\nНа данный момент это только прототип в будушем будет доступно больше функций\nЕсли есть идеи то можете мне написать:\nАдрес Gmail: d.zimnov@gmail.com\nЯ в Discord: Ywxig#8564\nМой Git: Ywxig')
        label.pack()

def dell(event):
        global program
        program = ''

def printt(event):
        file = open('Buff.bup', 'r')
        program = file.read()
        print('\n\n\n\n\n\n\n\n\n\n' + str(program))
        text.delete('1.0', tkinter.END)
        text.insert('1.0', program)

class Link():

        def MyGit():
                wb.open('https://github.com/Ywxig/Program')

        def MyDiscord():
                text.insert('1.0', 'Ywxig#8564')

        def MainInfo():
                os.startfile('Info/MainInfo.html')

def ReadConf():
        File = open('CONFIG.py', 'r')
        T = File.read()
        text.insert('1.0', T)

def FileStrat():
        os.startfile('PasPogger.py')
        print('Ok')


#Бинды для функций!     
text.bind('<<Modified>>', on_edit)
text.bind('<F5>', Save.save_pas_flat)
text.bind('<Alt-s>', Save.export2)
text.bind('<Control-o>', open_file2)
text.bind('<Control-s>', Save.save_pas2)
text.bind('<Control-d>', dell)
text.bind('<Control-p>', printt)
text.bind('<space>', CreatPas)

menuBar = tkinter.Menu(root)
save = tkinter.Menu(root)


#Save
saveMenu = tkinter.Menu(root)
saveMenu = tkinter.Menu(menuBar)
saveMenu.add_command(label="Сохранить", command=Save.save_pas)
saveMenu.add_command(label="Экспорт", command=Save.export)
saveMenu.add_command(label="Открыть", command=open_file)
saveMenu.add_command(label="Выход", command=root.quit)

#Tools
readme = tkinter.Menu(root)
readme = tkinter.Menu(menuBar)
readme.add_command(label="HTML", command=Save.readme_html)
readme.add_command(label="Текст", command=Save.readme_txt)

comentmenu = tkinter.Menu(root)
comentmenu = tkinter.Menu(menuBar)
comentmenu.add_command(label="Верхний коментарий", command=Tools.coment_up)
comentmenu.add_command(label="Нижний коментарий", command=Tools.coment_down)

tooldef = tkinter.Menu(root)
tooldef = tkinter.Menu(menuBar)
tooldef.add_command(label="Write()", command=Tools.Deffains.Write)
tooldef.add_command(label="Writeln()", command=Tools.Deffains.Writeln)
tooldef.add_command(label="Read()", command=Tools.Deffains.Read)
tooldef.add_command(label="Readln()", command=Tools.Deffains.Readln)
tooldef.add_command(label="Logic", command=Tools.Deffains.Logic)

toolMenu = tkinter.Menu(root)
toolMenu = tkinter.Menu(menuBar)
toolMenu.add_cascade(label="Опирации", menu=tooldef)
toolMenu.add_command(label="Очистить", command=Tools.clear)
toolMenu.add_cascade(label="Добавить коммент", menu=comentmenu)
toolMenu.add_command(label="Востановить", command=Tools.buff)
toolMenu.add_cascade(label="ReadMe", menu=readme)
toolMenu.add_command(label="Вставить код", command=Tools.InsertCode)
toolMenu.add_command(label="Ножницы", command=Tools.CodeMask)
toolMenu.add_command(label="Открыть Терминал", command=Term)

#Optin!
OptinMenu = tkinter.Menu(root)
OptinMenu = tkinter.Menu(menuBar)
OptinMenu.add_command(label="PasPogger on git", command=Link.MyGit)
OptinMenu.add_command(label="Конфиг", command=ReadConf)

#Help!
winMenu = tkinter.Menu(root)
winMenu = tkinter.Menu(menuBar)
winMenu.add_command(label="Второе окно", command=FileStrat)

menuBar.add_cascade(label="Фаил", menu=saveMenu)
menuBar.add_cascade(label="Инструменты", menu=toolMenu)
menuBar.add_cascade(label="Настройки", menu=OptinMenu)
menuBar.add_cascade(label="Окна", menu=winMenu)
menuBar.add_command(label="О прогорамме", command=InfopROGRAM)
root.config(menu=menuBar)




root.mainloop()
