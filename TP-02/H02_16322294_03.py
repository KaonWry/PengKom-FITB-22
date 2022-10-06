# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 5 Oktober 2022
# Deskripsi : Program mencari faktor prima dari sebuah bilangan

# Input data
inpNum = int(input('Masukan N: '))

print ('Faktor primanya adalah', end=' ')
for i in range (2,inpNum+1) :
    if (inpNum % i ==  0) :
        factors = int(0)
        for j in range (1,i+1):
            if (i % j == 0) :
                factors += 1
        if (factors == 2) :
            print (i , end=' ' )
print('')