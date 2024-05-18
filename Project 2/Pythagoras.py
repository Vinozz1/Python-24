import tkinter as tk
from tkinter import ttk as tema
from tkinter.messagebox import showinfo
import ttkbootstrap as tb
import subprocess

def back_to_main():
    root.destroy()
    subprocess.Popen(['python', 'main.py'])

root = tb.Window(themename="vapor")

a = tk.IntVar()
b = tk.IntVar()
c = tk.IntVar()

def hitung_rumus():
    valueA = a.get()
    valueB = b.get()

    valueC = (valueA**2 + valueB**2)**0.5

    c.set(valueC)
    entry_c.config(textvariable=c)  

root.title("Rumus Pythagoras")
root.geometry("400x400")
root.resizable(True, True)
root.config(bg="gray")

frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

label_a = tema.Label(frame, text="Panjang Sisi A:")
label_a.pack(padx=10, pady=5, fill="x", expand=True)
entry_a = tema.Entry(frame, textvariable=a)
entry_a.pack(padx=10, pady=5, fill="x", expand=True)

label_b = tema.Label(frame, text="Panjang Sisi B:")
label_b.pack(padx=10, pady=5, fill="x", expand=True)
entry_b = tema.Entry(frame, textvariable=b)
entry_b.pack(padx=10, pady=5, fill="x", expand=True)

button_hitung = tema.Button(frame, text="Hitung", command=hitung_rumus)
button_hitung.pack(padx=10, pady=10, fill="x", expand=True)

label_c = tema.Label(frame, text="Panjang Sisi C :")
label_c.pack(padx=10, pady=5, fill="x", expand=True)
entry_c = tema.Entry(frame, textvariable=c, state="readonly")
entry_c.pack(padx=10, pady=5, fill="x", expand=True)

back_button = tema.Button(frame, text="Kembali ke Menu Utama", command=back_to_main)
back_button.pack(padx=10, pady=10, fill="x", expand=True)

root.mainloop()
