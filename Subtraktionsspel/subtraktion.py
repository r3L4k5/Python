
pot = 50

while pot > 0:
       
    player_list= ["Player1", "Player2"]

    for player in player_list:

        if pot < 0:
            break
        
        print("Pot =", pot)
        minus = input(f"Hur mycket vill du minska från poten, {player}?: ")
            
        if int(minus) > 5 or int(minus) < 1 and player ==  "Player 1":
            print("Player1 you lose!!!")
            quit()
                
        elif int(minus) > 5 or int(minus) < 1 and player ==  "Player 1": 
            print("Player1 you lose!!!")
            quit()
            
        pot -= int(minus)

if player == "player1":
    print("Player1 has won and Player2 has lost!")
    
else:
    print("Player2 has won and Player1 has lost!")

    






