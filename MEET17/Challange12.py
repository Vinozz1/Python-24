import random
import string
import os

hari = ["Senin", "Selasa", "Rabu", "Kamis", "Ju'mat", "Sabtu"]

mata_pelajaran = {}
lanjut = True
while lanjut:
    print("*"*10,"DAFTAR MAPEL", "*"*11)
    mapel = input("Mapel: ")
    guru = input("Guru: ")
    hari_kelas = input("Hari: ")
    jam_kelas = input("Jam: ")
    ruangan = input("Ruangan: ")
    
    id_mapel = ''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices(string.digits, k=3))

    mata_pelajaran[id_mapel] = {"Mapel": mapel, "Guru": guru, "Hari": hari_kelas, "Jam": jam_kelas, "Ruangan": ruangan}

    continue_input = input("Lanjut (y/t)? ")
    if continue_input.lower() != 'y':
        lanjut = False

print("Lanjut (y/t)?", continue_input)

os.system("cls" if os.name == "nt" else "clear")

print("*"*10,"DAFTAR MAPEL", "*"*11)
print("Mapel:", mapel)
print("Guru:", guru)
print("Hari:", hari_kelas)
print("Jam:", jam_kelas)
print("Ruangan:", ruangan)

print("*"*35)
print("\nID\t\tMAPEL\t\t\tGURU\t\tHARI\t\tJAM\t\tRUANGAN")
print("*"*35)
for id_mapel, info in mata_pelajaran.items():
    print(f"{id_mapel}\t\t{info['Mapel']:20}\t{info['Guru']:15}\t{info['Hari']:10}\t{info['Jam']:10}\t{info['Ruangan']:10}")
