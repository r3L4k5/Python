import random
import time
import os

os.system("cls")

player_amount = int(input("\nHur många spelare är det? "))

players = []
player_nr = []

for i in range(player_amount):
    
    player_name = input(f"\nVad heter spelare nummer {i + 1}? ")
    players.append(player_name)
    
    player_nr.append(random.randint(1,6))


    i+=1

os.system("cls")


