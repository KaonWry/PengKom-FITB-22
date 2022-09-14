# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 14 September 2022
# Deskripsi : Program menghitung barang yang harus ditawarkan

#Input data
ADasar  = int(input('Masukan harga dasar barang A: '))
AJual   = int(input('Masukan harga jual barang A: '))
BDasar  = int(input('Masukan harga dasar barang B: '))
BJual   = int(input('Masukan harga jual barang B: '))
CDasar  = int(input('Masukan harga dasar barang C: '))
CJual   = int(input('Masukan harga jual barang C: '))

#Hitung selisih jual dan beli
AUntung = AJual - ADasar
BUntung = BJual - BDasar
CUntung = CJual - CDasar

#Cari yang paling besar
if  AUntung > max(BUntung, CUntung) : 
    print ('Barang yang harus ditawarkan adalah barang A')

elif BUntung > max(CUntung,AUntung) : 
    print ('Barang yang harus ditawarkan adalah barang B')

elif CUntung > max(BUntung,AUntung) :
    print ('Barang yang harus ditawarkan adalah barang C')