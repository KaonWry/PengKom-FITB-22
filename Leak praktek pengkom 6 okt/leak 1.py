# Input data
inpA = int(input('Masukan nilai A: '))
inpB = int(input('Masukan nilai B: '))

# Loop
for i in range(1, 10+1) :
    bCoef = 2*(i-1)
    print((inpA + (bCoef*inpB))**i, end=' ')
print(' ')
