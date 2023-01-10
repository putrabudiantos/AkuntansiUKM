from tkinter import *
from tkinter import ttk
import informasialert

# Top level window 

def tambahopsi():
    window = Tk()

    window.title("Jurnal Lanjutan")
    window.geometry('520x225')
    window.resizable(False, False)

    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("Today is", d2)

    # Judul Jurnal Lanjutan
    Label(window, text="Tambah Data Transaksi", font="courier,bold, 15").grid(row=0, column=0, columnspan=5, padx=20, pady=5)

    # Label Tanggal
    Label(window, text=d2, font="courier, 10").grid(row=1, column=0, columnspan=1, pady=8, padx=5, sticky=E)

    # Entry Deskripsi Nama Transaksi
    keteranganmenu2 = Entry(window, width=21)
    keteranganmenu2.insert(1, "Nama Transaksi")
    getketerangan2 = keteranganmenu2.get()
    keteranganmenu2.grid(row=1, column=1, sticky=E, columnspan=1)

    # Label Frame Perkiraan
    perkiraan = LabelFrame(window, text = "Perkiraan", width=20)
    perkiraan.grid(row=2, column=0, sticky=E, columnspan=1, pady=1)

    # combobox Perkiraan 1
    comboperkiraan = ttk.Combobox(perkiraan, state='readonly',values=[
        'Aktiva Lancar (D)',
        'Kas',
        'Bank',
        'Perlengkapan',
        'Persediaan Bahan Baku',
        'Persediaan Barang Dagang',
        'Sewa Dibayar Dimuka',
        'Aktiva Tetap (D)',
        'Tanah',
        'Bangunan',
        'Bangunan',
        'Kendaraan',
        'Peralatan',
        'Akumulasi Penyusutan (K)',
        'Akumulasi Penyusutan Kendaraan',
        'Akumulasi Penyusutan Peralatan',
        'Akumulasi Penyusutan Bangunan',
        'Utang Jangka Pendek (K)',
        'Utang Usaha',
        'Utang Jangka Panjang (K)',
        'Modal (K)',
        'Modal Pemilik',
        'Prive',
        'Pendapatan (K)',
        'Pendapatan',
        'Penjualan Barang',
        'Ikhtisar Laba/Rugi',
        'Potongan Penjualan',
        'Retur Penjualan',
        'Harga Pokok Penjualan (D)',
        'Harga Pokok Penjualan',
        'Potongan Pembelian',
        'Retur Pembelian',
        'Biaya Penjualan (D)',
        'Biaya Pengiriman',
        'Biaya Penjualan Lain-lain',
        'Biaya Admin dan Umum (D)',
        'Biaya Air',
        'Biaya Depresiasi Peralatan',
        'Biaya Gaji Karyawan',
        'Biaya Listrik',
        'Biaya Makan dan Minum',
        'Biaya Sewa Tempat Usaha',
        'Biaya Telepon',
        'Biaya Umum Lain-lain',
        'Beban Penyusutan Bangunan',
        'Beban Penyusutan Kendaraan',
        'Beban Penyusutan Peralatan',
        'Beban Piutang Tak Tertagih',
        'Pendapatan Diluar Usaha (K)',
        'Pendapatan Bunga Bank',
        'Pendapatan Hasil Panen',
        'Biaya Diluar Usaha (D)',
        'Biaya Administrasi Bank'])
    comboperkiraan.grid(row = 2, column=0, sticky=W, columnspan=1, pady=1)
    comboperkiraan.current(1)


    # combobox Perkiraan 2
    comboperkiraan = ttk.Combobox(perkiraan, state='readonly',values=[
        'Aktiva Lancar (D)',
        'Kas',
        'Bank',
        'Perlengkapan',
        'Persediaan Bahan Baku',
        'Persediaan Barang Dagang',
        'Sewa Dibayar Dimuka',
        'Aktiva Tetap (D)',
        'Tanah',
        'Bangunan',
        'Bangunan',
        'Kendaraan',
        'Peralatan',
        'Akumulasi Penyusutan (K)',
        'Akumulasi Penyusutan Kendaraan',
        'Akumulasi Penyusutan Peralatan',
        'Akumulasi Penyusutan Bangunan',
        'Utang Jangka Pendek (K)',
        'Utang Usaha',
        'Utang Jangka Panjang (K)',
        'Modal (K)',
        'Modal Pemilik',
        'Prive',
        'Pendapatan (K)',
        'Pendapatan',
        'Penjualan Barang',
        'Ikhtisar Laba/Rugi',
        'Potongan Penjualan',
        'Retur Penjualan',
        'Harga Pokok Penjualan (D)',
        'Harga Pokok Penjualan',
        'Potongan Pembelian',
        'Retur Pembelian',
        'Biaya Penjualan (D)',
        'Biaya Pengiriman',
        'Biaya Penjualan Lain-lain',
        'Biaya Admin dan Umum (D)',
        'Biaya Air',
        'Biaya Depresiasi Peralatan',
        'Biaya Gaji Karyawan',
        'Biaya Listrik',
        'Biaya Makan dan Minum',
        'Biaya Sewa Tempat Usaha',
        'Biaya Telepon',
        'Biaya Umum Lain-lain',
        'Beban Penyusutan Bangunan',
        'Beban Penyusutan Kendaraan',
        'Beban Penyusutan Peralatan',
        'Beban Piutang Tak Tertagih',
        'Pendapatan Diluar Usaha (K)',
        'Pendapatan Bunga Bank',
        'Pendapatan Hasil Panen',
        'Biaya Diluar Usaha (D)',
        'Biaya Administrasi Bank'])
    comboperkiraan.grid(row = 3, column=0, sticky=W, columnspan=1, pady=1)
    comboperkiraan.current(1)

    # Label Total
    Label(window, text='Total:', font="courier, 10").grid(row=4, column=0, columnspan=1, pady=8, padx=5, sticky=E)


    # Label Frame Debet
    debit = LabelFrame(window, text = "Debet", width=20)
    debit.grid(row=2, column=1, sticky=E, columnspan=1, pady=1)

    # Entry Nominal 1
    entrydebet1 = Entry(debit, width=21)
    entrydebet1.insert(1, "0")
    getketerangandebet1 = entrydebet1.get()
    entrydebet1.grid(row=2, column=0, sticky=E, columnspan=2)

    # Entry Nominal 2
    entrydebet2 = Entry(debit, width=21)
    entrydebet2.insert(1, "0")
    getketerangandebet2 = entrydebet2.get()
    entrydebet2.grid(row=3, column=0, sticky=E, columnspan=2)

    # Label Hasil debit
    Label(window, text='0', font="courier, 10").grid(row=4, column=1, columnspan=1, pady=8, padx=5, sticky=W)

    # tombol simpan sambah opsi
    tombolsimpantambahopsi = ttk.Button(window, text="Simpan", width=10, command=lambda: informasialert.Pesan(window).sukses()).grid(row=5, column=1, columnspan=1, pady=5)

    # Label Frame Kredit
    kredit = LabelFrame(window, text = "Kredit", width=20)
    kredit.grid(row=2, column=2, sticky=E, columnspan=1)

    # Entry Nominal 1
    entrykredit1 = Entry(kredit, width=21)
    entrykredit1.insert(1, "0")
    getketerangankredit1 = entrykredit1.get()
    entrykredit1.grid(row=2, column=0, sticky=E, columnspan=2)

    # Entry Nominal 2
    entrykredit2 = Entry(kredit, width=21)
    entrykredit2.insert(1, "0")
    getketerangankredit2 = entrykredit2.get()
    entrykredit2.grid(row=3, column=0, sticky=E, columnspan=2)

    # Label Hasil kredit
    Label(window, text='0', font="courier, 10").grid(row=4, column=2, columnspan=1, pady=8, padx=5, sticky=W)

    window.mainloop()