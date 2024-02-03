while True:
    bilangan = int(input("Masukkan bilangan ganjil lebih dari 20: "))

    if bilangan % 2 == 1 and bilangan > 20:
        print("Benar!")
        break
    else:
        print("False, try again !")
