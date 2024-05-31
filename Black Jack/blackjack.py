import random
import card
import os
import time

#Antal spelare som deltar, lista med spelare, lista med värden och lista med deras kort
player_Count = int(input(" \n Hur många spelare?: "))
player_List = []
value_List = []
hands = [[]]

#Anger spelarens namn och läggs sedan till i "player_List[]" samt en tom array i "hands[]"
for i in range(player_Count):
    player_Name = input(f" \n Vad heter spelare nummer {i + 1}?: ")
    player_List.append(player_Name)
    hands.append([])

#Dealerns kort
hands[0].append(card.random_card())
hands[0].append(card.random_card())

dealer_Value = 0

#Kalkylerar dealerns korts värde
def calcdealer_Value(): 
    global dealer_Value, dealer_card
    
    for dealer_card in hands[0]:
        dealer_Value += dealer_card.value

#Spelarnas kort och värde      
player_Value = 0

#Kalkylerar spelarens korts totala värde
def calcplayer_Value(i):
    player_Value = 0
  
    for player_Card in hands[i + 1]:
        player_Value += player_Card.value
        
    value_List.append(player_Value)
    print("\nKortens totala värde är:", player_Value)

#Kalkylerar spelarens korts nya totala värde efter hit
def hit_value(i):
    player_Value = 0
    
    for player_Card in hands[i + 1]:
        player_Value += player_Card.value
    
    value_List[i] = player_Value
    print("\n Amins korts totala värde är:", value_List[i])
    
#Visar spelarens två
def show_hand(i):
    y = 0
    player_hand = []
    
    for y in range(len(hands[i + 1])):
        card_value = str(hands[i + 1][y].value)
        card_deno = str(hands[i + 1][y].deno)
        
        player_hand.append(card_deno)
        player_hand.append(card_value)
    
    print("\nSpelaren", player_List[i], "har korten:", " ".join(player_hand))
        
print(os.system("cls"))

#Fyller på spelarnas "hands[]" med kort från "class card" via "deck[]" och visar deras kort
i = 1

for i in range(player_Count):
    
    hands[i + 1].append(card.random_card())
    hands[i + 1].append(card.random_card())

    show_hand(i)
    calcplayer_Value(i)
    print("______________________________________________________________________")
    
    time.sleep(1.5)

#Visar endast en av dealerns kort
print(" \nDealern har korten:", hands[0][0], "och N/A " )
print("______________________________________________________________________ ")

#Funktion som låter spelare välja "hit" för att dra kort och "stand" för att stå över
def hit_or_stand(i):
    hit = input("\n" + player_List[i] + ", 'hit' eller 'stand'?: ").lower()

    if hit != "hit":
        print("\n", player_List[i], "har valt 'stand' och känner sig färdig" )
        #print("______________________________________________________________________ ")
        done.append(player_List[i])
    
    while value_List[i] < 21 and hit == "hit":   
        time.sleep(1)
        hands[i + 1].append(card.random_card())
        print("\n", player_List[i], "drog kortet:", hands[i + 1][len(hands[i + 1]) - 1])
        hit_value(i)

        if value_List[i] > 21:
            print("\n Kortens totala värde är över 21 och", player_List[i], "kommer inte deltag längre")
            #print("______________________________________________________________________ ")
            break

        elif value_List[i] == 21:
            winner.append(player_List[i])
            print("\n Kortens totala värde är 21 och", player_List[i], "kommer inte kunna dra fler kort")
            #print("______________________________________________________________________ ")
            break
        
        time.sleep(1)
        print("______________________________________________________________________ ")
        hit = input("\n" + player_List[i] + ", hit igen?: ").lower()
        
        if hit != "hit":
            print("\n", player_List[i], "har valt 'stand' och känner sig färdig" )
            done.append(player_List[i])
        
#Lista för spelaren eller spelarna som vinner (winner[]) och lista för dem kan bli uttagna till vinnare (done[])
winner = []
done = []

#Loop som eliminerar spelare, förbjuder spelare från att dra kort och ger spelare alternativet att dra kort
for i in range(player_Count): 
    
    if value_List[i] > 21:
        time.sleep(1)
        print("\n" + player_List[i], "korts totala värde är över 21 och kommer inte deltag längre")
        #print("______________________________________________________________________ ")

    elif value_List[i] == 21:
        time.sleep(1)
        winner.append(player_List[i])
        print("\n" + player_List[i], "korts totala värde är 21 och kommer inte kunna dra fler kort")
        #print("______________________________________________________________________ ")
        
    else:
        time.sleep(1)
        hit_or_stand(i)

    print("______________________________________________________________________ ")
        
time.sleep(1) 
print("\n Dealerns andra kort är:", hands[0][1])
print("______________________________________________________________________ ")


def calc_winners():
    max_done = max(done)
    
    for values in done:
        
        if values == max_done:
            

while dealer_Value < 17:
    
    hands[0].append(card.random_card())
    print("\n Dealern drog kortet:", hands[0][len(hands[0]) - 1])
    calcdealer_Value()
    print("", dealer_Value)

if dealer_Value > 21:
    print("Dealerns korts totala värde är över 21 och kan inte deltag längre")
    calc_winners()
    print("vinnarna är:", " ".join(winner))
    

elif dealer_Value == 21: 
    end_game = input("Dealerns korts totala värde är 21 och utses till spelets vinnare")
    exit 

else:
    calc_winners()
    print("vinnarna är:", " ".join(winner))
    



    

