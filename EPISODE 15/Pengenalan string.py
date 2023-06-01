data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

"""
    1. denagn menggunakan single quote '...'
    2. denegan menggunkan double quote "..."
"""

data = 'Menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakna tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash (untuk membuat backlash menjadi string, tambahkan backlash lagi)
print("c:\\user\\Ucup")

# tab
print("ucup\totong, jauhan") #menambah kan \t untuk membuat teks semakin jauh


# backspace
print("ucup \botong, mendekat") #menambahkan \b untuk mendekatkan teks

# newline
print("baris pertama.\nbaris kedua") # LF --> line feed --> biasa dipakai di unix, mac os, linux
print("baris pertama.\rbaris kedua") # CR --> carriage return --> biasa dipakai commodore, acorn, lisp
print("baris pertama.\n\rbaris kedua") # CRLF --> line fed carriage return --> dipakai oleh windows

# 3. string literal atau RAW
#hati-hati
print('C:\new folder') # akan salah path nya

# menggunakan raw string
print(r'C:\new \t\r\b\\folder') # jika menggunakan raw string semuanya akan menjadi string

# multiline literal string
print("""
Nama  : Yunisa
Kelas : TI.22.C7
""")

# multiline literal string dan RAW
print(r"""
Nama  : Yunisa
Kelas : TI.22.C7
website : www.yunisa.com/newID
""")