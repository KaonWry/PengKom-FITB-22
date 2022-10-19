# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 19 Oktober 2022
# Deskripsi : Program menghitung jumlah string 1 disebut di string 2

# Input data
str1L = int(input("Masukan panjang string 1: "))
str1 = str(input("Masukan string 1: "))
str2L = int(input("Masukan panjang string 2: "))
str2 = str(input("Masukan string 2: "))

# Map ke array
str1Arr = [str(x) for x in str1]
str1L = len(str1Arr)
str2Arr = [str(x) for x in str2]
str2L = len(str2Arr)

# Cari yang sama
count = int(0)
for i in range (str2L - str1L + 1):
    j = 0
    while j < str1L:
        if (str2Arr[i + j] != str1Arr[j]):
            break
        j += 1
    if (j == str1L):
        count += 1
        j = 0
        
print (f"String 1 muncul sebanyak {count} kali.")