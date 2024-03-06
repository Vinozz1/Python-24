#for
print("<<\t list dengan perulangan for: ")

data_list1 = {2,5,1,4,9,8}
for i in data_list1 :
    print(f"Data list 1 = {i}")

#for, range
print("<<\t list dengan perulangan for, range: ")

data_list1_panjang = len(data_list1)
for i in range(data_list1_panjang):
    print(f"Data list panjang 1 = {i}")

#while
print("<<\t list dengan perulangan while: ")
data_list2 = ["a","b","c",1]
i = 0
data_list2_panjang = len(data_list2)
while i<data_list2_panjang:
    print(f"Data list 2 = {data_list2[i]}")
    i+=1

#comprehension
print("<<\t list dengan comprehension: ")
[print(f"data list 2 : {i}")for i in data_list2]

#kuadrat
print("<<\t list dengan kuadrat :  ")
list3 = [1,5,3,4]
[print(f"data list 3 kuadrat : {i**2}")for i in list3]

#enumerate
print("<<\t list dengan enumerate :  ")
for index, data in enumerate(list3):
    print(f"{index+1}. {data}")

#list kosong
print("<<\t list kosong :  ")
list_4 = []
list_4.append("budi")
list_4.append("luigi")
list_4.append("budu")

print(f"List kosong = {list_4}")

