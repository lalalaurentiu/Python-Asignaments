import calc

with open('C:/Users/laure/Desktop/test/expresii.txt','r') as f:
    for line in f:
        line = line.rstrip('\n')
        iesire = open('C:/Users/laure/Desktop/test/iesire.txt','a+')
        if line[1] == '-':
            iesire.write(line+'='+str(calc.sum(int(line[0]), int(line[-1]))))
        else: 
            iesire.write('\n'+line+'='+str(calc.sum(int(line[:2]), int(line[-1]))))
f.close
    
 