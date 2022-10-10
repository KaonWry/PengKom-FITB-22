# NIM / Nama : 16322294 / Trystan Prastanov Gabriel
# Tanggal : 27 September 2022
# Deskripsi : Program penghitung biaya perjalanan optimal

# KAMUS
# biayaTanpaPaket, biayaPaket1, biayaPaket2 : integer
# costTanpaPaket, costPaket1, costPaket2 : integer

biayaTanpaPaket = int(input('Masukan biaya perjalanan per hari : '))
biayaPaket1 = int(input('Masukan biaya paket 1 : '))
biayaPaket2 = int(input('Masukan biaya paket 2 : '))

costTanpaPaket = biayaTanpaPaket * 30
costPaket1 = biayaPaket1 + (10 * biayaTanpaPaket * 0.6) + (biayaTanpaPaket * 20)
costPaket2 = biayaPaket2 + (20 * biayaTanpaPaket * 0.9) + (biayaTanpaPaket * 10)

if (costTanpaPaket < min(costPaket1, costPaket2)) :
    print('Tuan Kil tidak membeli paket dengan total pengeluaran sebesar', costTanpaPaket)
elif (costPaket1 < min(costTanpaPaket, costPaket2)) :
    print('Tuan Kil akan memilih paket 1 dengan total pengeluaran sebesar', costPaket1)
elif (costPaket2 < min(costPaket1, costTanpaPaket)) :
    print ('Tuan Kil akan memilih paket 2 dengan total pengeluaran sebesar', costPaket2)