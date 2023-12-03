# OPERASI ARITMATIKA

a = 10
b = 3 

#operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil )
 
# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil )

# operasi peerkalian *
hasil = a * b
print(a,'*',b,'=',hasil )

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil )

# operasi eksponen atau pangkat **
hasil = a ** b
print(a,'**',b,'=',hasil )

# operasi modulus % (sisa dari pembagian) example 12 dibagi 5 sisa 2
hasil = a % b
print(a,'%',b,'=',hasil )

# operasi floor division // (jumlah yang dapat di bagi) example 20 dibagi 3 hanya dapat dibagi 6 kali
hasil = a // b
print(a,'//',b,'=',hasil )

#prioritas operasi, operational precedence
#......
#    1. ()
#    2. exponen **
#    3. perkalian dan teman-teman * / ** % //
#    4. pertamabahan dan pengurangan + - 
x= 3
y= 2
z=4

hasil = x ** y * z + x / y - y % z // x
print (x, '**', y,'*', z, '+', x, '/', y, '-', y, '%', z, '//', x ,'=',hasil )
# cara penghitungan seperti di matematika dasar PAKBATAKUR
# disini yang pertama () lalu ** lalu * lalu / lalu % lalu // lalu + lalu -

hasil = x + y * z
print (x, '+', y, '*', z, '=', hasil )

hasil = (x + y) * z
print ('(',x, '+', y,'), *', z, '=', hasil )