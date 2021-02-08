def Convert(string): 
    list1 = list(string.split(",")) 
    return list1


string = "3,9,13,4,42"


c = Convert(string)
d = []


for i in range(len(c)): 
    c[i] = int(c[i])
    d.append(c[i])


for j in range(len(d)):
    d[j] = d[j] ** 2

    
print(','.join(str(numbers) for numbers in d))
