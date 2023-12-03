# membuat gabungan area rentang dari angka
#  +++++++3--------10++++++++

inputUser = float(input("masukan angka bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n"))

# +++++3---------
# memeriksa angka kurang dari 3
isiKurangDari = (inputUser < 3)
print("kurang dari 3 =", isiKurangDari) 

# +++++10
isiLebihDari= (inputUser >10)
print ("lebih dari 10", isiLebihDari)

# membuat gabungan area rentang dari angka <3 atau >10 akan bernilai true sedangkan jika tidak termasuk kurang dari 3 atau lebih dari 10 akan bernilai fase
isCorrect = isiKurangDari or isiLebihDari
print('angka yang anda masukan :', isCorrect)

# -------3+++++++10-------
# kasus irisan (jadi angka yang true terdapat diantara 3 sampai 10)
inputUser = float(input(" masukan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10"))

# ------3++++++
# lebih dari 3
isiLebihDari = inputUser > 3
print("lebih dari 3 =", isiLebihDari)

# ++++10-----
# kurang dari 10
isiKurangDari = inputUser <10
print ("kurang dari 10=", isiKurangDari)

# ------3+++++++10
isCorrect = isiKurangDari or isiLebihDari
print('angka yang anda masukan :', isCorrect)

# masukan angka 
# -------0+++++++5------8+++++++++11------
