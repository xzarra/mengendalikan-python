# scope variabel
# local jadi yang terubah hanya variabel local saja.
''' berikut adalah contoh penggunaan variabel local'''

namaBuku = "Buku awal saya adalah Bahasa Indonesia " # kita buat variabel global dahulu
print(namaBuku) # kita panggil variabel globalnya 

def rubahNamaBuku(namaBaru): # lalu kita buat fungsi untuk mengubah variabel global
    namaBuku = namaBaru  # perubahan variabel global menjadi namabaru   
    print("Saya merubah judul buku menjadi : ",namaBuku) # kita keluarkan hasil perubahannya

rubahNamaBuku('Buku matematika') # kita inisialisasikan perubahan namabarunya 
print("nama Buku saya sekarang adalah ", namaBuku) # nilai nama buku ini tetap bernilai "buku awal saya adalah bahasa indonesia"
# variabel rubahNamaBuku tidak akan berubah lagi

# kita coba buat contoh namaBuku lagi
namaBuku = "Buku awal saya adalah Bahasa inggris"
# output dibawah adalah nama buku
print(namaBuku)

# variabel global bisa diganti jika didalam fungsi terdapat pemanggilan
# contohnya

warnaBuku = 'putih' # kita inisialisasikan wrana buku terlebih dahulu.
print('warna buku awal', warnaBuku) # lalu kita keluarkan variabel diatas

def rubahWarna(warnaBaru): # fungsi untuk merubah warna
    global warnaBuku # pemanggilan scope variabel
    warnaBuku = warnaBaru
    print('warna buku yang sudah terubah', warnaBuku)

rubahWarna('Hitam')# penggantian variabel 
# maka output dibawah ini adalah hitam
print('variabel global', warnaBuku)