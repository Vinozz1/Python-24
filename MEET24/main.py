import fisika
import time 

def batas():
    print("-"*15)

waktu_awal= time.time()

print( f"Massa jenis = { fisika.MassaJenis.MassaJenis(10 ,2) }")
print( f"Massa  = { fisika.MassaJenis.Massa(10 ,2) }")
print( f"Volume = { fisika.MassaJenis.Volume(10 ,2) }")

waktu_akhir = time.time()
print( f" Waktu yang dibutuhkan : {waktu_akhir - waktu_awal} ")

batas()
print( f"Usaha = { fisika.U( 12, 3)}")
print( f"Usaha = { fisika.G( 6, 2)}")
print( f"Usaha = { fisika.J( 9, 3)}")

batas()
print(f"Hasil Energi potensial = {fisika.Ep(4, 7, 4)}")
print(f"Hasil Energi kinetik = {fisika.Ek( 4, 8)}") 

batas()

diskon_10 = fisika.dc(10)
result = diskon_10(10000)
print(f"Diskon 10% = {result}")


