# try and exception
# mencoba dan pengecualian
# pengecualian dalam kode error
# kata kuncinya adalah "TRY:
#                       EXCEPT:"
# contoh program
a = int(input("Masukkan nilai : "))
# kita harus memasukkan tipe data bernilai integer
print(a)
# maka hasilnya adalah 
'''
Masukkan nilai : 10
10
'''

# lalu kita coba memasukkan tipe data string 
'''
maka outputnya adalah :
Masukkan nilai : te
Traceback (most recent call last):
    File "c:/Users/xalysta/Desktop/mengendalikan-pyhton/try and exception/exception.py", line 6, in <module>
    a = int(input("Masukkan nilai : "))
ValueError: invalid literal for int() with base 10: 'te'
'''
# kenapa error? karena tipe data yang seharusnya adalah integer, bukan string

# kita buat program menggunakan try and error

while True: # kita buat perulangan agar jika program berjalan dengan baik akan tetap di ulang
    try: # kita coba dahulu
        import dedn
        print("======= Program pembagian sederhana =======")
        bil1 = int(input("Masukkan bilangan pertama : "))
        bil2 = int(input("Masukkan bilangan kedua   : "))
        hasil = bil1/bil2
        break
    #except: # jika error maka akan keluar output dibawah
    #    print("Masukkan angka saja !!")
# exception mempunyai 3 cara untuk digunakan
# yang pertama adalah seperti diatas
# yang kedua adalah pendefinisian error contohnya :
    except ValueError:
        print("Cukup masukkan angka saja yaaa!")
    except ZeroDivisionError:
        print("Coba jangan dibagi dengan bilangan nol yaa")
    
    except Exception as error:
        print(error)
print("Hasil perkalian bilangan ",bil1,"x",bil2,"adalah : ",hasil)    
