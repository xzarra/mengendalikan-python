# fungsi stacks adalah menumpuk, keluar di akhir
# stacks = pop


tumpukanKardus = [1,2,3,4,5,6] # kita inisialisasikan tumpukan kardus ada 6 data
print("tumpukan kardus adalah : ",tumpukanKardus) # menampilkan data tumpukan kardus

tumpukanKardus.append(7) # kita tambah tumpukan nomer ke 7
print("data masuk ",7)
print("data sekarang : ",tumpukanKardus)# kita keluarkan data yang kita tambahkan

tumpukanKardus.append(8) # kita tambah antrean nomer ke 8 
print("data masuk ",8)
print("data sekarang : ",tumpukanKardus) # kita keluarkan data yang kita tambahkan

out = tumpukanKardus.pop() # kita stack menggunakan keyword .pop
print("data yang keluar adalah data ke ",out) # kita tampilkan data yang keluar
print("data terbaru adalah : ",tumpukanKardus) # hasil data yang kita stack

