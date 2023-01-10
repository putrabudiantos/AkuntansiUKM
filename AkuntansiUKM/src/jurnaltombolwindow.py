import datetime 
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, messagebox
from informasialert import Pesan
from openpyxl import Workbook 
from openpyxl.styles import Color, PatternFill, Font, Border, Side
import json, configsql, updateframedata, os
from datetime import date
import mysql.connector


class JurnalWindow:
    def __init__(self, toplevel):
        self.toplevel = toplevel
        self.login = Toplevel(self.toplevel)
        self.login.title("Jurnal")
        self.login.geometry("850x500")
        self.login.resizable(0,0)

        today = datetime.date.today()
        year = today.year
        # Judul window
        Label(self.login, text="Jurnal", font=('Calibri 15')).grid(row=0, column=2)
        # header bulan
        bulan = ttk.Combobox(self.login, state='readonly',values=['Januari','Februari','Maret','April','Mei','Juni','Juli', 'Agustus','September','Oktober','November', 'Desember'])
        bulan.grid(row=1, column=0)
        bulan.current(0)

        # header tahun
        tahun = ttk.Combobox(self.login, state='readonly',values=year)
        tahun.grid(row=1, column=1)
        tahun.current(0)

        # header 
        Label(self.login, text="/", font=('Calibri 15')).grid(row=1, column=2)

        # header bulan
        bulan2 = ttk.Combobox(self.login, state='readonly',values=['Januari','Februari','Maret','April','Mei','Juni','Juli', 'Agustus','September','Oktober','November', 'Desember'])
        bulan2.grid(row=1, column=3)
        bulan2.current(0)

        # header tahun
        tahun2 = ttk.Combobox(self.login, state='readonly',values=year)
        tahun2.grid(row=1, column=4)
        tahun2.current(0)     

        # tabel data
        my_connect = mysql.connector.connect(
        host="localhost",
        user="python", 
        passwd="KaliLinux",
        database="ukm"
        )

        my_conn = my_connect.cursor()
        ####### end of connection ####
        my_conn.execute("SELECT * FROM laporanjurnal")

        i=2 
        j=3
        for student in my_conn: 
            for j in range(len(student)):
                e = Entry(self.login, width=20, fg='black') 
                e.grid(row=i, column=j, padx=0, pady=0) 
                e.insert(END, student[j])
            i=i+1
