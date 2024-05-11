#class in python 
class Mobil():
    # var class
    JmlMobil = 0
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
        Mobil.JmlMobil += 1
    def TampilMobil(self):
        print(f"Mobilku {self.merk}")
    def ubahWarna(self, warnaBaru ):
        self.warna = warnaBaru

print( f"sebelum. Jumlah Data Mobil = {Mobil.JmlMobil}")
MobilAvanza = Mobil("Mclarren Sena", "Kuning", 2024)
MobilXenia = Mobil("Aventador", "Pink", 2023)
MobilRush = Mobil("Aston Martin DBX", "Biru", 2022)
print( f"Jumlah Data Mobil = {Mobil.JmlMobil}")
MobilAvanza.TampilMobil()
MobilXenia.TampilMobil()
print( f"Mobilku {MobilRush.merk} warna{MobilRush.warna} pada tahun {MobilRush.tahun}")
MobilAvanza.ubahWarna("hijau")
print(f"Warna baru {MobilAvanza.merk} = {MobilAvanza.warna}")