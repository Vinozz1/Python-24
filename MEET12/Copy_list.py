#copy
data1 = [1,2,3,4]
data2 = ["a","b","c"]
dataList1 = data1 
print(f"data1 = {data1}")
print(f"dataList1 = {dataList1}")
data1[-1] = 100
print(f"data1 UPDATE= {data1}")
print(f"dataList1 UPDATE= {dataList1}")
print(f"Memory Address data1 = {hex(id(data1))}")
print(f"Memory Address dataList1 = {hex(id(dataList1))}")
print("-"*15)
dataList2 = data2.copy()
print(f"Memory Address data2 = {hex(id(data2))}")
print(f"Memory Address dataList2 = {hex(id(dataList2))}")