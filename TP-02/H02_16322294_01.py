# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 5 Oktober 2022
# Deskripsi : Program mengecek bilangan sempurna

# Input data
inpNum = int(input('Masukan bilangan: '))

# Cari jumlah faktor
i =  int(1)
factorSum = int(0)
while (i < inpNum) :
    if (inpNum % i == 0) :
        factorSum += i
    i += 1

# Cek kesamaan jumlah faktor dengan bilangan input
if (inpNum < 0 or inpNum == 0) : 
    print('Bilangan tersebut bukan bilangan sempurna')
elif (factorSum == inpNum) :
    print('Bilangan tersebut adalah bilangan sempurna')
else :
    print('Bilangan tersebut bukan bilangan sempurna')