
"""while len(player_List) > 0:
    
    if value_List[i] == 21:
        done.append(player_List[i])
        print("Spelaren", player_List[i] + "s kort totala värde är 21 och kan därför inte dra fler kort")
            
        player_List.remove(player_List[i])
        value_List.remove(value_List[i])
        hands.remove(hands[i])
        i -= 1
                
    elif value_List[i] > 21:
        print("Spelaren", player_List[i] + "s korts totala värde är över 21 och elimineras därför från spelet")
                
        player_List.remove(player_List[i])
        value_List.remove(value_List[i])
        hands.remove(hands[i])
        i -= 1
                    
    else:
        hit_option = input("\nSpelare " + player_List[i] + ", hit eller stand?: ").lower()
        print(os.system("cls"))
                    
        if hit_option == "hit":
            
        else: 
            print("Spelaren", player_List[i] + " väljer att inte att dra ett nytt kort" )
            done.append(player_List[i])
            player_List.remove(player_List[i])
        
        i += 1
        print("______________________________________________________________________")"""


#Avslöjar dealerns dålda andra kort
"""print("Dealerns andra kort:", hands[0][1], "\n\n Kortens värde är", dealer_Value)

winner = []
if dealer_Value == 21:
    print("Dealern korts värde är 21 och har därför vunnit spelet!")

elif dealer_Value < 16:
    hands[0].append(card.random_card())
    print("Dealern har dragit kortet:", hands[0][len(hands[0]) - 1])

else: 
    done.sort
    for i in range(len(done)):
        if value_List == max(value_List)"""