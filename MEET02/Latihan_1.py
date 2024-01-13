a = float(input("Masukkan Variabel a = "))
b = float(input("Masukkan Variabel b = "))
c = float(input("Masukkan Variabel c = "))

Hasil_1 = a * b - c
Hasil_2 = a + b / 23 // (a + c) * Hasil_1
Hasil_3 = 127 + (a - c + b) % Hasil_2 ** Hasil_1

print(" a * b - c =", Hasil_1)
print("a + b / 23 // (a + c) * Hasil_1=", Hasil_2)
print(" 127 + (a - c + b) % Hasil_2 ** Hasil_1=", Hasil_3)
