# list data tidak hanya string, 
# tetapi juga ada integer, booelan, float dan sebagainya
# kita bisa menambahkan varian data dengan satu list

nama = ["Arya Satya Saputra", 19, True, 3.89]
# var = 0 : string, 1 : integer, 2 : booelan, 3 : float
print(nama) # outputnya adalah ['Arya Satya Saputra', 19, True, 3,89]

# list data bisa ditambahkan langsung
# dengan catatan tipe data harus sama
# kita coba menambah bil integer dengan 4
print(nama[1] + 4) # outputnya adalah 23