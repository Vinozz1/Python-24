#Operator Assignment :
# 1. =
# 2. +=
# 3. -=
# 4. *=
# 5. /=
# 6. %=
# 7. //=
# 8. **=

print("-"*15, "+=")
a = 10
a += 3 # a = a + 3
print( "a = ", a)

print("-"*15, "-=")
a = 10
a -= 3 # a = a - 3
print( "a = ", a)

print("-"*15, "*=")
a = 10
a *= 3 # a = a * 3
print( "a = ", a)

print("-"*15, "/=")
a = 10
a /= 3 # a = a / 3
print( "a = ", a)

print("-"*15, "%=")
a = 10
a %= 3 # a = a % 3
print( "a = ", a)

print("-"*15, "//=")
a = 10
a //= 3 # a = a // 3
print( "a = ", a)

print("-"*15, "**=")
a = 10
a **= 3 # a = a ** 3
print( "a = ", a)

# Operator Assignment ( Logika )
#1. &
#2. |
#3. ^

print("-"*15, "&")
x = True
x &= False
print( "True & False =", x)

x = True
x &= True
print( "True & True = ", x)

print("-"*15, "|")
x = True
x |= False
print( "True | False =", x)

x = True
x ^= True
print( "True ^ True = ", x)

print("-"*15, "^")
x = True
x ^= False
print( "True ^ False =", x)

x = True
x ^= True # x = True ^True
print( "True ^ True = ", x)