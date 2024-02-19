tinggi = int(input("masukan tinggi = ")) 

for i in range(1, tinggi + 1):
    print(" " * (tinggi - i) + "*" * (2 * i - 1))

for i in range(tinggi - 1, 0, -1):
    print(" " * (tinggi - i) + "*" * (2 * i - 1))


print("-"*20)

for i in range(1, 6):  
    print(" "  * (5 - i) + "*" * (2 * i - 1))

for i in range(4, 0, -1):  
    print(" " * (5 - i) + "*" * (2 * i - 1))

print("Butterfly pattern:")
for i in range(1, 6):
    print("+" * i + " " * (10 - 2 * i) + "+" * i)
for i in range(4, 0, -1):
    print("+" * i + " " * (10 - 2 * i) + "+" * i)