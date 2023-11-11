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


    
for i in range(len(players)):
    
    while len(players) >1 and i <= len(players):

        death = random.randint(1,6)
        
        os.system("cls")


        print(f"""  \n         ⢦⣤⣴⣶⣶⣶⣶⣶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⣆
    ⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠏⠉⠉⠉⠉⠉⠉⠉⠉
    ⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⣾⣿⣿⣿⣿⣿⢿⣿⠛⠿⡿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⣾⣿⣿⠁⠀⠈⠇⠀⢿⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣾⣿⣿⡇⠀⠀⠀⠈⠂⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             
      \n Avgör spelaren {players[i]}s öde...""")
        
        time.sleep(random.randint(3,6))
    
        if player_nr[i] == death:
            
            print(f"\n Spelaren {players[i]} elimineras \n ")
            players.pop(i)
            time.sleep(random.randint(2,2))
            i+=1
            if i >= len(players) :
                i+=1
                break

        else:
            print(f"\n Spelaren {players[i]} kvarstår \n")
            time.sleep(random.randint(2,2))
            i+=1
            if i >= len(players):
                
                break

    
        #player_amount += 1
    

print(f" Spelaren {players[0]} vann #1 ")
time.sleep(10)

