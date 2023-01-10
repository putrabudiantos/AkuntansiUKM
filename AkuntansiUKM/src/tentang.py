from tkinter import * 
import tkinter as tk

def tentang(root):
    #deskripsi
    descriptions = """
    Aplikasi ini dibuat untuk para UKM untuk menunjang mobilitas dan kemudahan dalam pembukuan keuangan dalam usaha tersebut dan aplikasi ini didesign secara mudah agar pengguna dapat menggunakannya dengan mudah. 
    """
    tentangku = Toplevel(root)
    tentangku.geometry("500x200")
    tentangku.title("Tentang")
    tentangku.resizable(False, False)
    Label(tentangku, text="Versi Aplikasi v.0.9 Beta", font="courier, 12").pack(padx=10, pady=10)
    T = Text(tentangku, height = 6, width = 55)
    T.pack()
    T.insert(tk.END, descriptions)
    exits = Button(tentangku, text="Kembali", command=lambda: tentangku.destroy()).pack(pady=7)
    print("Menu child about ditekan")