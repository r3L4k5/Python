import index as inx
import random as r

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
    global opp
    
    show_opp()
    opp_name = input("\nWho will you challenge?: ").capitalize()
    print("\nYou've challenged",opp_name,"!")
    print("\nThe battle has commenced!")

    for trainer in inx.trainer_list:
        if trainer.name == opp_name:
            opp = trainer
    
    return opp

def beast_status(active_beasts):
    print("\nOpp's", active_beasts[0].name, "HP:", active_beasts[0].stats.HP)
    print("Your", active_beasts[1].name, "HP:", active_beasts[1].stats.HP)

def fight(player):
    active_beasts = [opp.gang[0], player.gang[0]]
    beast_status(active_beasts)
    
    if active_beasts[1].stats.Speed > active_beasts[0].stats.Speed:
        print("\nYour", active_beasts[1].name, "attacked")
        active_beasts[0].stats.HP -= damage_calc(active_beasts[1], active_beasts[0])
        beast_status(active_beasts)

        faint(player, active_beasts)

        print("\nOpp's", active_beasts[0].name, "attacked")
        active_beasts[1].stats.HP -= damage_calc(active_beasts[0], active_beasts[1])
        beast_status(active_beasts)

        faint(player, active_beasts)
        
    else:
        print("\nOpp's", active_beasts[0].name, "attacked")
        active_beasts[1].stats.HP -= damage_calc(active_beasts[0], active_beasts[1])
        beast_status(active_beasts)

        faint(player, active_beasts)
        
        print("\nYour", active_beasts[1].name, "attacked")
        active_beasts[0].stats.HP -= damage_calc(active_beasts[1], active_beasts[0])
        beast_status(active_beasts)

        faint(player, active_beasts)
    
    
def faint(player, active_beasts):
    for i in range(2):

        if active_beasts[i].stats.HP <= 0 and active_beasts[i] == opp.gang[0]:
            print("\n"+ active_beasts[0].name, "has fainted")
            opp.gang.pop(0)
            
            try:
                active_beasts[0] = opp.gang[0]
            except:
                print("\nAll Opp's Beasts fainted! You won!")
                quit()
        
        if active_beasts[i].stats.HP <= 0 and active_beasts[i] == player.gang[0]:
            print("\n"+ active_beasts[1].name, "has fainted")
            player.gang.pop(0)
            
            try:
                active_beasts[1] = player.gang[0]
            except:
                print("\nAll your Beasts fainted! You've been defeated!")
                quit()
            
    return active_beasts

def damage_calc(beast_off, beast_def):
    effect_mult = 1
    dmg = round(((22 * 75 * beast_off.stats.Attack / beast_def.stats.Defence) / 50) * effect_mult * (r.randint(217, 255) / 255))
    
    return dmg

