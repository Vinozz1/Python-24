'''
Aritmatika Python :
1. + (penjumlahan)
2. - ( pengurangan )
3. * ( perkalian )
4. / ( pembagian )
5. ** ( pangkat )
6. % ( modulus )
7. // ( Floor Division - hasil bagi )

Prioritas :
1. ()
2. **
3. * / % //
4. + -
'''

a = 4
b = 2

#Pejumlahan 
Hasil = a + b
# print( a, " + ", b, " = ", Hasil)
print( a, " + ", b, " = ", a + b)

#Pengurangan 
Hasil = a - b
print( a, " - ", b, " = ", Hasil)

#Perkalian
Hasil = a * b
print( a, " * ", b, " = ", Hasil)

#Pengurangan 
Hasil = a / b
print( a, " / ", b, " = ", Hasil)

#Modulus 
Hasil = a % b
print( a, " % ", b, " = ", Hasil)

#Pangkat 
Hasil = a ** b
print( a, " ** ", b, " = ", Hasil)

#Hasil bagi / Floor Division
Hasil = a // b
print( a, " // ", b, " = ", Hasil)

'''
Prioritas Operasi Aritmatika :
1. ()
2. **
3. * / % //
4. + -
'''

x = 4
y = 5
z = 6

Hasil = x * ( y - z)
print( " x * ( y - z ) =", Hasil)

hasil = ( x + y ) // ( z - y) ** x
print ( " ( x + y ) // ( z - y) ** x =", Hasil)
