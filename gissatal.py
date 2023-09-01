# I denna uppgift ska vi öva på variabler, vilkor och loopar
import random
import os
os.system ("cls" if os.name == "nt" else "clear")

print ("\n--------")
print (".:GissaTalet:.")

print ("gissa ett tal mellan 1- 10 och pröva lyckan, du får 3st försök!\n")

slumptal = random.randint(1, 10)

#print(slumptal)

i=0
hitta = False

#loopar

while i < 3:
    gissatalet = input("mata in tal: ")

    if slumptal == int(gissatalet):
        hitta = True
        print("\n Rätt gissat \n")
        break

    i+=1

if hitta:
    print("\n Bra jobbat, här får du en anka lol")

else: 
    print ("Cringe loser")
 