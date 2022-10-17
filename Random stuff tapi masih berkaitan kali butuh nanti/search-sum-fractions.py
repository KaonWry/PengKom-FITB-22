inpN = int(input('N = '))
inpX = int(input('X = '))
totalSum = int(0)

for i in range(1, inpN+1) :
    a = i * 2
    b = i * inpX
    print (f'{a}/{i}*{inpX}', end = ' + ')
    totalSum += a / b
print ('')
print (totalSum)