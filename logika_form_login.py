data_1 = input ("username ")
data_2 = input ("password ")
if data_1 == "senor" and data_2 == "mademoiselle":
    hasil = "berhasil masuk"
elif data_1 == "senor" and not data_2 == "mademoiselle":
    hasil = "password salah"
elif not data_1 == "senor" and  data_2 == "mademoiselle":
    hasil = "username salah"
else:
    hasil = "username dan password salah"
print(f"{hasil}")
