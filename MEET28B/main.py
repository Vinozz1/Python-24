import tkinter as tk
from tkinter import ttk
from Rumus.EnergiPotensial import EnergiPotensial
from Rumus.EnergiKinetik import EnergiKinetik
import ttkbootstrap as tb

class MainApplication(tb.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Kalkulator Energi")
        self.geometry("400x300")

        # Buat label untuk judul
        self.title_label = ttk.Label(self, text="Kalkulator Energi", font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        # Buat frame untuk pilihan energi
        self.option_frame = ttk.Frame(self)
        self.option_frame.pack(pady=10)

        # Buat tombol untuk energi potensial
        self.potensial_button = ttk.Button(self.option_frame, text="Energi Potensial", command=self.show_potensial)
        self.potensial_button.grid(row=0, column=0, padx=10)

        # Buat tombol untuk energi kinetik
        self.kinetik_button = ttk.Button(self.option_frame, text="Energi Kinetik", command=self.show_kinetik)
        self.kinetik_button.grid(row=0, column=1, padx=10)

        # Buat frame untuk masukan dan hasil
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=10)

        # Variabel String untuk menyimpan hasil
        self.result_var = tk.StringVar()

        # Buat label untuk menampilkan hasil
        self.result_label = ttk.Label(self.input_frame, textvariable=self.result_var, font=("Helvetica", 14))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def show_potensial(self):
        # Hapus frame masukan sebelumnya
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        # Buat label dan masukan untuk energi potensial
        self.massa_label = ttk.Label(self.input_frame, text="Massa (kg):")
        self.massa_label.grid(row=0, column=0, padx=10, pady=5)
        self.massa_entry = ttk.Entry(self.input_frame)
        self.massa_entry.grid(row=0, column=1, padx=10, pady=5)

        self.ketinggian_label = ttk.Label(self.input_frame, text="Ketinggian (m):")
        self.ketinggian_label.grid(row=1, column=0, padx=10, pady=5)
        self.ketinggian_entry = ttk.Entry(self.input_frame)
        self.ketinggian_entry.grid(row=1, column=1, padx=10, pady=5)

        self.show_button = ttk.Button(self.input_frame, text="Tampilkan Hasil", command=self.calculate_potensial)
        self.show_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_kinetik(self):
        # Hapus frame masukan sebelumnya
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        # Buat label dan masukan untuk energi kinetik
        self.massa_label = ttk.Label(self.input_frame, text="Massa (kg):")
        self.massa_label.grid(row=0, column=0, padx=10, pady=5)
        self.massa_entry = ttk.Entry(self.input_frame)
        self.massa_entry.grid(row=0, column=1, padx=10, pady=5)

        self.kecepatan_label = ttk.Label(self.input_frame, text="Kecepatan (m/s):")
        self.kecepatan_label.grid(row=1, column=0, padx=10, pady=5)
        self.kecepatan_entry = ttk.Entry(self.input_frame)
        self.kecepatan_entry.grid(row=1, column=1, padx=10, pady=5)

        self.show_button = ttk.Button(self.input_frame, text="Tampilkan Hasil", command=self.calculate_kinetik)
        self.show_button.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_potensial(self):
        try:
            massa = float(self.massa_entry.get())
            ketinggian = float(self.ketinggian_entry.get())
            gravitasi = 9.8  # Nilai gravitasi bumi, bisa disesuaikan dengan kebutuhan
            energi_potensial = EnergiPotensial(massa, gravitasi, ketinggian).hitung()
            self.result_var.set(f"Energi Potensial: {energi_potensial:.2f} Joule")
        except ValueError:
            self.result_var.set("Input tidak valid")

    def calculate_kinetik(self):
        try:
            massa = float(self.massa_entry.get())
            kecepatan = float(self.kecepatan_entry.get())
            energi_kinetik = EnergiKinetik(massa, kecepatan).hitung()
            self.result_var.set(f"Energi Kinetik: {energi_kinetik:.2f} Joule")
        except ValueError:
            self.result_var.set("Input tidak valid")

if __name__ == "__main__":
    root = MainApplication()
    root.mainloop()
