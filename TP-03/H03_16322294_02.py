# NIM/NAMA  : 16322294 / Trystan Prastanov Gabriel
# Tanggal   : 19 Oktober 2022
# Deskripsi : Program lampu menyala dan mati

# Input data
lampCount = int(input("Masukan banyak lampu: "))
pressCount = int(input("Masukan berapa kali Tuan Kil menekan tombol: "))
lamp = [0] * lampCount

# Operasi lampu
for i in range (pressCount):
    press = int(input(f"Tombol yang ditekan ke {i + 1}: "))
    # Lampu di ujung kiri
    if (press-1 == 0):
        # Lampu di tengah
        if (lamp[press-1] == 0):
            lamp[press-1] = 1
        elif (lamp[press-1] == 1):
            lamp[press-1] = 0
        # Lampu di kanan
        if (lamp[press-1+1] == 0):
            lamp[press-1+1] = 1
        elif (lamp[press-1+1] == 1):
            lamp[press-1+1] = 0
    # Lampu di ujung kanan
    elif (press-1 == lampCount-1):
        # Lampu di tengah
        if (lamp[press-1] == 0):
            lamp[press-1] = 1
        elif (lamp[press-1] == 1):
            lamp[press-1] = 0
        # Lampu di kiri
        if (lamp[press-1-1] == 0):
            lamp[press-1-1] = 1
        elif (lamp[press-1-1] == 1):
            lamp[press-1-1] = 0
    # Sisanya
    else:
        # Lampu di tengah
        if (lamp[press-1] == 0):
            lamp[press-1] = 1
        elif (lamp[press-1] == 1):
            lamp[press-1] = 0
        # Lampu di kanan
        if (lamp[press-1+1] == 0):
            lamp[press-1+1] = 1
        elif (lamp[press-1+1] == 1):
            lamp[press-1+1] = 0
        # Lampu di kiri
        if (lamp[press-1-1] == 0):
            lamp[press-1-1] = 1
        elif (lamp[press-1-1] == 1):
            lamp[press-1-1] = 0

# Output data
lamp = "".join(map(str, lamp))
print(f"Keadaan akhir rangkaian lampu adalah {lamp}.")