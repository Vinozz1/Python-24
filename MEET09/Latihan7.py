bilangan = int(input("Masukkan bilangan: "))

while bilangan % 2 == 0 or bilangan < 20 or (bilangan < 35 and bilangan > 25) or bilangan > 40:
    bilangan = int(input("Masukkan bilangan dalam rentang 10-15, 20-25, atau 35-40: "))

print("Benar")
