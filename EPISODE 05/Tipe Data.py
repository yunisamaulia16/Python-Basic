""" tipe data adalah macam-macam data 
yang dapat dipakai di python yg dapat di masukan ke variabel"""

# tipe data: Angka satuan (integer)
data_integer = 1 #semua angka yg tdk ada koma termasuk integer 
print("data :", data_integer, ", bertipe : ", type(data_integer))
#print(type(data_integer))
#kita bisa naro banyak data memakai koma

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe :", type(data_float))

# tipe data: kumpulan kata (string)
data_string = "Yunisa" #misal yunisa 10, masih termasuk string
print("data : ", data_string)
print("- bertipe :", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## Tipe data khusus ##
# bilangan kompleks (misal 5+6j, u/ j bilangan imajener)
data_complex = complex(5,6) #bilangan real didpn, bil imajener dibelakang
print("data : ", data_complex)
print("- bilangan : ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double, c_char, c_long #bisa tipe data apasaja
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
