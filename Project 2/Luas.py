import tkinter as tk
from tkinter import ttk as tema
from tkinter.messagebox import showinfo
import ttkbootstrap as tb
import subprocess

def back_to_main():
    root.destroy()
    subprocess.Popen(['python', 'main.py'])

root = tb.Window(themename="vapor")

Luas = tk.StringVar()
Alas = tk.IntVar()
Tinggi = tk.IntVar()
Sisi = tk.IntVar()
Jarijari = tk.IntVar()

def kirim():
    energi_hitung = 0
    if Luas.get() == "Lingkaran":
        energi_hitung = 3.14 * Jarijari.get()**2
    elif Luas.get() == "Persegi":
        energi_hitung = Sisi.get() **2
    elif Luas.get() == "Segitiga":
        energi_hitung = Tinggi.get() * Alas.get() / 2

    h = f"Luas {Luas.get()}: {energi_hitung:.2f}"
    showinfo(title="BIO", message=h)

root.title("Energi")
root.geometry("600x1000")
root.resizable(True, True)
root.config(bg="gray")


frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill="x", expand=True)

label_Alas = tema.Label(frame, text="Alas(m):")
label_Alas.pack(padx=10, pady=10, fill="x", expand=True)
form_Alas = tema.Entry(frame, textvariable=Alas)
form_Alas.pack(padx=10, pady=10, fill="x", expand=True)

label_Tinggi = tema.Label(frame, text="Ketinggian (m):")
label_Tinggi.pack(padx=10, pady=10, fill="x", expand=True)
form_Tinggi = tema.Entry(frame, textvariable=Tinggi)
form_Tinggi.pack(padx=10, pady=10, fill="x", expand=True)

label_Sisi = tema.Label(frame, text="Sisi (m):")
label_Sisi.pack(padx=10, pady=10, fill="x", expand=True)
form_Sisi = tema.Entry(frame, textvariable=Sisi)
form_Sisi.pack(padx=10, pady=10, fill="x", expand=True)

label_Jarijari = tema.Label(frame, text="Jari - jari (m):")
label_Jarijari.pack(padx=10, pady=10, fill="x", expand=True)
form_Jarijari = tema.Entry(frame, textvariable=Jarijari)
form_Jarijari.pack(padx=10, pady=10, fill="x", expand=True)

label_Luas = tema.Label(frame, text="Pilih Rumus Luas:")
label_Luas.pack(padx=10, pady=10, fill="x", expand=True)
ba1 = tema.Radiobutton(frame, value="Lingkaran", text="Lingkaran", variable=Luas)
ba1.pack(padx=10, fill="x", expand=True)
ba2 = tema.Radiobutton(frame, value="Persegi", text="Persegi", variable=Luas)
ba2.pack(padx=10, pady=10, fill="x", expand=True)
ba3 = tema.Radiobutton(frame, value="Segitiga", text="Segitiga", variable=Luas)
ba3.pack(padx=10, pady=10.5, fill="x", expand=True)

BTN = tema.Button(frame, text="KIRIM", command=kirim)
BTN.pack(padx=10, fill="x", expand=True)

back_button = tema.Button(frame, text="Kembali ke Menu Utama", command=back_to_main)
back_button.pack(padx=10, pady=10, fill="x", expand=True)

root.mainloop()