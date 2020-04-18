# package adalah kumpulan dari modul modul
# package = folder kumpulan modul
# kata kunci ="From -folder- import -file-"
# jika import package terdapat __init__ dia adalah modul utama
# penggunaan init kata kunci "from .-file- import *"

import pelajaran # mengimport package pelajaran

pan = pelajaran.pantun() # memanggil fungsi pantun
print(pan, "\n") # menampilkan fungsi pantun

puis = pelajaran.puisi() # memanggil fungsi puisi
print(puis,"\n") # menampilkan fungsi puisi

disk = pelajaran.diskrit() # memanggil fungsi diskrit
print(disk,"\n") # menampilkan fungsi diskrit

himp = pelajaran.himpunan() # memanggil fungsi himpunan
print(himp) # menampilkan fungsi himpunan

'''
ini adalah contoh penggunaan package
'''