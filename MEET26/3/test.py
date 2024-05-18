import tkinter as tk
from tkinter import ttk as tema
from tkinter import messagebox
import random
import string
import os

def add_mapel():
    mapel = entry_mapel.get()
    guru = entry_guru.get()
    hari = entry_hari.get()
    jam = entry_jam.get()
    ruangan = entry_ruangan.get()

    if not all([mapel, guru, hari, jam, ruangan]):
        messagebox.showerror("Error", "Semua field harus diisi")
        return

    id_mapel = ''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices(string.digits, k=3))
    mata_pelajaran[id_mapel] = {"Mapel": mapel, "Guru": guru, "Hari": hari, "Jam": jam, "Ruangan": ruangan}

    clear_entries()
    messagebox.showinfo("Info", "Mata pelajaran berhasil ditambahkan")

def clear_entries():
    entry_mapel.delete(0, tk.END)
    entry_guru.delete(0, tk.END)
    entry_hari.delete(0, tk.END)
    entry_jam.delete(0, tk.END)
    entry_ruangan.delete(0, tk.END)

def kirim(message):
    messagebox.showinfo("BIO", message)

def show_mapel():
    message = "*"*10 + " DAFTAR MAPEL " + "*"*11 + "\n"
    
    for id_mapel, info in mata_pelajaran.items():
        message += f"Mapel: {info['Mapel']}\n"
        message += f"Guru: {info['Guru']}\n"
        message += f"Hari: {info['Hari']}\n"
        message += f"Jam: {info['Jam']}\n"
        message += f"Ruangan: {info['Ruangan']}\n"
        message += "*"*35 + "\n"

    message += "\nID\t\tMAPEL\t\t\tGURU\t\tHARI\t\tJAM\t\tRUANGAN\n"
    message += "*"*35 + "\n"
    
    for id_mapel, info in mata_pelajaran.items():
        message += f"{id_mapel}\t\t{info['Mapel']:20}\t{info['Guru']:15}\t{info['Hari']:10}\t{info['Jam']:10}\t{info['Ruangan']:10}\n"
    
    kirim(message)

# Inisialisasi tkinter
root = tk.Tk()
root.title("Daftar Mata Pelajaran")

# Frame
frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

mata_pelajaran = {}

# Form input
label_mapel = tema.Label(frame, text="Mapel")
label_mapel.pack(side="left")
entry_mapel = tema.Entry(frame)
entry_mapel.pack(side="left", padx=5, fill="x", expand=True)

label_guru = tema.Label(frame, text="Guru")
label_guru.pack(side="left")
entry_guru = tema.Entry(frame)
entry_guru.pack(side="left", padx=5, fill="x", expand=True)

label_hari = tema.Label(frame, text="Hari")
label_hari.pack(side="left")
entry_hari = tema.Entry(frame)
entry_hari.pack(side="left", padx=5, fill="x", expand=True)

label_jam = tema.Label(frame, text="Jam")
label_jam.pack(side="left")
entry_jam = tema.Entry(frame)
entry_jam.pack(side="left", padx=5, fill="x", expand=True)

label_ruangan = tema.Label(frame, text="Ruangan")
label_ruangan.pack(side="left")
entry_ruangan = tema.Entry(frame)
entry_ruangan.pack(side="left", padx=5, fill="x", expand=True)

button_submit = tema.Button(frame, text="Tambah", command=add_mapel)
button_submit.pack(side="left", padx=5, pady=10, fill="x", expand=True)

button_show = tema.Button(frame, text="Tampilkan Daftar Mapel", command=show_mapel)
button_show.pack(side="left", padx=5, pady=10, fill="x", expand=True)

# text_output = tk.Text(frame, wrap=tk.NONE, width=60, height=15)
# text_output.pack(side="top", padx=5, pady=10, fill="both", expand=True)

feedback_label = tema.Label(frame, text="")
feedback_label.pack(side="top", padx=5, pady=10, fill="both", expand=True)

root.mainloop()
