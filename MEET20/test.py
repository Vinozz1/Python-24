import os

def mean(*args):
    total = sum(args)
    count = len(args)
    if count == 0:
        return 0
    return total / count

def main():
    numbers = []
    while True:
        os.system('cls')  
        input_numbers = input("Masukkan angka : ")
        if input_numbers.replace('.', '', 1).isdigit(): 
            data_numbers = float(input_numbers)
            numbers.append(data_numbers)
        else:
            print("Invalid.")
            continue
        
        lanjut = input("Lanjut (y/n) : ")
        if lanjut.lower() != 'y':
            break

    if numbers:
        avg = mean(*numbers)
        print(f"Hasil mean dari data : {numbers} = {avg:.2f}")
    else:
        print("Invalid.")

main()
