# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 29 September 2022
# Deskripsi : Program untuk mengetahui jumlah mahasiswa yang lulus

# Input jumlah mahasiswa
n           = int(input('Jumlah mahasiswa : '))-1
nilai       = [0] * (n+1)

# Input nilai mahasiswa
print('Jumlah mahasiswa sebanyak', n+1, 'orang')
print('Masukan nilai mahasiswa')
while (n >= 0) :
    nilai[n-1] = str(input('')).lower()
    if (nilai[n-1] in ('a', 'b', 'c', 'd', 'e', 'f')) :
        n-=1
    else :
        print('INPUT INVALID')

# Hitung lulus dan tidak lulus
lulus       = nilai.count('a') + nilai.count('b') + nilai.count('c') + nilai.count('d')
tdklulus    = nilai.count('e') + nilai.count('f')

# Output data
print('Lulus =', lulus)
print('Tidak lulus =', tdklulus)