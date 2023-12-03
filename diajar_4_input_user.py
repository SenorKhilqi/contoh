# INPUT USER

#data yang dimasukan pasti string
data = input ("masukan data: ")
print("data =" , data, ",type =",type(data))


#jika ingin mengambil int, float, maka
data_int = int(input("masukan angka: "))
print("data = ",data_int,",type =",type(data_int))


angka = float(input("masukan angka: "))
print("data = ",angka,",type =",type(angka))

#bagaimana dengan bool
#untuk mengambil data biner harus mengkasting terlebih dahulu dari integer (mencantumkan)
biner = bool (int (input("masukan nilai boolean : ")))
print("data = ",biner,",type =",type(biner))
