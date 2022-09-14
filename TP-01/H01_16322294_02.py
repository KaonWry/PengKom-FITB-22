# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 14 September 2022
# Deskripsi : Program menentukan kelas dari NIM

# Input data
InpNIM = int(input('Masukan akhiran NIM: '))

# Penentuan kelas
# InpNIM % 2 = 0 => NIM genap
# Selain itu NIM ganjil

# NIM 001 - 100
if InpNIM >=1 and InpNIM <=100 : 
    if InpNIM % 2 == 0 :
        print ('Mahasiswa masuk ke kelas K2')
    else :
        print ('Mahasiswa masuk ke kelas K1')

# NIM 101 - 200
elif InpNIM >=101 and InpNIM <= 200 :
    if InpNIM % 2 == 0 :
        print ('Mahasiswa masuk ke kelas K4')
    else :
        print ('Mahasiswa masuk ke kelas K3')

# NIM 201 - 300
elif InpNIM >=201 and InpNIM <=300 :
    if InpNIM % 2 == 0 :
        print ('Mahasiswa masuk ke kelas K6')
    else :
        print ('Mahasiswa masuk ke kelas K5')

# NIM 301 keatas
elif InpNIM >=301 : 
    if InpNIM % 2 == 0 :
        print ('Mahasiswa masuk ke kelas K8')
    else :
        print ('Mahasiswa masuk ke kelas K7')