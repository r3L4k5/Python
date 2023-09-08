# I denna uppgift ska vi öva på variabler, vilkor och loopar
import random
import os
os.system ("cls" if os.name == "nt" else "clear")

print ("\n--------")
print (".:GissaTalet:.")

print ("Gissa ett tal mellan 1- 10 och pröva lyckan, du får 3st försök!\n")

slumptal = random.randint(1, 10)

#print(slumptal)

i=0
hitta = False

#loopar

while i < 3:
    gissatalet = input("\nMata in tal: ")

    if slumptal == int(gissatalet):
        hitta = True
        #print("\n Rätt gissat, här får du en anka \U0001f986 lol")
        break

    i+=1
    
    if i < 3: 
     
     if i == 2:
        print("Du har {} gissning kvar" .format(3 - i))
     else: 
        print("Du har {} gissningar kvar" .format(3 - i))
     
     if int(gissatalet) > slumptal:
        print("Talet du är efter är lägre!") 
     else:
        print("Talet du är efter är högre!")
 
        


if hitta:
    print("\nRätt gissat, här får du en anka \U0001f986 lol\n")
 
else: 
    print("\nCringe loser, couldn't be me\n")
    
    
    
 