import os
from statistics import median, mode

def mean(*args):
    total = sum(args)
    count = len(args)
    if count == 0:
        return 0
    return total / count

def main():
    numbers = []
    Deret_Angka = []   
    while True:
        os.system('cls') 
        input_numbers = input("Masukkan angka : ")
        if input_numbers.replace('.', '', 1).isdigit(): 
            data_numbers = float(input_numbers)
            numbers.append(data_numbers)
            Deret_Angka.append(data_numbers)  
        else:
            print("Invalid.")
            continue
        lanjut = input("Lanjut (y/n) : ")
        if lanjut.lower() != 'y':
            break

    if numbers:
        DataMean = mean(*numbers)
        DataMedian = median(numbers)
        DataModus = mode(numbers)
        print("Deret angka :", Deret_Angka)
        print(f"Mean : {DataMean:.1f}")           
        print(f"Median : {DataMedian:.0f}")      
        print(f"Modus : [{DataModus:.0f}]")         
    else:
        print("Invalid.")

main()
