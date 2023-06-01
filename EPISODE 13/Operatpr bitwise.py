# Operator Bitwise (operasi binary)
# bitwise = operasi pada masing-masing bite

"""
contoh Binary :
int = 2 --> 00000010
            --------
indeks ke   76543210  #ini adalah dua dua dua dipangkatkan dg indeksnya 
jadi,  2**1 = 2

int = 1 --> 00000001
            --------
indeks ke   76543210
jadi, 2**0 = 1

int = ? (jwbannya 9) --> 00001001
                         --------
                         76543210
jadi, 2**3 + 2**0 = 8 + 1 = 9
"""

"""
contoh bitwise :
2 | (or) 1 --> 2 --> 00000010
               1 --> 00000001 
               kemudian keduanya id or kan 
                     00000011
            jadi,    2**1 + 2**0 = 2 + 1 = 3
        
"""

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n========OR========\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('------------------------- (|)')
print('nilai :',c,'binary:',format(c,'08b'))

# bitwise AND (&)
c = a & b
print('\n=======AND========\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('------------------------- (&)')
print('nilai :',c,'binary:',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print('\n=======XOR========\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('------------------------- (^)')
print('nilai :',c,'binary:',format(c,'08b'))

# bitwise NOT (~)
c = ~a #hasilnya akan mirror jika, negatif akan menjadi positif dan sebaliknya
print('\n=======NOT========\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('------------------------- (~)')
print('nilai :',c,'binary:',format(c,'08b'))
print('------------------------- (^)')  # NOT di XOR
d = 0b0000001001 
e = 0b1111111111
print('nilai :',e^d,' , bianry :',format(e^d,'08b'))

# SHIFTHING

# shift right (>>)
c = a >> 1
print('\n========>>========\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('------------------------- (>>)')
print('nilai :',c,'binary :',format(c,'08b'))

# shift left (<<)
c = a << 1
print('\n========<<========\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('------------------------- (<< )')
print('nilai :',c,'binary:',format(c,'08b'))