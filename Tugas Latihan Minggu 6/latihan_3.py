# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 29 September 2022
# Deskripsi : Program untuk mendapatkan jumlah bilangan ganjil dan genap dalam 1 set bilangan

# Input data
print('Masukan angka bebas, pencatatan akan berhenti bila input bilangan negatif')
genap = int(0)
ganjil = int(0)
while (True) :
    inp = int(input(''))
    if (inp < 0) :
        break
    else :
        if (inp % 2 == 0) :
            genap +=1
        elif (inp % 2 == 1) :
            ganjil +=1
        elif (inp == 0) :
            genap +=1

print ('Genap :', genap)
print ('Ganjil :', ganjil)
