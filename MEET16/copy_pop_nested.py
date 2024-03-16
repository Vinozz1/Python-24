dataDict = {
    "plm": "Palembang",
    "em": "Muara Enim",
    "pr": "Prabumulih",
    "llg": "LubukLinggau",
}
data_copy = dataDict.copy()
dataDict["plm"] = "PALEMBANG"
print(f"DataDict = {dataDict}")
print(f"data_copy = {data_copy}")

data_copy2 = dataDict.copy()
dataDict["llg"] = "LUBUKLINGGAU"
print(f"DataDict = {dataDict}")
print(f"data_copy2 = {data_copy2}")

print("-" * 15, "POP")
data_pop = dataDict.pop("plm")
print(f"data_pop = {data_pop}")
print(f"dataDict = {dataDict}")

print("-" * 15, "PopItem")
data_popItem = dataDict.popitem()  # data menjadi tuple
print(f"data_popItem = {data_popItem}")
print(f"dataDict = {dataDict}")

print("-" * 15, "NESTED DICTIONARY")
dataNest = {
    "mobill": {
        "merk": "rush",
        "color": "red",
        "year": 2022
    },
    "mobil2": {
        "merk": "avanza",
        "color": "putih",
        "year": 2020
    }
}
print(f"Merk Mobil1 = {dataNest['mobill']['merk']}")
print(f"Merk Mobil2 = {dataNest.get('mobil2').get('merk')}")
print(f"Color Mobil2 = {dataNest['mobil2']['color']}")

print("-" * 15, "DEEPCOPY")
from copy import deepcopy
dataNest_copy = deepcopy(dataNest)
dataNest["mobil2"]["merk"] = "Xenia"
print( f" dataNest = { dataNest}")
print( f" dataNest_copy= { dataNest_copy}")

print("-"*15, "COMPREHENSION")
data = "ABC"
data1 = { i for i in data } # ini jdi data set
print( f" data1 = { data1 }, type = { type ( data1 ) } ")
data1 =  { i : i for i in data }
print( f" data1 = { data1 }, type = { type ( data1) }")
print("-"*15, "2. COMPREHENSION")
data1 = [ "x", "y", "z"]
data2 = [ 7, 8, 9 ]
dataFinal = { k : v**3 for k,v in zip( data1, data2)}
print( f"Data final = {dataFinal}")