# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 29 September 2022
# Deskripsi : Program lagu anak ayam dengan while loop

# Input data
i = int(input('Anak ayam turunlah ')) - 1

# Loop
while (i >= 0) :
    if (i == 0) :
        print('Mati satu tinggalah induknya')
    else :
        print('Mati satu tinggalah', i)
    i-=1