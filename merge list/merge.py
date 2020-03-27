# merge adalah penggabungan data

makanan = ["soto","sate","seblak"]
# membuat variable makkanan
minuman = ["float","es teh","es jeruk"]
# membuat variable minuman
pesanan = makanan + minuman
# menggabungkan data makanan dan minuman
makanan.extend(minuman)
# atau juga bisa menambah dengan perintah extend
print(pesanan) # outputnya adalah soto, sate, seblak, float, es teh, es jeruk
print(makanan)