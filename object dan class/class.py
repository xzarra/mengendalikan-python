# membuat class
# classs digunakan untuk membuat definisi kelas baru dan diakhiri dengan titik

class Karyawan: # membuat class karyawan
    empCount = 0
    
    def __init__(self, name, salary): # mendeklarasikan init atau main dari python
        self.name = name
        self.salary = salary
        Karyawan.empCount +=1
    
    def displayKaryawan(self): # membuat object displaykaryawan
        print("Nama : ", self.name, ", Gaji : ", self.salary)

emp1 = Karyawan("Arya",2300)# menginput data karyawan
emp2 = Karyawan("Satya", 2100)

emp1.displayKaryawan() # memanggil data karyawan dari display Karywan
emp2.displayKaryawan()
print("Total Karyawan %d" % Karyawan.empCount) # menghitung banyaknya karyawan
