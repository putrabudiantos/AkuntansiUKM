
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
import filetipe, jurnalbutton, tentang, kalkulator, laporanbutton, detailperusahaan, configsql, informasialert, tambahopsi, updateframedata
import os, time, threading
import datetime
from PIL import ImageTk, Image 
import PIL.Image
import jurnaltombolwindow

class Main():
    def __init__(self, root):
        self.root = root
        self.main_menu()
        self.display()

    def display(self):

        self.tabmanager = Notebook(self.root)
        self.tabmanager.pack(expand=1,fill="both")

        self.tabjurnal = Frame(self.tabmanager)
        self.tablaporan = Frame(self.tabmanager)
        self.tabkalkulator = Frame(self.tabmanager)
        self.tabdb = Frame(self.tabmanager)
        self.tabkontribusi = Frame(self.tabmanager)

        self.navigasibar = [
            self.navigasibarjurnal(), 
            self.navigasibarlaporan(), 
            self.navigasibarkalkulator(),
            self.authdb(),
            self.navigasibarkontribusi(),
            ]

    def main_menu(self):

        self.root.geometry("623x500")
        self.root.title("Akuntansi UKM")
        # self.root.resizable(False, alse)

        navbar = Menu(self.root)
        self.root.config(menu=navbar)

        objek = Menu(navbar, tearoff=False)

        # Menubar File
        submenu = Menu(self.root, tearoff=False)
        objek.add_command(label="Buat File Baru", command=None)
        objek.add_command(label="Buka File", command=lambda: filedialog.askopenfilename(title="Buka File", initialdir="./", filetypes=filetipe.files))
        objek.add_separator()
        objek.add_command(label="Simpan", command=lambda: filedialog.asksaveasfile(filetypes=filetipe.files, defaultextension=filetipe.filetype))
        objek.add_command(label = "Simpan Sebagai", command=lambda: filedialog.asksaveasfilename(confirmoverwrite=False))
        objek.add_separator()
        submenu.add_command(label = "PDF (.pdf)", command=None)
        submenu.add_command(label = "Microsoft Excel (.xlsx)", command=None)
        objek.add_cascade(label = "Ekspor sebagai", menu=submenu)
        objek.add_separator()
        objek.add_command(label = "Keluar",command=lambda: exit())
        navbar.add_cascade(label='File', menu=objek)
        
        #Membuat Edit Navigasi
        edit = Menu(navbar, tearoff=False)
        edit.add_command(label="Undo", command=None)
        edit.add_command(label="Redo", command=None)
        edit.add_separator()
        edit.add_command(label="Potong", command=None)
        edit.add_command(label="Copy", command=None)
        edit.add_separator()
        edit.add_command(label="Temukan File", command=None)
        edit.add_separator()
        edit.add_command(label="Atur Perusahaan Anda",  command=lambda: detailperusahaan.AturPerusahaan(self.root))
        navbar.add_cascade(label="Edit", command=None, menu=edit)

        #Membuat View Menu
        view = Menu(navbar, tearoff=False)
        view.add_command(label="Tema", command=None)
        navbar.add_cascade(label="View", command=None, menu=view)

        # Membuat Help Menu
        help = Menu(navbar, tearoff=False)
        help.add_command(label="Tutorial", command=None)
        help.add_command(label="Tentang", command=lambda: tentang.tentang(self.root))
        navbar.add_cascade(label="Bantuan", command=None, menu=help)

    def navigasibarjurnal(self):

        self.tabmanager.add(self.tabjurnal, text="Jurnal")

        today = datetime.date.today()
        year = today.year

        Label(self.tabjurnal, text="Jurnal Akuntansi UKM",  font=('Calibri 15')).place(relx=0.5, rely=0.05, anchor=CENTER)

        combomonth = ttk.Combobox(self.tabjurnal, state='readonly',values=['Januari','Februari','Maret','April','Mei','Juni','Juli', 'Agustus','September','Oktober','November', 'Desember'])
        combomonth.place(relx=0.18, rely=0.12, anchor=NW)
        combomonth.current(0)

        comboyear = ttk.Combobox(self.tabjurnal, state='readonly',values=year)
        comboyear.place(relx=0.85, rely=0.12, anchor=NE)
        comboyear.current(0)
        cari = ttk.Entry(self.tabjurnal, width=30)
        cari.insert(0, 'Cari')
        cari.place(relx=0.5, rely=0.21, anchor=CENTER)
        print("Tab jurnal ditekan")

        updateframedata.Main(self.tabjurnal)

        tomboltransaksi = ttk.Button(self.tabjurnal, text="[+] Transaksi Baru", width=20, command=lambda: jurnalbutton.Jurnal(self.root)).place(relx=0.3, rely=0.9, anchor=CENTER)
        tombollanjutan = ttk.Button(self.tabjurnal, text="[+] Tambah Opsi", width=20, command=lambda: tambahopsi.tambahopsi()).place(relx=0.68, rely=0.9, anchor=CENTER)
        
    
    def navigasibarlaporan(self):
        self.tabmanager.add(self.tablaporan,text="Laporan")

        Label(self.tablaporan, text="Laporan Akuntansi UKM",  font=('Calibri 15')).pack(pady=10)

        jurnaltombol = Button(self.tablaporan, text='Jurnal', height=2, command=lambda: jurnaltombolwindow.JurnalWindow(self.tablaporan)).pack(fill=X)
        bukubesartombol = Button(self.tablaporan, text='Buku Besar', height=2).pack(fill=X)
        neracasaldotombol = Button(self.tablaporan, text='Neraca Saldo', height=2).pack(fill=X)
        labarugitombol = Button(self.tablaporan, text='Laba Rugi', height=2).pack(fill=X)
        neracatombol = Button(self.tablaporan, text='Neraca', height=2).pack(fill=X)
        periodetombol = Button(self.tablaporan, text='Periode', height=2).pack(fill=X)
        utangtombol = Button(self.tablaporan, text='Utang', height=2).pack(fill=X)
        piutangtombol = Button(self.tablaporan, text='Piutang', height=2).pack(fill=X)
        spttombol = Button(self.tablaporan, text='SPT PPh OP', height=2).pack(fill=X)

    def navigasibarkalkulator(self):
        self.tabmanager.add(self.tabkalkulator,text="Kalkulator")
        Label(self.tabkalkulator, text="Kalkulator",  font=('Calibri 15')).place(relx=0.5, rely=0.05, anchor=CENTER)
        kalkulator.Calc(self.tabkalkulator)

    def authdb(self):
        self.tabmanager.add(self.tabdb,text="Konfigurasi Database")
        Label(self.tabdb, text="Konfigurasi Database",  font=('Calibri 15')).place(relx=0.5, rely=0.05, anchor=CENTER)
        self.hostname = ttk.Entry(self.tabdb)
        self.username = ttk.Entry(self.tabdb)
        e1_str = tk.StringVar()
        self.password = ttk.Entry(self.tabdb, show='*', textvariable=e1_str)
        self.databse = ttk.Entry(self.tabdb)

        labelhostname = Label(self.tabdb, text="Hostname", font=('Calibri 13'))
        labelhostname.place(relx=0.27, rely=0.2)
        self.hostname.place(relx=0.46, rely=0.2)

        labelusername = Label(self.tabdb, text="Username", font=('Calibri 13'))
        labelusername.place(relx=0.27, rely=0.27)
        self.username.place(relx=0.46, rely=0.27)

        sv = tk.StringVar()
        c_v1 = IntVar(value=0)

        labelpassword = Label(self.tabdb, text="Password", font=('Calibri 13'))

        def tampilsandi():
            if c_v1.get() == 1:
                self.password.config(show='')
            else:
                self.password.config(show='*')

        checktampilsandi = tk.Checkbutton(self.tabdb, text="Tampil", variable=c_v1, onvalue=1, offvalue=0, command=tampilsandi)
        checktampilsandi.place(relx=0.73, rely=0.34)

        labelpassword.place(relx=0.27, rely=0.34)
        self.password.place(relx=0.46, rely=0.34)

        labeldatabase = Label(self.tabdb, text="Database", font=('Calibri 13'))
        labeldatabase.place(relx=0.27, rely=0.41)
        self.databse.place(relx=0.46, rely=0.41)

        tombolsubmit = Button(self.tabdb, text='Sambungkan', command=lambda: [submitdb(),self.hasil])
        tombolsubmit.place(relx=0.42, rely=0.5)

        def submitdb():
            import mysql.connector

            gethostname = self.hostname.get()
            getusername = self.username.get()
            getpassowrd = self.password.get()
            getdatabase = self.databse.get()

            temporary = (gethostname, getusername, getpassowrd, getdatabase)

            if gethostname == "":
                self.hasil = informasialert.Pesan(self.root).kosong()
            elif getusername == "":
                self.hasil = informasialert.Pesan(self.root).kosong()
            elif getpassowrd == "":
                self.hasil = informasialert.Pesan(self.root).kosong()
            elif getdatabase == "":
                self.hasil = informasialert.Pesan(self.root).kosong()
            else:
                self.hasil = informasialert.Pesan(self.root).suksesterhubung()
            
            configsql.MySQL(gethostname, getusername, getpassowrd, getdatabase)


    def navigasibarkontribusi(self):
        self.tabmanager.add(self.tabkontribusi,text="Kontribusi")
        Label(self.tabkontribusi, text="Kontribusi dengan Kami",  font=('Calibri 15')).place(relx=0.5, rely=0.05, anchor=CENTER)


if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()