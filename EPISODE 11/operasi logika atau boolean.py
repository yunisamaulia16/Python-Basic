# operasi logika atau boolean

# not, or, and, xor

# NOT
print("====NOT====")
a = True
c = not a # melakukan operasi not pada a
print("data a :",a)
print('=========NOT')
print("data c :",c)

# OR (harus memiliki dua buah nilai)
# jika salah satu bernilai true, maka hasilnya true
print("====OR====")
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)

# AND (jika dua buah nilai true, maka hasilnya true)
print("====AND====")
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

# XOR (jika salah satu nilai bernilai true, maka hasilnya true)
print("====XOR====")
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)

# ini di sebut sebagai tabel kebenaran