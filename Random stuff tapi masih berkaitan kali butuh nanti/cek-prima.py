while True :
    InpNumber = int(input('Input the number (positive integer only) : '))
    if(InpNumber > 0):
        break
    
if (InpNumber == 1) :
    print ('1 is neither prime nor composite number')
    exit()
    
i = int(0)    
while (i < InpNumber) :
    i+=1
    if (i == 1) :
        continue
    elif (i == InpNumber) :
        continue
    elif (InpNumber % i == 0) :
        print (InpNumber, 'is not a prime number')
        exit()
        
print (InpNumber, 'is a prime number')