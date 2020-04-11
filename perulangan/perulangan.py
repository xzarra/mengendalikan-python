# perulangan menggunakan for

nama = ["arya","satya","saputra","19 tahun","belajar","pyhton", "itu asik"]

for data in nama: # membuat variable data dari variabel nama
    print(data) # akan menampilkan data di variabel nama

# perulangan menggunakan while
# perulangan akan dieksekusi terus menerus selama kondisi bernilai true

hitung = 1
# kita inisialisasikan variable hitung
while (hitung <= 10): # lalu kita buat kondisi, jika hitung lebih dari 10 maka akan menampilkan perintah dibawahnya
    print("bilangan yang muncul : ", hitung) # menampilkan hasil perulangan dari variable hitung
    hitung += 1 # kita tambahkan operator increment 

print("- bilangan lebih dari 10 -") # kondisi jika perulangan sudah memenuhi kondisi

# perulangan menggunakan nested loop
# perulangan ini maksudnya adalah perulangan di dalam perulangan

i = 2
while (i < 10):
    j = 2
    while (j <= i/j):
        if not(i%j):
            print(j," bilangan j kurang dari sama dengan pembagian bilangan i/j")
        j += 1
    if (j > i/j):
        print(i, " bilangan j lebih dari pembagian i/j")
        i += 1
print("program berakhir")