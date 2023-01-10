from tkinter import messagebox

class Pesan():
    def __init__(self, root):
        self.akars = root
        
    def sukses(self):
        messagebox.showinfo(title="Tersimpan",message="Data Telah disimpan")
        self.akars.destroy()

    def gagal(self):
        messagebox.showinfo(title="Tersimpan",message="Data gagal disimpan")
        self.akars.destroy()
        
    def kosong(self):
        messagebox.showinfo(title="Tersimpan",message="Data kosong mohon isi")

    def suksesconvert(self):
        messagebox.showinfo(title="Berhasil", message="Berhasil Mengkonvert ke XLS")

    def suksesterhubung(self):
        messagebox.showinfo(title="Berhasil", message="Berhasil Terhubung dengan Database")
