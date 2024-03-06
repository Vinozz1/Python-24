print("\n<< Prima dan Komposit >>")
print("-"*15)

list = input("Masukkan angka-angka yang ingin diperiksa (pisahkan dengan koma): ").split(',')
dataNumber = [int(num) for num in list]

prima = []
komposit = {}

for number in dataNumber:
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
