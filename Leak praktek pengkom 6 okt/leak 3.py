# Input data
inpA = int(input('Masukan nilai A: '))
inpB = int(input('Masukan nilai B: '))
inpT = int(input('Masukan tinggi persegi: '))
inpL = int(input('Masukan lebar persegi: '))

row = 1
col = int()
for i in range(1, inpT + 1):
    col = row
    for j in range(1, inpL + 1):
        print(col, end=' ')
        col += inpA
    print('')
    row += inpB