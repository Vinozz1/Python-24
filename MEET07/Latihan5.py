x = int(input("Masukkan koordinat x: "))
y = int(input("Masukkan koordinat y: "))

if x > 0 and y > 0:
    kuadran = "I"
elif x < 0 and y > 0:
    kuadran = "II"
elif x < 0 and y < 0:
    kuadran = "III"
elif x > 0 and y < 0:
    kuadran = "IV"
else:
    kuadran = "Titik Pusat"

print(f"Koordinat ({x},{y}) berada di kuadran {kuadran}")
