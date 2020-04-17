# tipe data sets adalah himpunan
# tidak punya urutan dan menggunakan {}

minuman = {"es teh",
            "kopi",
            "es jeruk",
            "es capcin"}

minuman.add("es beng beng") # menambah variabel 
print(minuman) # menghasilkan output
# outputnya adalah {'es teh', 'kopi', 'es jeruk', 'es capcin', 'es beng beng'}
# kenapa outputnya tidak urut? karena tipe data sets tidak memperhatikan berapa datanya

# kita bisa mengurutkan datanya menggunakan perintah sorted

print("="*100)
print(sorted(minuman))
''' 
hasilnya adalah 
['es beng beng', 'es capcin', 'es jeruk', 'es teh', 'kopi']
'''

# kita coba menggunakan himpunan dengan menggabungkan fungsi gabungan dan irisan

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {1,3,5,7}

print(ganjil.union(genap)) # union merupakan fungsi gabungan
print(ganjil.intersection(prima)) # intersection merupakan fungsi irisan