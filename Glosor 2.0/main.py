import os
import sqlite3 as list
import Gloslista2
import random

sqList, cursor = Gloslista2.connect()

frst = input("Vill du börja med nya glosor? j/n: ")

if frst == 'j':
    Gloslista2.delete(sqList,cursor)


mode = input("Hur vill du ha det? Mata in 1 för Sv till Eng eller 2 för Eng till Sv: ")

if mode == '1':
    naOrd = "svenska"
    trOrd = "engelska"
else:
    naOrd = "engelska"
    trOrd = "svenska"

cont = 'j'

while cont == 'j':

    native = input(f"Mata in ord på {naOrd}: ")
    trans = input(f"Mata in översättning på {trOrd}: ") 

    Gloslista2.addList(native, trans, sqList, cursor)

    cont = input("Mata in 'j' om du vill fortsätta, annars 'n': ")

show = Gloslista2.showList(cursor)

while len(show) != 0:
    word = random.choice(show)
    svar = input(f"Överätt {word[1]} till {trOrd}:  ")
    if svar == word[2]:
        print("Rätt svar!")
    else:
        print("Fel svar!")

    #print(word[2])n
    show.remove(word)

print("Du är klar med programmet!")
