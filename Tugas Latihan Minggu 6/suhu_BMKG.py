# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 29 September 2022
# Deskripsi : Program untuk mendapatkan statistik suhu 1 bulan

# Input data jumlah hari
hari = int(input('Jumlah hari : ')) - 1
suhu = [0] * (hari + 1)
hariTotal = hari + 1

# Input data suhu
print('1 bulan sepanjang', hari+1, 'hari')
print('Masukan data suhu')
while (hari >= 0) :
    suhu [hari-1] = int(input(('Hari ke-' + str(hariTotal - hari) + ' : ')))
    hari-=1
    
# Hitung statistik
suhuAvg = sum(suhu) / hariTotal
suhuTinggi = max(suhu)
suhuRendah = min(suhu)

# Output data
print('Suhu tertinggi :', suhuTinggi)
print('Suhu terendah :', suhuRendah)
print('Suhu rata-rata :', suhuAvg)