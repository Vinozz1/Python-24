print("\n<<< FIBONACCI >>>\n")
print("-"*20)

data = int(input("Masukkan angka: "))
print("-"*20)

ListFebc = [1, 2]  
[ListFebc.append(ListFebc[i-1] + ListFebc[i-2]) for i in range(2, data)] 
print(ListFebc)

print("-"*5, "kedua", "-"*5)

variabel = int(input("Masukkan angka: "))
print("-"*20)

Listvariabel = [1, 2]  
for i in range(2, variabel):
    Listvariabel.append(Listvariabel[i-1] + Listvariabel[i-2])  

print(Listvariabel)

