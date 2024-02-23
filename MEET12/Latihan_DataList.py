# data_list = []

# for i in range(2, 100, 2):
#     if i >= 10 and i <= 20:
#         data_list.append(i)

# for i in range(91, 101, 2):
#     data_list.append(i)

# print("<<< Latihan >>>")
# print("1.range(1,100)")
# print("2.value/item : genap (i >= 10 dan i <= 20 )")
# print("3.value/item : ganjil ( i >=90 dan i<= 100)")
# print("")
# print(data_list)


number = [i for i in range(1, 100) if (i >= 10 and i <= 20 and i % 2 == 0) or (i >= 90 and i <= 100 and i % 2 != 0)]

print("<<<      LATIHAN     >>>")
print("Berikut akan tampil list dengan kondisi:")
print("1. range(1,100)")
print("2. Hanya value/item : genap (i >=10 dan i <=20)")
print("3. Hanya value/item : ganjil (i >=90 dan i <=100)\n")

print(number)