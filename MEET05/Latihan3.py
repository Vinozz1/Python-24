print("<< \t NOTA PENJUALAN - TOKO XYZ \t >>")
print("-"*42)

nama_barang = input("Nama barang\t: ")
harga_barang = int(input("Harga barang \t: "))
jumlah_beli = int(input("Jumlah beli\t: "))
subTotal = harga_barang * jumlah_beli
print(f"subTotal\t:Rp. {subTotal:>30,.0f}")

diskon = 0.2 * subTotal
print(f"diskon\t\t:Rp. {diskon:>30,.0f}")

total = subTotal - diskon
print(f"total\t\t:Rp. {total:>30,.0f}")

Besar_bayar = int(input("Total bayaran anda\t:Rp."))
print(f"Besar bayar\t:Rp. {Besar_bayar:>30,.0f}")

print("-"*42)
Kembalian = Besar_bayar - total
print(f"Kembalian\t:Rp. {Kembalian:>30,.0f}")

print("Rincian Kembalian:")
lembar_50 = Kembalian // 50000
sisakembalian1 = Kembalian % 50000
print(f"Rp 50.000\t\t: {lembar_50:>30,.0f} lembar")

lembar_20 = sisakembalian1 // 20000
sisakembalian2 = sisakembalian1 % 20000
print(f"Rp 20.000\t\t: {lembar_20:>30,.0f} lembar")

lembar_10 = sisakembalian2 // 10000
sisakembalian3 = sisakembalian2 % 10000
print(f"Rp 10.000\t\t: {lembar_10:>30,.0f} lembar")

lembar_5 = sisakembalian3 // 5000
sisakembalian4 = sisakembalian3 % 5000
print(f"Rp 5.000\t\t: {lembar_5:>30,.0f} lembar")

lembar_2 = sisakembalian4 // 2000
sisakembalian5 = sisakembalian4 % 2000
print(f"Rp 2.000\t\t: {lembar_2:>30,.0f} lembar")

lembar_1 = sisakembalian5 // 1000
print(f"Rp 1.000\t\t: {lembar_1:>30,.0f} lembar")