a = input ("username")
b = input ("password")

if a == "abcd" and b == "1234":
    hasil = "berhasil masuk"
elif a == "abcd" and not b == "1234":
    hasil = "password salah"
elif not a == "abcd" and  b == "1234":
    hasil = "username salah"
else:
    hasil = "username dan password salah"
print(f"{hasil}")
