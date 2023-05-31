#operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean (true/false)

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari > #lebih ke posisi
print("======lebih besar dari (>)======")
hasil = a > 3
print(a, '>', 3,'=', hasil)
hasil = b > 3
print(b, '>', 3,'=', hasil)
hasil = b > 2
print(b, '>', 2,'=', hasil)

# kurang dari <
print("======lebih kecil dari (<)======")
hasil = a < 3
print(a, '<', 3,'=', hasil)
hasil = b < 3
print(b, '<', 3,'=', hasil)
hasil = b < 2
print(b, '<', 2,'=', hasil)

# lebih dari sama dengan (>=)
print("======lebih dari sama dengan (>=)======")
hasil = a >= 3
print(a, '>=', 3,'=', hasil)
hasil = b >= 3
print(b, '>=', 3,'=', hasil)
hasil = b >= 2
print(b, '>=', 2,'=', hasil)

# kurang dari sama dengan (<=)
print("======kurang dari sama dengan (<=)======")
hasil = a <= 3
print(a, '<=', 3,'=', hasil)
hasil = b <= 3
print(b, '<=', 3,'=', hasil)
hasil = b <= 2
print(b, '<=', 2,'=', hasil)

# sama dengan (==)
# apabila sama dengan nya satu (=) disebut assigment,
# jika sama dengan nya double (==) itu berarti membandingkan
print("======sama dengan (==)======")
hasil = a == 4
print(a,'==',4,'=', hasil)
hasil = b == 4
print(b,'==',4,'=', hasil)

print("======sama dengan (==)======")
hasil = a == 4
print(a,'==',4,'=', hasil)
hasil = b == 4
print(b,'==',4,'=', hasil)

print("======tidak sama dengan (!=)======")
hasil = a != 4
print(a,'!=',4,'=', hasil)
hasil = b != 4
print(b,'!=',4,'=', hasil)

# is sebagai komparasi objek identity

"""
catatan :
jika melakukan komparasi ( > < >= <= == != ) 
dapat bekerja pada sintaks literal
contoh literal : a = 4 
a memiliki nilai, sedangkan 4 adalah literal karena tidak ada variabel nya
a akan memakan memori, sedangkan 4 tidak memakan memori karena literal
dan hanya hidup di baris itu saja.
"""
"""
is membandingan komparasi antara nilai yang memakan memori (membandingkan memori/objek)
"""

print("======objec identity (is)======")
x = 5 # ini adalah assigment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x))) #id adalah objec identity
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)

"""
jika x=5 maka nilai x adalah 5, jika type(x) maka maka class nya integer
dan id(x) (id(x)merupakan memorinya) 
hex(id(x)) maka menjadi hex ini adalah addresnya/memorinya
jadi, id adalah objec identity 
"""

x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# is sebagai komparasi objek identity

print("======objec identity (is not)======")
x = 5 # ini adalah assigment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x))) #id adalah objec identity
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

x = 5 # ini adalah assigment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x))) #id adalah objec identity
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)