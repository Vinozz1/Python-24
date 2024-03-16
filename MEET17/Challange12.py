import random
import string
import os

hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

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

os.system("cls" if os.name == "nt" else "clear")

print("*"*10,"DAFTAR MAPEL", "*"*11)
for id_mapel, info in mata_pelajaran.items():
    print("Mapel:", info['Mapel'])
    print("Guru:", info['Guru'])
    print("Hari:", info['Hari'])
    print("Jam:", info['Jam'])
    print("Ruangan:", info['Ruangan'])
    print("*"*35)

print("\nID\t\tMAPEL\t\t\tGURU\t\tHARI\t\tJAM\t\tRUANGAN")
print("*"*35)
for id_mapel, info in mata_pelajaran.items():
    print(f"{id_mapel}\t\t{info['Mapel']:20}\t{info['Guru']:15}\t{info['Hari']:10}\t{info['Jam']:10}\t{info['Ruangan']:10}")
