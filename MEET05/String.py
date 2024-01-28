data = "ini string"
print("data =", type(data) )

# Ada 2 cara membuat string di python,
#1. Double Qoute
#2. Single Qoute

data = " Ini menggunakan Double Qoute "
print(data)
data = ' Ini menggunakan Single Qoute '
print(data)

print("' Tester 1 '")
print('" Tester 2 "')

#String dengan simbol \ 
print( " Hari jum'at " )
print( ' Hari jum\'at ' )

#\n
print( "\nKalimat Pertama \nKalimat kedua \nKalimat ketiga" )

#backslash
print( "c:\\user\\juan fans Gojo nomor 1" )

#backspace
print("Lebih \bDekat")

#Literal String dan Raw
print("""
Nama  : JUan penye gojo
Kelas : 10
""")

# raw : untuk mengabaikan string apapun yang tampil
print( r"c:\new folder")

#Literal String and Raw
print(r"""
Nama  : juan 
Kelas : 9\nine
alamat: plg
""")