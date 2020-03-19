# operator logika
# mengkombinasikan suatu statement

# contoh validasi password 
password = "arya123"
comfirmPassword = "arya1234" # misalnya kita memasukkan typo

# validasi password, apakah password sama dengan confirm password atau tidak
# kita samakan password dan validasi apakah sama ataukah tidak
print(password == "arya123" and comfirmPassword == "arya123") # hasilnya adalah false karena tidak sama dengan yang di validasi