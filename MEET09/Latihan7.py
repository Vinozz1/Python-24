while True:
    bilangan = int(input("Masukkan bilangan: "))

    if (10 < bilangan < 15) or (20 < bilangan < 25) or (35 < bilangan < 40):
        print("Benar")
        break
    else:
        print("False, try again !")
