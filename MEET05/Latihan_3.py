print("<< \t Nota Penjualan - Toko XYX \t >>")
print( "_"*20 )
nama_barang = input( "Nama Barang\t: " )
harga_barang = int( input( "Harga Barang\t: " ) )
jumlah_beli = int( input( "Jumlah Beli\t: " ) )

subTotal = harga_barang * jumlah_beli
print(f"SubTotal\t: Rp. {subTotal:>20} ")

diskon = 0.2 * subTotal
print(f"Diskon\t\t: Rp. {diskon:>20.0f} ")

total = subTotal - diskon
print(f"Total Bayar\t: Rp. {total:>20.0f} ")

Besar_bayar = int(input("Besar bayar\t: "))
print("-"*20)
Kembalian = Besar_bayar - total
print(f"Kembalian\t\t: Rp. {Kembalian:>20.0f}")

print("Rincian Kembalian: ")
Hasil_1 = Kembalian // 50000
print(f"Rp.50000\t : {Hasil_1:.0f}  Lembar")
p1 = Hasil_1 % 50000

Hasil_2 = p1 // 20000
print(f"Rp.20000\t : {Hasil_2:.0f} Lembar")
p2 = Hasil_2 % 10000

Hasil_3 = p2 // 10000
print(f"Rp.10000\t : {Hasil_3:.0f} Lembar")

Hasil_4 = 8000 // 5000
print(f"Rp.5000\t : {Hasil_4:.0f} Lembar")

Hasil_5 = 3000 // 2000
print(f"Rp.2000\t : {Hasil_5:.0f} Lembar")

Hasil_6 = 1000 // 1000
print(f"Rp.1000\t : {Hasil_6:.0f} Lembar")