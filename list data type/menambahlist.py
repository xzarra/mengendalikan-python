# fungsi menambahkan list data pada array

makanan = ["seblak","sate","mi ayam","bakso"]
# var = indeks 0, indeks 1, indeks 2, indeks 3

makanan.append("salad")
# menambahkan indeks ke dalam var makanan

makanan[3] = "kolak"
# kita coba merubah bakso menjadi kolak

print(makanan) # outputnya adalah seblak, sate, mi ayam, kolak, salad

# kita menambahkan list di tengah tengah sate dan mie ayam
makanan.insert(2,"ayam geprek")

print(makanan)