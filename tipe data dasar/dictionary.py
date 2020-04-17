# tipe data dictionary
# struktur data asosiatif atau menggunakan mapping

# kegunaan dictionary
# mengambil data berdasarkan key atau variabel
# garis besar dictionary adalah "key : value"

# keuntungan dictionary ini adalah kita bisa mengambil data berdasarkan valuenya

#contoh program data mahasiswa
mahasiswa1 = {"Nim": 901001,
            "Nama": "Arya Satya",
            "Progdi": "Teknik informatika",
            "Angkatan": 2019,
            "Motto": "Belajar, Belajar, Praktekkan"}

mahasiswa2 = {"Nim": 901002,
            "Nama": "Nindy Saputri",
            "Progdi": "Teknik telekomunikasi",
            "Angkatan": 2018,
            "Motto": "Berjalan dan tetap santuy"}

# menampilkan data diatas
print(mahasiswa1) # data mahasiswa 1
print(mahasiswa2) # data mahasiswa 2

# output
'''
{'Nim': 901001, 'Nama': 'Arya Satya', 'Progdi': 'Teknik informatika', 'Angkatan': 2019, 'Motto': 'Belajar, Belajar, Praktekkan'}
{'Nim': 901002, 'Nama': 'Nindy Saputri', 'Progdi': 'Teknik telekomunikasi', 'Angkatan': 2018, 'Motto': 'Berjalan dan tetap santuy'}
'''

# kita bisa hanya menampilkan namanya saja
print(mahasiswa1["Nama"]) # menampilkan nama mahasiswa1 = Arya Satya

# kita coba menampilkan keys, value dan items, untuk membedakan ketiga fungsi itu
print(mahasiswa1.keys())
print(mahasiswa1.values())
print(mahasiswa1.items())
'''
outputnya adalah
dict_keys(['Nim', 'Nama', 'Progdi', 'Angkatan', 'Motto'])
dict_values([901001, 'Arya Satya', 'Teknik informatika', 2019, 'Belajar, Belajar, Praktekkan'])
dict_items([('Nim', 901001), ('Nama', 'Arya Satya'), ('Progdi', 'Teknik informatika'), ('Angkatan', 2019), ('Motto', 'Belajar, Belajar, Praktekkan')])
'''

# kita coba ringkas data diatas menggunakan list
dataMahasiswa = {901001:mahasiswa1,901002:mahasiswa2}
print("\n",dataMahasiswa[901001])