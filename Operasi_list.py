#ambil item/value dalam list
#     0/-3       1/-2       2/-1 
data_list = ["Ignatius", "Global", "School"]
print(f"Data list -2 = {data_list[-2]}")

print("-"*35)
# ambil tertentu di value list
data_list2 = [1,2,3,4,"a","b"]
print(f"Data list2[1:3] = {data_list2[1:3]}")
print(f"Data list2[2:-1] = {data_list2[2:-1]}")
print(f"Data list2[3:] = {data_list2[3:]}")

print("-"*35)
#Menggabugkan list mwnggunakan tambah
data1 = [1,2,3,4,5,5]
data2= ["b","c","d"]

print(f"Hasil gabun+ data 1 dan data 2 = {data1+data2}")

#Menggunakan extend
data1.extend(data2)
print(f"Hasil gabung extend data 1 dan 2 = {data1}")

print("-"*30)
#Menghitung jumlah value/angka (misal : 1,2,3, disini ada 3 value/angka.) 
#dalam list : len
print(f"Jumlah value/item di data 1 = {len(data1)}")

print("-"*30)
#Repetition atau pengulangan
data_rep= ["x","y"]*3
print(f"Data repetition = {data_rep}")

print("-"*30)
data3= ["Kuning","Merah","Hijau"]
if "Kuning"in data3:
    print("benar")
else:
    print("Salah")

print("-"*30)
#List dalam perulangan

for i in ["Ayam","Bebek",'Ikan']:
    print(f"Value dari i adalah = {i}" )

print("-"*30)
#Menambahkan value dalam list di awal
data_list.insert(0,"SMA")
print(f"Data list setelah di insert = {data_list}" )

#menambahkan kata/value dalam list di akhir
data_list.append("oke")
print(f"Data list setelah di append = {data_list}" )


print("-"*30)
#untuk mengganti kata yang diinginkan.(-1 it lokasi)
data_list[-1]="Sangat keren"
print(f"Data list setelah di update = {data_list}" )

print("-"*30)
#menghapus item/ value dalam list
data_list.remove("SMA")
print(f"Data list setelah di remove = {data_list}" )

print("-"*30)
#menghapus kata/value di akhir 
data_list.pop()
print(f"Data list setelah di pop= {data_list}" )

print("-"*30)
data_angka = [1,2,24,856,90,3,34,41,12,2,2,1]
print(f"Value/kata dari angka 41 di dalam list diatas adalah = {data_angka.index(41)}" )

print("-"*30)
#Menghitung berapa banyak value/angka di dalam sebuah list
print(f"Jumlah angka 2 di dalam list diatas = {data_angka.count(2)}")
print(f"Jumlah angka 1 di dalam list diatas = {data_angka.count(1)}")

print("-"*30)
#mencari angka/value yang paling kecil atau yang paling besar di dalam list
print(f"Angka terkecil di list angka diatas adalah = {min(data_angka)}")
print(f"Angka terbesar di list angka diatas adalah = {max(data_angka)}")

print("-"*30)
#mengurutkan angka/value dari yg terkecil di dalam list
data_angka.sort()
print(f"Urutan angka/value dari yang terkecil di dalam list angka = {data_angka}")

print("-"*30)
#mengurutkan angka/value dari yang terbesar
data_angka.reverse()
print(f"Urutan angka/value dari yang terbesar di dalam list angka = {data_angka}")