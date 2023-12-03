nama = input("Masukan nama anda ")
usia = int(input("Masukan usia anda "))
kelamin = input("jenis kelamin Laki-laki/Perempuan ")
if kelamin == "Laki-laki":
    if usia > 25:
        panggilan = "Sir"
    else:
        panggilan = "Adek"
elif kelamin == "Perempuan":
    if usia > 25:
        panggilan = "Nyonya"
    else:
        panggilan = "Nona"
else:
    print("pilih antara Laki-Laki / Perempuan")

print("selamat datang", panggilan, nama, "berumur", usia, "Di Old Trafford")