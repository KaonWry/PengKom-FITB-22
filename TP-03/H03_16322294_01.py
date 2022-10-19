# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 19 Oktober 2022
# Deskripsi : Program menghitung diskon terbesar

# Input data
dataCount = int(input("Masukan banyak barang: "))
price = [0] * dataCount
discount = [0] * dataCount
priceCut = [0] * dataCount

# Input harga barang
for i in range(dataCount):
    price[i] = int(input(f"Masukan harga bawal barang ke-{i + 1}: "))

# Input diskon barang
for i in range(dataCount):
    discount[i] = int(input(f"Masukan besar diskon (dalam persen) barang ke-{i + 1}: "))

# Hitung potongan harga
for i in range(dataCount):
    priceCut[i] = int(price[i] * (discount[i] / 100))

# Output data
print(f"Barang {priceCut.index(max(priceCut)) + 1} memiliki diskon paling besar yaitu {max(priceCut)}.")