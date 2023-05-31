# Episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++++++3-----------10+++++++++
# kasus digabungkan
inputUser = float(input("Masukan angka yang\nbernilai kurang dari 3\natau\nlebih besar dari 10 ="))

# +++++++++3------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# ---------10++++++++++++
# memeriksa angka lebih adri 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)


# ++++++++++3-----------10+++++++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan =", isCorrect)

#----------3+++++++++++10---------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukan angka yang\nbernilai lebih dari 3\ndan\nkurang dari dari 10 ="))

#----------3+++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3   =", isLebihDari)

#++++++++++10----------
# kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 =",isKurangDari)

#----------3+++++++++++10---------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan =", isCorrect)


# pr
# -----0+++++5-----8+++++11-----
# +++++0-----5+++++8-----11+++++