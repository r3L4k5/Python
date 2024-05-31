
import index as inx
#import battle as btl

player_name = ""
gender = ""
player_gang = []
player_inventory = []

def name_and_gender():
    global player_name, gender, player
    confirm = "no"   

    while confirm == "no" :

        player_name = input("What's your name?: ") 
        player_gender = input("What's your gender?: ")

        confirm = input("\nYou're called '" + player_name + "' and your gender is '" + player_gender + "', yes or no?: ").lower()

        if confirm == "yes":
            player = inx.Trainer(player_name, player_gender, [], [])
            break


name_and_gender()

def open_beast_dex():
    print("\nThe Beastdex:")   
    for beasts in inx.beast_dex:
        align = 17 - len(beasts.name) - 6
        
        if len(beasts.element) == 2:
            print("-", beasts.dex_num,"#", beasts.name, "".rjust(align, " "),beasts.element[0],"/",beasts.element[1]) 
        else:
            print("-", beasts.dex_num,"#", beasts.name, "".rjust(align, " "),beasts.element[0])
   
def add_to_party():
    open_beast_dex()
    choose_beast = input("\nChoose a beast to add to your party from the Beastdex: ").capitalize()

    for i in range(len(inx.beast_dex)):
        if inx.beast_dex[i].name == choose_beast:
            print(inx.beast_dex[i].name + " was added to your party!")
            player.gang.append(inx.beast_dex[i])

for i in range(6):
    add_to_party()
    
    print("\nYour gang: ")
    for i in range(len(player.gang)):
        align = 9 - len(player.gang[i].name)
       
        if len(player.gang[i].element) == 1:
            print(" \n",(i + 1),"-",player.gang[i].name, "".rjust(align, " "),player.gang[i].element[0])
        else:
            print(" \n",(i + 1),"-",player.gang[i].name, "".rjust(align, " "),player.gang[i].element[0],"/",player.gang[i].element[1])

    if i == 5:
        print("\nAlright, now choose your opp: ")
        break

    confirm = input("\nDo you want to add another Beast to your Gang, yes or no?: ").lower()
    if confirm == "no":
        print("\nAlright, now choose your opp!")
        break


    


    




   



    
    
    
    
    



    






