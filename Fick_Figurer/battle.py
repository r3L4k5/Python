import index as inx
#import setup as stp

#Variabler
opp_name == ""

#Funktioner
def show_opp():

    for i in range(len(inx.trainer_list)):
        print("\n " + inx.trainer_list[i].name + "'s Gang:")
        
        for x in range(len(inx.trainer_list[i].gang)):
            align = 10 - len(inx.trainer_list[i].gang[x].name) 
           
            if len(inx.trainer_list[i].gang[x].element) == 1:
                print(" -",(x + 1), inx.trainer_list[i].gang[x].name, "".rjust(align, " "),inx.trainer_list[i].gang[x].element[0])
            else: 
                print(" -",(x + 1), inx.trainer_list[i].gang[x].name,
                       "".rjust(align, " "),inx.trainer_list[i].gang[x].element[0],"/",inx.trainer_list[i].gang[x].element[1])

def choose_opp():
    global opp_name
    
    opp_name = input("\nWho will you challenge?: ").capitalize()
    print("\nYou've challenged",opp_name,"!")
    print("The battle has commenced!")

def battle_start(opp_gang):
    print(opp_name, "has sent out", opp_gang[1])
    print("You sent out", )

for trainer in inx.trainer_list:
        if trainer.name == opp_name:
            battle_start(trainer.gang)


   
            

