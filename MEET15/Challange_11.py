print("\n<< Prima dan Komposit >>")
print("-"*15)

minimal = int(input("Masukkan angka minimum: "))
maximal = int(input("Masukkan angka maksimum: "))

prima = []
komposit = {}

for number in range(minimal, maximal + 1):
    if number > 1:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                komposit[number] = None  
                break
        if is_prime:
            prima.append(number)

print("-"*15)
print("\n<< Prima >>")
print("-"*15)

print("Bilangan Prima:")
print(prima)

print("\n<< Komposit >>")
print("-"*15)

print("Bilangan Komposit:")
print(list(komposit.keys()))