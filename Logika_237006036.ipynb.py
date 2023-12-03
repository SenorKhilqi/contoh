nilai = float(input("masukan nilai "))

if nilai > 100:
    hasil = "PERFECT"
elif nilai >= 85:
    hasil = "A"
elif nilai >= 77:
    hasil = "A-"
elif nilai >= 69:
    hasil = "B+"
elif nilai >= 61:
    hasil = "B"
elif nilai >= 53:
    hasil = "B-"
elif nilai >= 45:
    hasil = "C+"
elif nilai >= 37:
    hasil = "C"
elif nilai >= 29:
    hasil = "C-"
elif nilai >= 21:
    hasil = "D"
elif nilai >0:
    hasil = "E"
else:
    hasil = "TIDAK LULUS"
print("=" *15)
print("skor anda ", hasil)
print("=" *15)

