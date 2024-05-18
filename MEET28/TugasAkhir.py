import tkinter as tk
from tkinter import ttk as tema
from tkinter.messagebox import showinfo
import ttkbootstrap as tb

root = tb.Window(themename="vapor")

energi = tk.StringVar()
massa = tk.IntVar()
kecepatan = tk.IntVar()
gravitasi = tk.IntVar(value=10)
ketinggian = tk.IntVar()

def kirim():
    energi_hitung = 0
    if energi.get() == "Energi Kinetik":
        energi_hitung = 0.5 * massa.get() * kecepatan.get()**2
    elif energi.get() == "Energi Potensial":
        energi_hitung = massa.get() * gravitasi.get() * ketinggian.get()

    h = f"Energi {energi.get()}: {energi_hitung:.2f}"
    showinfo(title="BIO", message=h)

root.title("Energi")
root.geometry("400x600")
root.resizable(False, False)
root.config(bg="gray")

frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill="x", expand=True)

label_massa = tema.Label(frame, text="Massa (kg):")
label_massa.pack(padx=10, pady=10, fill="x", expand=True)
form_massa = tema.Entry(frame, textvariable=massa)
form_massa.pack(padx=10, pady=10, fill="x", expand=True)

label_kecepatan = tema.Label(frame, text="Kecepatan (m/s):")
label_kecepatan.pack(padx=10, pady=10, fill="x", expand=True)
form_kecepatan = tema.Entry(frame, textvariable=kecepatan)
form_kecepatan.pack(padx=10, pady=10, fill="x", expand=True)

label_gravitasi = tema.Label(frame, text="Gravitasi (m/s^2):")
label_gravitasi.pack(padx=10, pady=10, fill="x", expand=True)
form_gravitasi = tema.Entry(frame, textvariable=gravitasi)
form_gravitasi.pack(padx=10, pady=10, fill="x", expand=True)

label_ketinggian = tema.Label(frame, text="Ketinggian (m):")
label_ketinggian.pack(padx=10, pady=10, fill="x", expand=True)
form_ketinggian = tema.Entry(frame, textvariable=ketinggian)
form_ketinggian.pack(padx=10, pady=10, fill="x", expand=True)

label_energi = tema.Label(frame, text="Pilih Jenis Energi:")
label_energi.pack(padx=10, pady=10, fill="x", expand=True)
ba1 = tema.Radiobutton(frame, value="Energi Kinetik", text="Energi Kinetik", variable=energi)
ba1.pack(padx=10, fill="x", expand=True)
ba2 = tema.Radiobutton(frame, value="Energi Potensial", text="Energi Potensial", variable=energi)
ba2.pack(padx=10, pady=10, fill="x", expand=True)

BTN = tema.Button(frame, text="KIRIM", command=kirim)
BTN.pack(padx=10, fill="x", expand=True)

root.mainloop()
