# NIM / Nama : 16322294 / Trystan Prastanov Gabriel
# Tanggal : 27 September 2022
# Deskripsi : Program pengatur kursi pesawat

# KAMUS
# seat : int
# line : string
# column : string

# Input data
seat    = int(input('Masukan nomor antrian tiket : '))

# Cari baris
if (seat % 4 == 0) :
    line = str(int(seat / 4))
else :
    line = str(int(seat / 4) + 1)

# Cari kolom
if (seat % 4 == 1) :
    column = 'A'
elif (seat % 4 == 2) :
    column = 'B'
elif (seat % 4 == 3) :
    column = 'C'
elif (seat % 4 == 0) :
    column = 'D'

# Output
print('Tempat duduk tiket nomor', seat, 'memiliki nomor', line + column)