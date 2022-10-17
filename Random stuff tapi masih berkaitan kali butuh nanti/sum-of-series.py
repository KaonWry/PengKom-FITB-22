n = int(input('N = '))
x = int(input('X = '))
k = int(0)

for i in range (1, n+1):
    j = int(i * str(x))
    print(j)
    k += j
    print (k)