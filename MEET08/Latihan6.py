print("\t\t TIKET BUS \t")
print("-" * 20)

harga_tiket = {
    1: {'ekonomi': 100000, 'bisnis': 400000, 'eksekutif': 700000},
    2: {'ekonomi': 200000, 'bisnis': 500000, 'eksekutif': 800000},
    3: {'ekonomi': 300000, 'bisnis': 600000, 'eksekutif': 900000}
}

print("Pilihan kota:")
print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuklinggau")
pilihan_kota = int(input("Masukkan angka untuk pilihan kota (1/2/3): "))

print("Pilihan kelas:")
print("1. Ekonomi")
print("2. Bisnis")
print("3. Eksekutif")
kode_kelas = int(input("Masukkan angka untuk pilihan kelas (1/2/3): "))

banyak_tiket = int(input("Masukkan jumlah tiket: "))

harga_per_tiket = 0

if pilihan_kota == 1:
    if kode_kelas == 1:
        harga_per_tiket = harga_tiket[1]['ekonomi']
    elif kode_kelas == 2:
        harga_per_tiket = harga_tiket[1]['bisnis']
    elif kode_kelas == 3:
        harga_per_tiket = harga_tiket[1]['eksekutif']
elif pilihan_kota == 2:
    if kode_kelas == 1:
        harga_per_tiket = harga_tiket[2]['ekonomi']
    elif kode_kelas == 2:
        harga_per_tiket = harga_tiket[2]['bisnis']
    elif kode_kelas == 3:
        harga_per_tiket = harga_tiket[2]['eksekutif']
elif pilihan_kota == 3:
    if kode_kelas == 1:
        harga_per_tiket = harga_tiket[3]['ekonomi']
    elif kode_kelas == 2:
        harga_per_tiket = harga_tiket[3]['bisnis']
    elif kode_kelas == 3:
        harga_per_tiket = harga_tiket[3]['eksekutif']

sub_total = banyak_tiket * harga_per_tiket

diskon = 0

if (pilihan_kota == 2 and kode_kelas == 1) or (pilihan_kota == 3 and kode_kelas == 3):
    kode_promo = input("Masukkan kode promo: ")
    if kode_promo == "igs":
        diskon = 0.1 * sub_total

total_bayar = sub_total - diskon

print(f"\nSubtotal: Rp {sub_total:,}")
print(f"Diskon: Rp {diskon:,}")
print(f"Total Bayar: Rp {total_bayar:,}")
