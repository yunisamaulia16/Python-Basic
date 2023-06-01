# operator dalam bentuk method

## merubah case dari string ##

# merubahsemua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lowe case
alay = "aKu KeCe AbieeZZzzZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# pengecekan dengan isX method

# contoh untuk pengercekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilanya boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya boolean
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecek huruf dan angka
# isdecimal() <-- untuk mengecek angka saja
# isspace() <-- untuk mengecek spasi, tab, newline \n
# istitle() <-- untuk mengecek semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle() # hasilnya boolean

print(judul + " is title = " + str(cek_judul))

## cek komponen startswith(), endswith() ##
cek_start = "Sajangnim Oppa".startswith("Sajangnim")
print("start =" + str(cek_start))

cek_end = "Sajangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

## penggabungan komponen join() split() ##
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

## alokasi karakter rjust(), ljust() center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-") 
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip("-") # menghilangkan tanda -
print("'"+tengah+"'")

kanan = kanan.strip() # menghilangkan spasi 
print("'"+kanan+"'")
