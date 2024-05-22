import tkinter as tk
import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def open_energi():
    energi_path = os.path.join(script_dir, 'Energi.py')
    subprocess.Popen(['python', energi_path])

def open_pythagoras():
    pythagoras_path = os.path.join(script_dir, 'Pythagoras.py')
    subprocess.Popen(['python', pythagoras_path])

def open_Luas():
    luas_path = os.path.join(script_dir, 'Luas.py')
    subprocess.Popen(['python', luas_path])

root = tk.Tk()
root.title("Main Menu")
root.geometry("400x600")
root.resizable(False, False)
root.config(bg="gray")

energi_button = tk.Button(root, text="Energi", command=open_energi)
energi_button.pack(pady=10)

pythagoras_button = tk.Button(root, text="Pythagoras", command=open_pythagoras)
pythagoras_button.pack(pady=10)

luas_button = tk.Button(root, text="Luas", command=open_Luas)
luas_button.pack(pady=10)

root.mainloop()
