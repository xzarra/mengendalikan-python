# ini adalah cara menampilkan waktu

import time; # digunakan untuk mengimport modul time

localtime = time.asctime(time.localtime(time.time()))
print ("Waktu sekarang adalah : ",localtime) # menampilkan waktu

import calendar; # import modul calender dahulu

cal = calendar.month(2020, 4)# kita setting kalender tahun 2020, dan bulan april= 4
print("Kalender bulan APRIL tahun 2020")
print (cal) # menampilkan kalender bulan april

call = calendar.calendar(2020,w=1,l=1,c=1)
print (call)