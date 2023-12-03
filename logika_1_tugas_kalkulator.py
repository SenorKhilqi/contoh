import sys #agar membatasi karakter yang di isi ketika user mengisi hanya yang tertera pada pilihan

bil1 = int(input("bilangan pertama = "))
bil2 = int(input("bilangan kedua = "))
prosses = input("prosses yang akan digunakan (+, -, *, /) ")
if prosses not in ("+", "-", "/", "*"):
  print("harap masukan pilihan yang tertera") #jika user mengisi tidak sesuai dengan pilihan maka akan terjadi eror
  sys.exit(1) #lalu akan otomatis exit

if prosses == "+":
    hasil = bil1 + bil2
elif prosses == "-":
    hasil = bil1 - bil2
elif prosses == "*":  # untuk string bisa menggunakan * atau X
    hasil = bil1 * bil2
elif prosses == "/":  # untuk bagian string bisa menggunakan : atau /
    hasil = bil1 / bil2
else:
    print("pilih antara +, -, *, /")
print(f"hasil dari {bil1} {prosses} {bil2} adalah {hasil}")

# notes "JIKA AKAN MENGGUNAKAN / ATAU * DARI ATAS SAMPAI BAWAH TERUS GUNAKAN ITU JANGAN DIGANTI DENGAN x ATAU : KARENA AKAN MEMBUAT LIUER MASTAKA"