# fungsi queues menumpuk data dan dikeluarkan yang di depan dahulu
# di queues  harus mengimport library python bernama deque
from collections import deque

antreanSembako = deque([1,2,3,4,5])
print("antrean sembako awalnya ada : ",antreanSembako)

# menambah data antrean
antreanSembako.append(6)
print("data masuk : ",6)
print("data sekarang adalah : ",antreanSembako)

# mengurangi data dari awal
out = 0
while (out < 6):
    out = antreanSembako.popleft()
    print("data keluar adalah : ",out)
    print("data yang tersedia : ",antreanSembako)
    out += 1

''' hasilnya adalah dibawah ini :
antrean sembako awalnya ada :  deque([1, 2, 3, 4, 5])
data masuk :  6
data sekarang adalah :  deque([1, 2, 3, 4, 5, 6])
data keluar adalah :  1
data yang tersedia :  deque([2, 3, 4, 5, 6])
data keluar adalah :  2
data yang tersedia :  deque([3, 4, 5, 6])
data keluar adalah :  3
data yang tersedia :  deque([4, 5, 6])
data keluar adalah :  4
data yang tersedia :  deque([5, 6])
data keluar adalah :  5
data yang tersedia :  deque([6])
'''