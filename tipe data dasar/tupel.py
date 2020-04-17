# tipe data tuple sama halnya seperti list, namun perbedaannya di list memakai [], tipe data tuple menggunakan ()
# data tuple =TIDAK BISA DIRUBAH=

# kita coba buat tipe data list
Ganjil = [1,3,5,7,9]

# kita coba buat tipe data tuple
Genap = (2,4,6,8,10)

# kita lihat class type nya
print(type(Ganjil))
print(type(Genap))

''' 
maka akan keluar seperti ini
<class 'list'>
<class 'tuple'>
'''

# kita coba tambahkan data pada tuple
#Genap.append(2)

''' 
hasilnya tidak bisa karena tipe data tuple tidak bisa dirubah

Traceback (most recent call last):
  File "c:/Users/xalysta/Desktop/mengendalikan-pyhton/tipe data dasar/tupel.py", line 21, in <module>
    Genap.append(2)
AttributeError: 'tuple' object has no attribute 'append'
'''

# tuple memiliki 2  perintah yaitu count dan index
# perintah count = menghitung
# perintah index = mencari index

print(Genap.count(4))
print(Genap.index(10))
