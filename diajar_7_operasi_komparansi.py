# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,<=,>=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print ('======== lebih besar dari (>)')
hasil = a > 3
print (a,'>',3,'=',hasil)
hasil = b > 2
print (b,'>',2,'=',hasil)
hasil = a > 4
print (a,'>',4,'=',hasil)
hasil = b > 2
print (b,'>',2,'=',hasil)

# kurang dari dari <
print ('======== kurang dari dari (<)')
hasil = a < 3
print (a,'<',3,'=',hasil)
hasil = b < 2
print (b,'<',2,'=',hasil)
hasil = a < 4
print (a,'<',4,'=',hasil)
hasil = b < 2
print (b,'<',2,'=',hasil)

# lebih dari dari sama dengan >=
print ('======== lebih besar dari sama dengan (>=)')
hasil = a >= 3
print (a,'>=',3,'=',hasil)
hasil = b >= 2
print (b,'>=',2,'=',hasil)
hasil = a >= 4
print (a,'>=',4,'=',hasil)
hasil = b >= 2
print (b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print ('======== kurang dari sama dengan (<=)')
hasil = a <= 3
print (a,'<=',3,'=',hasil)
hasil = b <= 2
print (b,'<=',2,'=',hasil)
hasil = a <= 4
print (a,'<=',4,'=',hasil)
hasil = b <= 2
print (b,'<=',2,'=',hasil)

#  ==sama dengan 
# jika sama dengannya satu (=)itu adalah achivment
# jika sama dengannya dua (==) itu adalah perbandingan atau membandingkan
print ('======== sama dengan (==)')
hasil = a == 3
print (a,'==',3,'=',hasil)
hasil = b == 2
print (b,'==',2,'=',hasil)
hasil = a == 4
print (a,'==',4,'=',hasil)
hasil = b == 2
print (b,'==',2,'=',hasil)

# tidak sama dengan !=
print ('======== samadengan (!=)')
hasil = a != 3
print (a,'!=',3,'=',hasil)
hasil = b != 2
print (b,'!=',2,'=',hasil)
hasil = a != 4
print (a,'!=',4,'=',hasil)
hasil = b != 2
print (b,'!=',2,'=',hasil)

# is sebagai komparasi object
print ('======= object identity(is)')
x = 5 # ini adalah assigment membuat object
y = 5
print ('nilai x =,',x,',id=',hex(id(x)))
print ('nilai y =,',x,',id=',hex(id(y  )))
hasil = x is y
print ('x is y =',hasil)

x = 5 # ini adalah assigment membuat object
y = 6
print ('nilai x =,',x,',id=',hex(id(x)))
print ('nilai y =,',x,',id=',hex(id(y  )))
hasil = x is y
print ('x is y =',hasil)

# is sebagai komparasi object
print ('======= object identity(is not)')
x = 5 # ini adalah assigment membuat object
y = 5
print ('nilai x =,',x,',id=',hex(id(x)))
print ('nilai y =,',x,',id=',hex(id(y  )))
hasil = x is not y
print ('x is not y =',hasil)

x = 5 # ini adalah assigment membuat object
y = 6
print ('nilai x =,',x,',id=',hex(id(x)))
print ('nilai y =,',x,',id=',hex(id(y  )))
hasil = x is not y
print ('x is not y =',hasil)
