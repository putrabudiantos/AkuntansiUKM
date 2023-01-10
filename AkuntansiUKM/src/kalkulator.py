from tkinter import *

class Calc:

    def __init__(self, root):
        self.root = root
        self.ekspresi = ""
        self.inputtext = StringVar()
        self.layout()

    def klik(self, item):
        self.item = item
        self.ekspresi = self.ekspresi + str(self.item)
        self.inputtext.set(self.ekspresi)

    def clear(self):
        self.ekspresi = ""
        self.inputtext.set("")

    def samadengan(self):
        hasil = str(eval(self.ekspresi))
        self.inputtext.set(hasil)
        self.ekspresi = ""


    def layout(self):
        entryangka = Entry(self.root, textvariable=self.inputtext, width=25)
        entryangka.place(relx=0.5, rely=0.13, anchor=CENTER)

        tombol1 = Button(self.root, text=' 1 ', command=lambda: self.klik(1), height=1, width=7).place(relx=0.35, rely=0.2, anchor=CENTER)
        tombol2 = Button(self.root, text=' 2 ', command=lambda: self.klik(2), height=1, width=7).place(relx=0.5, rely=0.2, anchor=CENTER)
        tombol3 = Button(self.root, text=' 3 ', command=lambda: self.klik(3), height=1, width=7).place(relx=0.65, rely=0.2, anchor=CENTER)
        tombol4 = Button(self.root, text=' 4 ', command=lambda: self.klik(4), height=1, width=7).place(relx=0.35, rely=0.27, anchor=CENTER)
        tombol5 = Button(self.root, text=' 5 ', command=lambda: self.klik(5), height=1, width=7).place(relx=0.5, rely=0.27, anchor=CENTER)
        tombol6 = Button(self.root, text=' 6 ', command=lambda: self.klik(6), height=1, width=7).place(relx=0.65, rely=0.27, anchor=CENTER)
        tombol7 = Button(self.root, text=' 7 ', command=lambda: self.klik(7), height=1, width=7).place(relx=0.35, rely=0.34, anchor=CENTER)
        tombol8 = Button(self.root, text=' 8 ', command=lambda: self.klik(8), height=1, width=7).place(relx=0.5, rely=0.34, anchor=CENTER)
        tombol9 = Button(self.root, text=' 9 ', command=lambda: self.klik(9), height=1, width=7).place(relx=0.65, rely=0.34, anchor=CENTER)
        tombol0 = Button(self.root, text=' 0 ', command=lambda: self.klik(0), height=1, width=7).place(relx=0.5, rely=0.41, anchor=CENTER)
        tomboltambah = Button(self.root, text='+', command=lambda: self.klik('+'), height=1, width=7, bg='yellow').place(relx=0.35, rely=0.41, anchor=CENTER)
        tombolkurang = Button(self.root, text='-', command=lambda: self.klik('-'), height=1, width=7, bg='yellow').place(relx=0.65, rely=0.41, anchor=CENTER)
        tombolbagi = Button(self.root, text='/', command=lambda: self.klik('/'), height=1, width=7, bg='yellow').place(relx=0.35, rely=0.48, anchor=CENTER)
        tombolkali = Button(self.root, text='x', command=lambda: self.klik('*'), height=1, width=7, bg='yellow').place(relx=0.5, rely=0.48, anchor=CENTER)
        tombolmodulo = Button(self.root, text='%', command=lambda: self.klik('%'), height=1, width=7, bg='yellow').place(relx=0.65, rely=0.48, anchor=CENTER)
        tombolequal = Button(self.root, text='=', command=lambda: self.samadengan(), height=1, width=7, bg='green').place(relx=0.5, rely=0.55, anchor=CENTER)
        tombolclear = Button(self.root, text='C', command=lambda: self.clear(), height=1, width=7, bg='white').place(relx=0.65, rely=0.55, anchor=CENTER)