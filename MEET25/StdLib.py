# Standard Library, Ex
import os
import platform

if platform.system == "Windows":
    os.system("cls")
elif platform.system == "Linux":
    os.system("clear")
print("oke")
if os.name == "nt": #Windows
    os.system("cls")
else: # posix : linux - mac
    os.system("clear")
def batas():
    print("-"*15)
batas()
import math
print(f"Faktorial dari !6 = {math.factorial(6)}")
data = [ 2, 3, 6, 9, 5 ]
print(f"Jumlah data = {math.fsum(data)}")
batas()
import calendar
m = 5 
y  =  2024
print( calendar.month( m, y ))