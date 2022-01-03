#!/usr/bin/env python
# coding=utf8
#
# ibus2cin
# a cin table conversion tool
# https://github.com/ethanliu/ibus2cin
#
# version: 3.0.0
# autor: Ethan Liu
#
import os
import sqlite3
import tkinter as tk
from sqlite3 import Error
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from webbrowser import open_new_tab

class Generator():
    headerTemplate = '''# The table was generated at {datetime} by ibus2cin conversion tool
# https://github.com/ethanliu/ibus2cin
#
%gen_inp
%encoding UTF-8
%ename {ename}
%cname {cname}
%serial_number {serial}
%selkey 0123456789
%keyname begin
a a
b b
c c
d d
e e
f f
g g
h h
i i
j j
k k
l l
m m
n n
o o
p p
q q
r r
s s
t t
u u
v v
w w
x x
y y
z z
, ,
. .
' ’
[ [
] ]
%keyname end
%chardef begin
'''
    footerTemplate = "%chardef end"

    def __init__(self, dbPath, cinPath):
        print(dbPath)
        print(cinPath)

        if dbPath == "" or os.path.isfile(dbPath) == False:
            messagebox.showerror(title = "Error", message = f'無法讀取資料庫檔案 "%s"' % (os.path.basename(dbPath)))
            return

        try:
            db = sqlite3.connect(dbPath)
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
        except Error:
            messagebox.showerror(title = "Error", message = f'無法讀取資料庫檔案 "%s"' % (os.path.basename(dbPath)))
            return

        try:
            info = self.parseAttrs(cursor)
        except Error:
            messagebox.showerror(title = "Error", message = f'無法讀取資料庫檔案 "%s"，檔案可能以損毀或不正確，請重新從行易官網下載 iBus Table 檔案' % (os.path.basename(dbPath)))
            return

        # print(info)
        content = self.parseContent(cursor)
        db.close()

        prefix = self.headerTemplate.format(
            datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ename = info['name'],
            cname = info['name.zh_tw'],
            serial = info['serial_number'],
        )
        suffix = self.footerTemplate

        fp = open(cinPath, "w")
        fp.write(prefix + content + suffix)
        fp.close()

        messagebox.showinfo(title = "Done", message = f'CIN 格式字根表檔案 "%s" 已儲存完成' % (os.path.basename(cinPath)))


    def parseAttrs(self, cursor):
        try:
            cursor.execute('SELECT attr, val FROM ime')
        except Error:
            print('a')
            print(Error)
            return
        rows = dict(cursor.fetchall())
        print(str(rows['name.zh_tw']))
        print(rows['serial_number'])
        return rows

    def parseContent(self, cursor):
        print("run")
        try:
            cursor.execute('SELECT tabkeys FROM phrases')
        except Error:
            query = '''
                ALTER TABLE "phrases" ADD COLUMN "tabkeys" CHAR;
                ALTER TABLE "phrases" ADD COLUMN "r0" CHAR; ALTER TABLE "phrases" ADD COLUMN "r1" CHAR; ALTER TABLE "phrases" ADD COLUMN "r2" CHAR; ALTER TABLE "phrases" ADD COLUMN "r3" CHAR; ALTER TABLE "phrases" ADD COLUMN "r4" CHAR;
                UPDATE "phrases" SET r0 = "a" WHERE m0 = 1; UPDATE "phrases" SET r0 = "b" WHERE m0 = 2; UPDATE "phrases" SET r0 = "c" WHERE m0 = 3; UPDATE "phrases" SET r0 = "d" WHERE m0 = 4; UPDATE "phrases" SET r0 = "e" WHERE m0 = 5; UPDATE "phrases" SET r0 = "f" WHERE m0 = 6; UPDATE "phrases" SET r0 = "g" WHERE m0 = 7; UPDATE "phrases" SET r0 = "h" WHERE m0 = 8; UPDATE "phrases" SET r0 = "i" WHERE m0 = 9; UPDATE "phrases" SET r0 = "j" WHERE m0 = 10; UPDATE "phrases" SET r0 = "k" WHERE m0 = 11; UPDATE "phrases" SET r0 = "l" WHERE m0 = 12; UPDATE "phrases" SET r0 = "m" WHERE m0 = 13; UPDATE "phrases" SET r0 = "n" WHERE m0 = 14; UPDATE "phrases" SET r0 = "o" WHERE m0 = 15; UPDATE "phrases" SET r0 = "p" WHERE m0 = 16; UPDATE "phrases" SET r0 = "q" WHERE m0 = 17; UPDATE "phrases" SET r0 = "r" WHERE m0 = 18; UPDATE "phrases" SET r0 = "s" WHERE m0 = 19; UPDATE "phrases" SET r0 = "t" WHERE m0 = 20; UPDATE "phrases" SET r0 = "u" WHERE m0 = 21; UPDATE "phrases" SET r0 = "v" WHERE m0 = 22; UPDATE "phrases" SET r0 = "w" WHERE m0 = 23; UPDATE "phrases" SET r0 = "x" WHERE m0 = 24; UPDATE "phrases" SET r0 = "y" WHERE m0 = 25; UPDATE "phrases" SET r0 = "z" WHERE m0 = 26; UPDATE "phrases" SET r0 = "[" WHERE m0 = 27; UPDATE "phrases" SET r0 = ";" WHERE m0 = 28; UPDATE "phrases" SET r0 = "'" WHERE m0 = 29; UPDATE "phrases" SET r0 = "[" WHERE m0 = 45; UPDATE "phrases" SET r0 = "]" WHERE m0 = 46; UPDATE "phrases" SET r0 = "," WHERE m0 = 55; UPDATE "phrases" SET r0 = "." WHERE m0 = 56;
                UPDATE "phrases" SET r1 = "a" WHERE m1 = 1; UPDATE "phrases" SET r1 = "b" WHERE m1 = 2; UPDATE "phrases" SET r1 = "c" WHERE m1 = 3; UPDATE "phrases" SET r1 = "d" WHERE m1 = 4; UPDATE "phrases" SET r1 = "e" WHERE m1 = 5; UPDATE "phrases" SET r1 = "f" WHERE m1 = 6; UPDATE "phrases" SET r1 = "g" WHERE m1 = 7; UPDATE "phrases" SET r1 = "h" WHERE m1 = 8; UPDATE "phrases" SET r1 = "i" WHERE m1 = 9; UPDATE "phrases" SET r1 = "j" WHERE m1 = 10; UPDATE "phrases" SET r1 = "k" WHERE m1 = 11; UPDATE "phrases" SET r1 = "l" WHERE m1 = 12; UPDATE "phrases" SET r1 = "m" WHERE m1 = 13; UPDATE "phrases" SET r1 = "n" WHERE m1 = 14; UPDATE "phrases" SET r1 = "o" WHERE m1 = 15; UPDATE "phrases" SET r1 = "p" WHERE m1 = 16; UPDATE "phrases" SET r1 = "q" WHERE m1 = 17; UPDATE "phrases" SET r1 = "r" WHERE m1 = 18; UPDATE "phrases" SET r1 = "s" WHERE m1 = 19; UPDATE "phrases" SET r1 = "t" WHERE m1 = 20; UPDATE "phrases" SET r1 = "u" WHERE m1 = 21; UPDATE "phrases" SET r1 = "v" WHERE m1 = 22; UPDATE "phrases" SET r1 = "w" WHERE m1 = 23; UPDATE "phrases" SET r1 = "x" WHERE m1 = 24; UPDATE "phrases" SET r1 = "y" WHERE m1 = 25; UPDATE "phrases" SET r1 = "z" WHERE m1 = 26; UPDATE "phrases" SET r1 = "[" WHERE m1 = 27; UPDATE "phrases" SET r1 = ";" WHERE m1 = 28; UPDATE "phrases" SET r1 = "'" WHERE m1 = 29; UPDATE "phrases" SET r1 = "[" WHERE m1 = 45; UPDATE "phrases" SET r1 = "]" WHERE m1 = 46; UPDATE "phrases" SET r1 = "," WHERE m1 = 55; UPDATE "phrases" SET r1 = "." WHERE m1 = 56;
                UPDATE "phrases" SET r2 = "a" WHERE m2 = 1; UPDATE "phrases" SET r2 = "b" WHERE m2 = 2; UPDATE "phrases" SET r2 = "c" WHERE m2 = 3; UPDATE "phrases" SET r2 = "d" WHERE m2 = 4; UPDATE "phrases" SET r2 = "e" WHERE m2 = 5; UPDATE "phrases" SET r2 = "f" WHERE m2 = 6; UPDATE "phrases" SET r2 = "g" WHERE m2 = 7; UPDATE "phrases" SET r2 = "h" WHERE m2 = 8; UPDATE "phrases" SET r2 = "i" WHERE m2 = 9; UPDATE "phrases" SET r2 = "j" WHERE m2 = 10; UPDATE "phrases" SET r2 = "k" WHERE m2 = 11; UPDATE "phrases" SET r2 = "l" WHERE m2 = 12; UPDATE "phrases" SET r2 = "m" WHERE m2 = 13; UPDATE "phrases" SET r2 = "n" WHERE m2 = 14; UPDATE "phrases" SET r2 = "o" WHERE m2 = 15; UPDATE "phrases" SET r2 = "p" WHERE m2 = 16; UPDATE "phrases" SET r2 = "q" WHERE m2 = 17; UPDATE "phrases" SET r2 = "r" WHERE m2 = 18; UPDATE "phrases" SET r2 = "s" WHERE m2 = 19; UPDATE "phrases" SET r2 = "t" WHERE m2 = 20; UPDATE "phrases" SET r2 = "u" WHERE m2 = 21; UPDATE "phrases" SET r2 = "v" WHERE m2 = 22; UPDATE "phrases" SET r2 = "w" WHERE m2 = 23; UPDATE "phrases" SET r2 = "x" WHERE m2 = 24; UPDATE "phrases" SET r2 = "y" WHERE m2 = 25; UPDATE "phrases" SET r2 = "z" WHERE m2 = 26; UPDATE "phrases" SET r2 = "[" WHERE m2 = 27; UPDATE "phrases" SET r2 = ";" WHERE m2 = 28; UPDATE "phrases" SET r2 = "'" WHERE m2 = 29; UPDATE "phrases" SET r2 = "[" WHERE m2 = 45; UPDATE "phrases" SET r2 = "]" WHERE m2 = 46; UPDATE "phrases" SET r2 = "," WHERE m2 = 55; UPDATE "phrases" SET r2 = "." WHERE m2 = 56;
                UPDATE "phrases" SET r3 = "a" WHERE m3 = 1; UPDATE "phrases" SET r3 = "b" WHERE m3 = 2; UPDATE "phrases" SET r3 = "c" WHERE m3 = 3; UPDATE "phrases" SET r3 = "d" WHERE m3 = 4; UPDATE "phrases" SET r3 = "e" WHERE m3 = 5; UPDATE "phrases" SET r3 = "f" WHERE m3 = 6; UPDATE "phrases" SET r3 = "g" WHERE m3 = 7; UPDATE "phrases" SET r3 = "h" WHERE m3 = 8; UPDATE "phrases" SET r3 = "i" WHERE m3 = 9; UPDATE "phrases" SET r3 = "j" WHERE m3 = 10; UPDATE "phrases" SET r3 = "k" WHERE m3 = 11; UPDATE "phrases" SET r3 = "l" WHERE m3 = 12; UPDATE "phrases" SET r3 = "m" WHERE m3 = 13; UPDATE "phrases" SET r3 = "n" WHERE m3 = 14; UPDATE "phrases" SET r3 = "o" WHERE m3 = 15; UPDATE "phrases" SET r3 = "p" WHERE m3 = 16; UPDATE "phrases" SET r3 = "q" WHERE m3 = 17; UPDATE "phrases" SET r3 = "r" WHERE m3 = 18; UPDATE "phrases" SET r3 = "s" WHERE m3 = 19; UPDATE "phrases" SET r3 = "t" WHERE m3 = 20; UPDATE "phrases" SET r3 = "u" WHERE m3 = 21; UPDATE "phrases" SET r3 = "v" WHERE m3 = 22; UPDATE "phrases" SET r3 = "w" WHERE m3 = 23; UPDATE "phrases" SET r3 = "x" WHERE m3 = 24; UPDATE "phrases" SET r3 = "y" WHERE m3 = 25; UPDATE "phrases" SET r3 = "z" WHERE m3 = 26; UPDATE "phrases" SET r3 = "[" WHERE m3 = 27; UPDATE "phrases" SET r3 = ";" WHERE m3 = 28; UPDATE "phrases" SET r3 = "'" WHERE m3 = 29; UPDATE "phrases" SET r3 = "[" WHERE m3 = 45; UPDATE "phrases" SET r3 = "]" WHERE m3 = 46; UPDATE "phrases" SET r3 = "," WHERE m3 = 55; UPDATE "phrases" SET r3 = "." WHERE m3 = 56;
                UPDATE "phrases" SET r4 = "a" WHERE m4 = 1; UPDATE "phrases" SET r4 = "b" WHERE m4 = 2; UPDATE "phrases" SET r4 = "c" WHERE m4 = 3; UPDATE "phrases" SET r4 = "d" WHERE m4 = 4; UPDATE "phrases" SET r4 = "e" WHERE m4 = 5; UPDATE "phrases" SET r4 = "f" WHERE m4 = 6; UPDATE "phrases" SET r4 = "g" WHERE m4 = 7; UPDATE "phrases" SET r4 = "h" WHERE m4 = 8; UPDATE "phrases" SET r4 = "i" WHERE m4 = 9; UPDATE "phrases" SET r4 = "j" WHERE m4 = 10; UPDATE "phrases" SET r4 = "k" WHERE m4 = 11; UPDATE "phrases" SET r4 = "l" WHERE m4 = 12; UPDATE "phrases" SET r4 = "m" WHERE m4 = 13; UPDATE "phrases" SET r4 = "n" WHERE m4 = 14; UPDATE "phrases" SET r4 = "o" WHERE m4 = 15; UPDATE "phrases" SET r4 = "p" WHERE m4 = 16; UPDATE "phrases" SET r4 = "q" WHERE m4 = 17; UPDATE "phrases" SET r4 = "r" WHERE m4 = 18; UPDATE "phrases" SET r4 = "s" WHERE m4 = 19; UPDATE "phrases" SET r4 = "t" WHERE m4 = 20; UPDATE "phrases" SET r4 = "u" WHERE m4 = 21; UPDATE "phrases" SET r4 = "v" WHERE m4 = 22; UPDATE "phrases" SET r4 = "w" WHERE m4 = 23; UPDATE "phrases" SET r4 = "x" WHERE m4 = 24; UPDATE "phrases" SET r4 = "y" WHERE m4 = 25; UPDATE "phrases" SET r4 = "z" WHERE m4 = 26; UPDATE "phrases" SET r4 = "[" WHERE m4 = 27; UPDATE "phrases" SET r4 = ";" WHERE m4 = 28; UPDATE "phrases" SET r4 = "'" WHERE m4 = 29; UPDATE "phrases" SET r4 = "[" WHERE m4 = 45; UPDATE "phrases" SET r4 = "]" WHERE m4 = 46; UPDATE "phrases" SET r4 = "," WHERE m4 = 55; UPDATE "phrases" SET r4 = "." WHERE m4 = 56;
            '''
            cursor.executescript(query)
            cursor.execute("UPDATE phrases SET tabkeys = (coalesce(r0,'')||coalesce(r1,'')||coalesce(r2,'')||coalesce(r3,'')||coalesce(r4,''))")
            cursor.executescript("ALTER TABLE phrases DROP COLUMN r0; ALTER TABLE phrases DROP COLUMN r1; ALTER TABLE phrases DROP COLUMN r2;ALTER TABLE phrases DROP COLUMN r3; ALTER TABLE phrases DROP COLUMN r4;")

        finally:
            cursor.execute('SELECT tabkeys, phrase FROM phrases ORDER BY id ASC')
            rows = cursor.fetchall()
            content = ""
            for row in rows:
                radical = row[0].strip().lower()
                phrase = row[1].strip()
                if radical == "" or phrase == "":
                    continue
                content += radical + "\t" + phrase + "\n"
            return content


class App(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self.version = '3.0.0'
        root.title("ibus2cin - " + self.version)
        root.geometry('480x400')
        root.resizable(False, False)

        self.root = root
        self.basedir = ""
        self.inputFilename = StringVar()
        self.outputFilename = StringVar()
        # print(root.configure().keys())
        # print(set(btn.configure().keys()) - set(frm.configure().keys()))

        # body = tk.Frame(root, bg = '#4D92C5')
        body = tk.Frame(root)
        body.pack(side = "top", fill = "both", expand = True)

        self.header = tk.Frame(body)
        self.contianer = tk.Frame(body)
        self.footer = tk.Frame(body)

        # body.grid(sticky = "nsew")
        self.header.grid(row = 0, column = 0)
        self.contianer.grid(row = 1, column = 0)
        self.footer.grid(row = 2, column = 0)

        body.grid_rowconfigure(0, weight = 2)
        body.grid_rowconfigure(1, weight = 7)
        body.grid_rowconfigure(2, weight = 1)

        # self.header.pack()
        # self.contianer.pack()
        # self.footer.pack()

        self.layoutViews()
        self.defineStyles()

    def performConvert(self):
        Generator(dbPath = os.path.join(self.basedir, str(self.inputFilename.get())), cinPath = os.path.join(self.basedir, str(self.outputFilename.get())))

    def defineStyles(self):
        style = ttk.Style(self)
        style.configure('Logo.TLabel', font = ('Helvetica', 80, 'bold'), foreground = 'black')
        style.configure('Branding.TLabel', font = ('Helvetica', 24), foreground = '#000000')
        style.configure('Heading.TLabel', font = ('Helvetica', 16), foreground = '#000000')


    def layoutViews(self):
        self.addMenu(self.root)
        self.addHeaderView(self.header)
        self.addContainerView(self.contianer)
        self.addFooterView(self.footer)

    def addMenu(self, root):
        def performAboutAction():
            open_new_tab('https://github.com/ethanliu/ibus2cin')

        menu = Menu(root)

        # fileMenu = Menu(menu)
        # fileMenu.add_command(label = "Open")
        # menu.add_separator()
        # fileMenu.add_command(label = "Exit")
        # menu.add_cascade(label = "File", menu = fileMenu)

        aboutMenu = Menu(menu)
        aboutMenu.add_command(label = "About", command = performAboutAction)
        menu.add_cascade(label = "About", menu = aboutMenu)

        root.config(menu = menu)


    def addHeaderView(self, parent):
        ttk.Label(parent, text = '無', style = 'Logo.TLabel').grid(row = 0, column = 0, rowspan = 8, pady = (20, 20), padx = (0, 20))
        ttk.Label(parent, text = "").grid(row = 0, column = 3)
        ttk.Label(parent, text = "").grid(row = 1, column = 3, pady = (10, 0))
        ttk.Label(parent, text = 'ibus2cin', style = 'Branding.TLabel').grid(row = 2, column = 3, sticky = W, pady = (0, 0))
        ttk.Label(parent, text = 'Ver.' + self.version).grid(row = 3, column = 3, sticky = W, pady = (0, 0))
        ttk.Label(parent, text = 'CIN Table Conversion Tool').grid(row = 4, column = 3, sticky = W)
        ttk.Label(parent, text = "").grid(row = 5, column = 3)
        ttk.Label(parent, text = "").grid(row = 6, column = 3)

    def addFooterView(self, parent):
        label = ttk.Label(parent, text = "This program is distributed to help legal users but without any warranty.", padding = 10, anchor = W)
        label.grid(row = 0, column = 0, columnspan = 5, sticky=W+E, pady = (40, 0))

    def addContainerView(self, parent):

        def selectFile():
            path = filedialog.askopenfilename(title = "Select file", filetypes = [("SQLite File", "*.db")], initialdir = os.path.dirname(__file__))
            self.basedir = os.path.dirname(path)
            self.inputFilename.set(os.path.basename(path))
            self.outputFilename.set(os.path.basename(path.replace('.db', '.cin')))

            if path == None or path == "":
                outputTextField['state'] = tk.DISABLED
                convertButton['state'] = tk.DISABLED
            else:
                outputTextField['state'] = tk.NORMAL
                convertButton['state'] = tk.NORMAL

            # inputTextField.delete(0, END)
            # inputTextField.insert(0, os.path.basename(path))

        inputTextField = ttk.Entry(parent, width = 30, textvariable = self.inputFilename, state = DISABLED)
        outputTextField = ttk.Entry(parent, width = 30, textvariable = self.outputFilename, state = DISABLED)

        selectFileButton = ttk.Button(parent, text = 'Open', command = selectFile)
        convertButton = ttk.Button(parent, text = 'Convert', state = DISABLED, command = self.performConvert)

        ttk.Label(parent, text = "iBus Table").grid(row = 0, column = 0, pady = 5)
        ttk.Label(parent, text = "CIN Table").grid(row = 1, column = 0, pady = 5)
        ttk.Label(parent, text = 'Choose an boshimay iBus Table file to continue...', style = 'Heading.TLabel').grid(row = 2, column = 0, columnspan = 4, pady = (20, 10), padx = (30, 0))

        inputTextField.grid(row = 0, column = 1, columnspan = 5)
        outputTextField.grid(row = 1, column = 1, columnspan = 5)
        selectFileButton.grid(row = 3, column = 1, pady = (0, 0))
        convertButton.grid(row = 3, column = 2, pady = (0, 0))


def main():
    root = tk.Tk()
    app = App(root)
    app.mainloop()


if __name__ == "__main__":
    main()