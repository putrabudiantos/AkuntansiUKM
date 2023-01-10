import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, filedialog
import csv, os, glob
import pandas as pd
import jurnalbutton, tambahopsi, informasialert
import excel

class Main():
    def __init__(self, root) -> None:
        self.root = root

        self.listbox = tk.Listbox(self.root, height = 10,
            width = 40,
            activestyle = 'dotbox',
            font = "Helvetica",
            fg = "black")
        self.adadata()


    def adadata(self):
        self.data = glob.glob('/home/python/Tugas/AkuntansiUKM/src/documents/jsonfolder/**/*.json', recursive=True)
        if self.data:
            for i,j in enumerate(self.data):
                self.listbox.insert(i, os.path.split(j)[1])
                self.listbox.pack(pady=130)
            self.pilih = Button(self.root, text='Ekspor ke EXCEL', command=lambda: [self.pilihan(), excel.connecting(), informasialert.Pesan(self.root).suksesconvert()]).place(relx=0.40, rely=0.7)
        else:
            labelresult = Label(self.root, text='Tidak ada data', font=('Calibri 13'))
            labelresult.place(relx=0.5, rely=0.5, anchor=CENTER)

    def pilihan(self):
        import json
        data_frame = pd.DataFrame()
        for i in self.listbox.curselection():
            print(self.listbox.get(i))
            # with open(i, 'r') as j:
            #     write = json.dump(i, j)
            # if self.listbox.get(i):
            #     with open(self.listbox.get(i), 'w') as f:
            #         pass
                    
# if __name__ == '__main__':
#     root = tk.Tk()
#     Main(root)
#     root.mainloop()

