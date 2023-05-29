import time #pembuktian compile lebih cepat dari interpreter
start_time = time.time() #pembuktian compile lebih cepat dari interpreter

print ("Hello")
print ("World")
print ("Hello World")

print ("Yunisa gadis pintar")
#ini comment tidak akan di eksekusi
a=10 #ini adalah comment juga (a tidak akan dieksekusi, a hanya menyimpan)
"""ini adalah multiline comment
ini adalah multiline comment"""
print (a)

print(time.time() - start_time, "detik") #pembuktian compile lebih cepat dari interpreter
#kita dapat mengcompile ke yang namanya bytecode
#Cara mengcopile buka terminal dan tuliskan 
#python -m py_compile Main.py