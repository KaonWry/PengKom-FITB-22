# NIM / Nama : 16322294 / Trystan Prastanov Gabriel
# Tanggal : 27 September 2022
# Deskripsi : Program pengatur kesulitan game

# KAMUS
# start : array, integer
# finish : array, integer
# passed : array, string
# countMudah : integer
# countSedang : integer
# countSulit : integer

# Var Declaration
start = [0] * 5
finish = [0] * 5
passed = [0] * 5

# Input data
i = 0
while (i < 5) : 
    inpStart = 'Banyak pemain yang memainkan level ' +  str(i+1) +  ' : '
    inpFinish = 'Banyak pemain yang menyelesaikan level '+ str(i+1) + ' : '
    start[i] = int(input(inpStart))
    finish[i] = int(input(inpFinish))
    i += 1

# Cari kesulitan
i = 0
while (i < 5) :
    if (finish[i] / start[i] >= 0.8) :
        passed[i] = 'mudah'
    elif (finish[i] / start[i] < 0.3) : 
        passed[i] = 'sulit'
    else :
        passed[i] = 'sedang'
    i += 1

# Hitung tingkat kesulitan
countMudah = int(passed.count('mudah'))
countSedang = int(passed.count('sedang'))
countSulit = int(passed.count('sulit'))

# Output
print('Banyak level mudah sebanyak ' + str(countMudah) + ', level sedang sebanyak ' + str(countSedang) + ', dan level sulit sebanyak ' +  str(countSulit) + '.')
if (countMudah == 2 and countSulit == 1) : 
    print('Target berhasil dicapai.')
else :
    print('Target gagal dicapai.')