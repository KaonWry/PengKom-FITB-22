# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 29 September 2022
# Deskripsi : Program lagu anak ayam dengan for loop

# Input data
i = int(input('Anak ayam turunlah '))

# Loop
for x in range(i):
    if (i-x-1 == 0) :
        print('Mati satu tinggalah induknya')
    else :
        print('Mati satu tinggalah', i-x-1)
