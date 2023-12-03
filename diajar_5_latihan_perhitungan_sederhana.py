# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print ("\nPROGRAM CELCIUS TEMPERATUR\n")
celcius = float (input ("Masukan suhu dalam celcius "))
print ("suhu adalah",celcius, "celcius")

# reamur 
reamur = (4/5) * celcius
print ("suhu dalam reamur adalah ",reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32 
print ("suhu dalam fahrenheit adalah", fahrenheit,"fahrenheit")

#kelvin
kelvin = celcius + 273
print ("suhu dalam kelvin adalah", kelvin,"kelvin")

# kelvin to fahrenheit 
fahrenheit = float (input("masukan suhu dakam kelvin :"))
fahrenheit = ((kelvin - 273)* (9/5)) + 32
print ("suhu kelvin dalam fahrenheit adalah", fahrenheit,"fahrenheit")

# fahrenheit to kelvin
kelvin = float(input ("masukan suhu dalam fahrenheit"))
kelvin = ((fahrenheit - 32 )(5/9))+ 273
print ("suhu fahrenheit dalam kelvin adalah", fahrenheit, "fahrenheit")
