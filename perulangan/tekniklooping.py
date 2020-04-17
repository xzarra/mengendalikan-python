# teknik looping menggunakan enumerate untuk mereturn indexs
namaHewan = ['kelinci','ayam','sapi']

makananHewan = ['wortel','biji bijian','rumput']
for index,urutan in enumerate(namaHewan): # enumerate adalah penjabaran ke bawah data menggunakan nomer
    print(index,":",urutan) # menampilkan hasil enumerate

'''
hasilnya adalah
0 : kelinci
1 : ayam
2 : sapi
'''

# kita coba menggunakan fungsi zip untuk menggabungkan enumerate

for urutan,makanan in zip(namaHewan,makananHewan):  # menggunakan fungsi zip
    print(urutan,"makanannya adalah", makanan) # mengeluarkan fungsi penggabungan

'''
outputnya adalah :
kelinci makanannya adalah wortel
ayam makanannya adalah biji bijian
sapi makanannya adalah rumput
'''

# teknik perulangan untuk mensorting data

namaMahasiswa = {'gilang','arya','cindy','dela'}

for urut in sorted(namaMahasiswa):
    print(urut)