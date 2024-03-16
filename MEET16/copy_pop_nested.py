dataDict = {
    "plm": "Palembang",
    "em": "Muara Enim",
    "pr": "Prabumulih",
    "llg": "Lubuk Linggau"
}
data_copy = dataDict
dataDict["plm"] = "PALEMBANG"
print(f"DataDict = {dataDict}")
print(f"data_copy = {data_copy}")
data_copy2 = dataDict.copy()
dataDict["llg"] = "LUBUK LINGGAU"
print(f"DataDict = {dataDict}")
print(f"data_copy2 = {data_copy2}")

print("-" * 15, "POP")
data_pop = dataDict.pop("plm")
print(f"Data Pop = {data_pop}")
print(f"dataDict = {dataDict}")

print("-" * 15, "Popitems")
data_popitem = dataDict.popitem()  # Data menjadi tuple
print(f"data_popItem = {data_popitem}")
print(f"dataDict = {dataDict}")

print("-" * 15, "NESTED DICTIONARY")
dataNest = {
    "mobil1": {
        "merk": "push",
        "color": "red",
        "year": 2022
    },
    "mobil2": {
        "merk": "toyota",
        "color": "putih",
        "year": 2020
    }
}
print(f"Merk Mobil1 = {dataNest['mobil1']['merk']}")
print(f"Merk Mobil2 = {dataNest['mobil2']['merk']}")
print(f"color Mobil2 = {dataNest['mobil2']['color']}")

print("-" * 15, "DEEPCOPY")
from copy import deepcopy 
dataNest_copy = deepcopy(dataNest)
dataNest["mobil2"]["merk"] = "xenia"
print(f"dataNest= {dataNest}")
print(f"dataNest_copy= {dataNest_copy}")

print("-" * 15, "COMPREHENSION")
data = "ABC"
data1 = (i for i in data)  # ini jadi data set
print(f"data1 = {data1}, type = {type(data1)} ")
data1 = {i: i*3 for i in data}
print(f"data1 = {data1}, type = {type(data1)} ")
print("-" * 15, "2.COMPREHENSION")
data1 = ["x", "y", "z"]
data2 = [7, 8, 9]
dataFinal = {k: v**3 for k, v in zip(data1, data2)}
print(f"Data Final = {dataFinal}")

print("-" * 15, "3.COMPREHENSION")
data = {"ana": 85, "ibnu": 90, "indah": 100, "bunga": 86}
data = {k: v for k, v in data.items() if v > 85}
print(f"Data = {data}")
