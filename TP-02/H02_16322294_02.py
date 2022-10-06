# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 5 Oktober 2022
# Deskripsi : Program mengecek jumlah dari bilangan yang membesar

# Input 1 pengecualian karena belum ada numPast
numNow = int(input('Angka ke-1: ')) 

# Init variables
minCounter = int(0)
biggerSum = int(0)

# Input data
i = int(2)
while True :
    displayInput = str('Angka ke-' + str(i) + ': ')
    numPast = numNow
    numNow = int(input(displayInput))

# Hitung jumlah kejadian angka sekarang lebih kecil dibanding angka sebelumnya
    if (numNow <= numPast) :
        minCounter += 1
        
# Reset counter dan jumlahkan angka jika angka membesar 
    elif (numNow > numPast) :
        minCounter = 0
        biggerSum += numNow
        
# Keluar loop jika lebih kecil berturut-turut sampai 3 kali
    if (minCounter == 3) :
        break

# Add counter
    i += 1
    
# Output data
print('Jumlah nilai yang membesar adalah ' + str(biggerSum) + '.')