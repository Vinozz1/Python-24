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
data2[ 0 ] = " xyz "
print(f"data2 updated = {data2}")
print(f"dataList2 updated = {dataList2}")

print("-"*15, "Nested List")
data1 = [ "I", "G", "S" ]
data1 = [ 10, 11, 12 ]
datalist = [ data1, "x", "y", "z", data2]
print( f"datalist = {datalist }")
print( f"datalist[0] = {datalist[0] }")
print( f"datalist[0][1] = {datalist[0][1] }")
datalist_copy = datalist.copy()
print(f"Memory Address datalist={hex(id(datalist))}")
print(f"Memory Address datalist_copy={hex(id(datalist_copy))}")
datalist[ -1 ][ -1] = 100
print(f"datalist updated = {datalist}")
print(f"datalist_copy updated = {datalist_copy}")

print("-"*15, "DeepCopy")
from copy import deepcopy
deta1s = deepcopy( datalist )
print(f"datalist = {datalist}")
print



