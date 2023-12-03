opsi_1 = input ("gamon (yes/no) ")
opsi_2 = input ("mencari yang baru (yes/no) ")
if opsi_1 == "no" and opsi_2 == "yes":
    hasil = "Anda menggunakan logika"
    # logika akan berfungsi sepenuhnya jika perasaan terhapus
else:
    hasil = "Anda menggunakan perasaan"
    # logika tidak akan berfungsi sepenuhnya jika perasaan masih ada
print(f"{hasil}")
