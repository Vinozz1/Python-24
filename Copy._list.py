#cara copy yg slh
data_1 = ["i","g","s"]
data_2 = data_1

print(f"Data 1 = {data_1}")
print(f"Data 2 = {data_2}")

data_1[0] = "Ai"
print(f"Data 1 setelah update = {data_1}")
print(f"Data 2 setelah update = {data_2}")

#alamat data 

print(f"Address memory data 1 = {hex(id(data_1))}")
print(f"Address memory data 2 = {hex(id(data_2))}")


print("-"*30)
#cara copy
data_3 = ["a","b","c"]
data_4 = data_3.copy()
print(f"Data 3 = {data_3}")
print(f"Data 4 = {data_4}")

#diupdate data salah satu saja
data_3[1] = "w"
print(f"Data 3 update = {data_3}")
print(f"Data 4 update = {data_4}")
print(f"Address memory data 3 = {hex(id(data_3))}")
print(f"Address memory data 4 = {hex(id(data_4))}")
