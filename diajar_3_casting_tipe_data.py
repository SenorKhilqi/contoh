#merubah dari suatu data ke tipe lainnya
#tipe data = int, float, str, bool

# INTEGER 
print ("===INTEGER===")
data_int = 9
print("data=", data_int, "type =", type(data_int))

data_float = float (data_int)
data_str = str (data_int)
data_bool = bool (data_int) #jika intr angka 0 maka akan false tapi dselain 0 akan true
print("data=", data_float, "type =", type(data_int))
print("data=", data_str, "type =", type(data_str))
print("data=", data_bool, "type =", type(data_bool)) 


## FLOAT
print ("===FLOAT===")
data_float = 9.8
print("data=", data_float, "type =", type(data_float))

data_int = int (data_float) #data tetap
data_str = str (data_float) #dibulatkan ke angka terkecil bukan terbesaar
data_bool = bool (data_float) #jika intr angka 0 maka akan false tapi dselain 0 akan true
print("data=", data_float, "type =", type(data_float))
print("data=", data_str, "type =", type(data_str))
print("data=", data_bool, "type =", type(data_bool)) 


### BOOLEAN
print ("===BOOLEAN===")
data_bool = True
print("data=", data_bool, "type =", type(data_bool))

data_float = float (data_bool)
data_str = str (data_bool)
data_int = int (data_bool)
print("data=", data_float, "type =", type(data_int))
print("data=", data_str, "type =", type(data_str))
print("data=", data_int, "type =", type(data_int)) 


#### STRING
print ("===STRING===")
data_str = "10"
print("data=", data_str, "type =", type(data_str))

data_float = float(data_str) #atring harus angka
data_bool = bool(data_str) #akan false jika string kosong
data_int = int  (data_str) #string harus angka
print("data=", data_float, "type =", type(data_float))
print("data=", data_bool, "type =", type(data_bool))
print("data=", data_int, "type =", type(data_int))
