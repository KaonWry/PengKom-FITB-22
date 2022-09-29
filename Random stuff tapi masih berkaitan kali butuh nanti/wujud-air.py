InpSuhu = int(input('Masukan suhu : '))
if (InpSuhu <= 0) :
    print ('Air beku')
elif (InpSuhu > 0 and InpSuhu < 100) :
    print ('Air cair')
else :
    print ('Air uap')