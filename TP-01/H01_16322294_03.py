# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 14 September 2022
# Deskripsi : Program menghitung rentang waktu

# Input data mulai
print ('Masukan waktu mulai!')
InpJamMulai     = int(input('Jam   : '))
InpMenitMulai   = int(input('Menit : '))
InpDetikMulai   = int(input('Detik : '))

# Input data selesai
print ('Masukan waktu selesai!')
InpJamSelesai   = int(input('Jam   : '))
InpMenitSelesai = int(input('Menit : '))
InpDetikSelesai = int(input('Detik : '))

# Ubah waktu jadi detik (mirip-mirip sama UNIX timestamp)
DetikMulai      = (InpJamMulai * 3600) + (InpMenitMulai * 60) + InpDetikMulai
DetikSelesai    = (InpJamSelesai * 3600) + (InpMenitSelesai * 60) + InpDetikSelesai

# Cari selang waktu
DetikSelang     = DetikSelesai - DetikMulai

# Cari Jam Selang
JamSelang       = int(DetikSelang / 3600)
DetikSelang     = int(DetikSelang % 3600)

# Cari Menit Selang
MenitSelang     = int(DetikSelang / 60)
DetikSelang     = int(DetikSelang % 60)

# Parse waktu ke string
JamSelang       = str(JamSelang)
MenitSelang     = str(MenitSelang)
DetikSelang     = str(DetikSelang)

# Output
if JamSelang    == '0' :
    OutJam      = ''
else :
    OutJam      = str(JamSelang + ' jam ')

if MenitSelang  == '0' :
    OutMenit    = ''
else :
    OutMenit    = str(MenitSelang + ' menit ')

if DetikSelang  == '0' :
    OutDetik    = ''
else :
    OutDetik    = str(DetikSelang + ' detik ')

print('Tuan Riz berlari selama ' + OutJam + OutMenit + OutDetik)