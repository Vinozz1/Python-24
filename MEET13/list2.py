#enumerate
dataLs = [ "a", "b", 1, 2 ]
for index, data in enumerate(dataLs):
    print( f" {index} . {data} " )

print("-"*15)
#Empty List
dataLs = []
dataLs.append( 1 )
dataLs.append( 2 )
dataLs.append( 3 )
print( f"{dataLs}" )

print( "-"*15 )
# list : any dan all
data1 = [ True, True, False ]
print( f"Result any = { any(data1)} || all { all(data1)} " )
data1 = [ False, True, True ]
print( f"Result any = { any(data1)} || all { all(data1)} " )
data1 = [ ]
print( f"Result any = { any(data1)} || all { all(data1)} " )

#Comprehension 2/19/2023
data = [ i for i in range(1,10) ]
print( data )

data = [ i*3 for i in range(1,10) ]
print( f"data*3 = { data }" )

print("-"*15)
data = [ i for i in range(10) if i % 2 == 0 ]
print( f"data genap = { data }")

data = []
for i in range ( 1, 10):
    if i % 2 == 0:
        data.append( i )
