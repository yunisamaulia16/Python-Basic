# latihan konversi satuan temperatur

# program konversi celcius ke satuan lain #

print("\nPROGRAM KONVERSI TERMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius :'))
print("suhu adalah", celcius, "celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "Kelvin")
