# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Yunisa"
nama_tengah = "Maulia"
nama_akhir = "Astuty"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang operator string
panjang = len(nama_lengkap) #spasi termasuk kedalam hitungan
print("panjang dari " + nama_lengkap + " = " + str(panjang))
# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

a = "a"
status = a in nama_lengkap
print("string " + a +" ada di " + nama_lengkap + " = " + str(status))

A = "A"
status = A in nama_lengkap
print("string " + A +" ada di " + nama_lengkap + " = " + str(status))

a = "a"
status = a not in nama_lengkap
print("string " + a +" tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing (mengambil data dari string)
print("index ke-0 : " + nama_lengkap[0]) # index dimulai dari 0
print("index ke-8 : " + nama_lengkap[8]) 
print("index ke-(-1):" + nama_lengkap[-1]) #jika minus akan ngambil dari belakang
print("index ke-(-2):" + nama_lengkap[-2])
print("index ke-[0:5]:" + nama_lengkap[0:5]) # titik dua berarti sampai (:)
# dalam python, jika akan akan menghitung index dari mana sampai mana index terakhir tidak di ikut sertakan 
print("index ke-[0:5]:" + nama_lengkap[0:6])
print("index ke-[0,2,4,6,8,10]:" + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil :" + min(nama_lengkap))
# item paling besar
print("paling besar :" + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(ascii_code))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah 0 pada " + data + " = " + str(jumlah))