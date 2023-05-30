# Episode Input User

# data yg dimasukan pasti string
data = input("Masukan data= ")

print("data = ", data, ", type =",type(data))

#jika kita ingin mengambil integer, maka
angka = float(input("Masukan angka = "))
angka = int(input("Masukan angka = "))

print("data = ", angka, ", type =",type(angka))

# Bagaimana dengan boolean
biner = bool(int(input("Masukan nilai boolean =")))
#casting boolean menjadi integer terlebih dahulu

print("data = ", biner, ", type =",type(biner))