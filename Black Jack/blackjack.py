import random 
import card


    
plCount = int(input("Hur många spelare?: "))
plList = []

hands = [[],[],[]]

#for car in card.deck:
    #print(car)

i = 1

for i in range(plCount):
    plName = input(f"Vad heter spelare nummer {i + 1}?: ")
    plList.append([])

for i in range(plCount): 
    hands[i + 1].append(card.random_card())
    hands[i + 1].append(card.random_card())
    


