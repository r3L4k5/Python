#Visar vad funktioner är och vad de har för nytta; främst för att slippa repetera kod.

import random

#Skapar en Tuple typ av samling
frukter = ("Banan", "Melon", "Kiwi", "Citron")
looping = True

#Definerar python funktion
def print_fruit(userinput):
    fnr = int(userinput)
    print(f"\n { frukter[fnr-1]} kommer här")

while looping:
    print("________________________________________")

    i=0
    
    for frukt in frukter:
        print(f"{str(i+1)}: {frukt}")
        i += 1
    
    frukter = input("\n Mata in nummer på frukt du vill ha:  ")

    print_fruit(frukter)
    
    go = input("Vill du välja en frunkt till? Ja/Nej ")

    if go == "Nej":
        break
    
