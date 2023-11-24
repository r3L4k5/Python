
pers = input("Mata in ditt förbannade personummer(ÅÅÅÅMMDDXXXX): ")

totalSum = 0
persNr = []

for numbers in pers:
    persNr.append(int(numbers))

for i in range(len(persNr)): 
    
    if i % 2 == 0:
        int(persNr[i]) * 2
        
        if persNr[i] >= 10:
            nr1 = persNr[i][:1]
            nr2 = persNr[i][-1:]
            
            totalSum += nr1 + nr2
        else:
            totalSum += persNr[i]
            

checkNr = (10-(totalSum % 10))%10

print(checkNr, persNr)

if checkNr == persNr[11]:
    print("Grattis din fjolle, ditt personummer är giltigt")
else:
    print("Skaffa dig ett riktigt personnummer, jävla stolpskott")
    
    
        

