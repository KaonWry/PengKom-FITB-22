# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 24 September 2022
# Deskripsi : Program untuk mengubah suhu

# Input data
SuhuAwal    = float(input('Masukan suhu awal : '))
print('\nKeterangan Input (hanya menerima huruf kapital semua atau huruf kecil semua)\nC = Celcius \nR = Reamur \nF = Fahrenheit \nK = Kelvin')
SatuanAwal  = str(input('Masukan satuan awal : '))
SatuanAkhir = str(input('Masukan satuan tujuan : '))

# Ubah suhu
# Dari celcius
if ((SatuanAwal == 'C' and SatuanAkhir == 'R') or (SatuanAwal == 'c' and SatuanAkhir == 'r')) :
    print((4/5) * SuhuAwal , '\u00b0R')
elif ((SatuanAwal == 'C' and SatuanAkhir == 'F') or (SatuanAwal == 'c' and SatuanAkhir == 'f')) :
    print(((9/5) * SuhuAwal) + 32 , '\u00b0F')
elif ((SatuanAwal == 'C' and SatuanAkhir == 'K') or (SatuanAwal == 'c' and SatuanAkhir == 'k')) :
    print(SuhuAwal + 273.15 , 'K')
    
# Dari reamur
elif ((SatuanAwal == 'R' and SatuanAkhir == 'C') or (SatuanAwal == 'r' and SatuanAkhir == 'c')) :
    print((5/4) * SuhuAwal, '\u00b0C')
elif ((SatuanAwal == 'R' and SatuanAkhir == 'F') or (SatuanAwal == 'r' and SatuanAkhir == 'f')) :
    print(((9/4) * SuhuAwal) + 32, '\u00b0F')
elif ((SatuanAwal == 'R' and SatuanAkhir == 'K') or (SatuanAwal == 'r' and SatuanAkhir == 'k')) :
    print(SuhuAwal + 273.15 , 'K')
    
# Dari fahrenheit
elif ((SatuanAwal == 'F' and SatuanAkhir == 'C') or (SatuanAwal == 'f' and SatuanAkhir == 'c')) :
    print((SuhuAwal - 32) * (5/9), '\u00b0C')
elif ((SatuanAwal == 'F' and SatuanAkhir == 'R') or (SatuanAwal == 'f' and SatuanAkhir == 'r')) :
    print((SuhuAwal - 32) * (4/9) , '\u00b0R')
elif ((SatuanAwal == 'F' and SatuanAkhir == 'K') or (SatuanAwal == 'f' and SatuanAkhir == 'k')) :
    print(((SuhuAwal - 32) * (5/9)) + 273.15 , 'K')
    
# Dari kelvin
elif ((SatuanAwal == 'K' and SatuanAkhir == 'C') or (SatuanAwal == 'k' and SatuanAkhir == 'c')) :
    print((SuhuAwal - 273.15) , '\u00b0C')
elif ((SatuanAwal == 'K' and SatuanAkhir == 'R') or (SatuanAwal == 'k' and SatuanAkhir == 'r')) :
    print((SuhuAwal - 273.15) * (5/4), '\u00b0R')
elif ((SatuanAwal == 'K' and SatuanAkhir == 'F') or (SatuanAwal == 'k' and SatuanAkhir == 'f')) :
    print(((SuhuAwal - 273.15) * (9/5) + 32 , '\u00b0F'))
    
# Kalau salah input
else :
    print('Input tidak valid')