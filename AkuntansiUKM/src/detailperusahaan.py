import configsql, informasialert
import csv
from tkinter import *
import json
from tkinter import ttk


class AturPerusahaan():
    def __init__(self, root):
        # objek root
        self.akar = root
        
        # toplevel objek
        self.login = Toplevel(self.akar)
        self.dataku = []
        self.maps = {}
        # Entry
        self.namaperusahaan = ttk.Entry(self.login)
        self.alamatperusahaan = ttk.Entry(self.login)
        self.telponperusahaan = ttk.Entry(self.login)
        self.emailperusahaan = ttk.Entry(self.login)

        self.login.geometry("330x150")
        self.login.title("Atur Perusahaan")
        self.login.resizable(False, False)
        Label(self.login, text="Nama Perusahaan", font="courier,bold, 9").grid(row=0, column=0,sticky=W, pady=5, padx=8)
        self.namaperusahaan.grid(row=0,column=1, pady=3)
        Label(self.login, text="Alamat Perusahaan", font="courier,bold, 9").grid(row=1, column=0,sticky=W, pady=5, padx=8)
        self.alamatperusahaan.grid(row=1,column=1, pady=3)
        Label(self.login, text="Telpon Perusahaan", font="courier,bold, 9").grid(row=2, column=0,sticky=W, pady=5, padx=8)
        self.telponperusahaan.grid(row=2,column=1, pady=3)
        Label(self.login, text="Email Perusahaan", font="courier,bold, 9").grid(row=3, column=0,sticky=W, pady=5, padx=8)
        self.emailperusahaan.grid(row=3,column=1, pady=3)

        self.hasilalert = informasialert.Pesan(self.login)
        Button(self.login, text="Simpan", command=lambda: [self.submit(), self.hasilalert]).place(x=120, y=115)

    def submit(self):
        getnama = self.namaperusahaan.get()
        getalamat = self.alamatperusahaan.get()
        gettelp = self.telponperusahaan.get()
        getemail = self.emailperusahaan.get()

        tmp = (getnama, getalamat, gettelp, getemail)
        
        if getnama == "":
            self.hasilalert = informasialert.Pesan(self.login).kosong()
        elif getalamat == "":
            self.hasilalert = informasialert.Pesan(self.login).kosong()
        elif gettelp == "":
            self.hasilalert = informasialert.Pesan(self.login).kosong()
        elif getemail == "":
            self.hasilalert = informasialert.Pesan(self.login).kosong()
        else:
            self.hasilalert = informasialert.Pesan(self.login).sukses() 

        # insert data ke temporary list untuk checking masuk
        for i in tmp:
            self.dataku.append(i)

        print(self.dataku)

        self.maps[getnama]=[{}]
        self.maps[getnama][0]['alamat'] = getalamat
        self.maps[getnama][0]['nomor'] = gettelp
        self.maps[getnama][0]['email'] = getemail

        with open(f'/home/python/Tugas/AkuntansiUKM/src/documents/perusahaan/{getnama}.json', 'w') as f:
            write = json.dump(self.maps,f)

        # Store ke database
        configsql.MySQL('localhost', 'python', 'KaliLinux', 'ukm').insert_data('detailperusahaan', tmp)

        



