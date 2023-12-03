# operasi logika atau boolean

# not, or, and, xor

# NOT
print ("======= NOT =======")
a = True
b = not a
print ("data a =",a)
print ("--------- NOT")
print ("data b =",b)

# OR (salah satu true akan menghasilkan true)
print ("===== OR =====")
a = False
b = False
c = a or b 
print (a ,"OR", b,"=",c )
a = False
b = True
c = a or b 
print (a ,"OR", b," =",c )
a = True
b = False
c = a or b 
print (a ," OR", b,"=",c )
a = True
b = True
c = a or b 
print (a ," OR", b," =",c )

# AND (keduanya harus true)
print ("===== AND =====")
a = False
b = False
c = a and b 
print (a ,"AND", b,"=",c )
a = False
b = True
c = a and b 
print (a ,"AND", b," =",c )
a = True
b = False
c = a and b 
print (a ," AND", b,"=",c )
a = True
b = True
c = a and b 
print (a ," AND", b," =",c )

# XOR (jika keduanya adalah true atau false maka akan menghasilkan false, tetapi jika salha satunya true atau false maka akan menghasilakan true)
print ("====XOR =====")
a = False
b = False
c = a ^ b 
print (a ,"XOR", b,"=",c )
a = False
b = True
c = a ^ b 
print (a ,"XOR", b," =",c )
a = True
b = False
c = a ^ b 
print (a ," XOR", b,"=",c )
a = True
b = True
c = a ^ b 
print (a ," XOR", b," =",c )