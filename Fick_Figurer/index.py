from enum import Enum

class Types(Enum):
    def __str__(self):
        return self.name
    
    Normal = 1,
    Fire = 2,
    Water = 3,
    Electric = 4,
    Grass = 5,
    Ice = 6,
    Fighting = 7,
    Poison = 8,
    Ground = 9,
    Flying = 10,
    Psychic = 11,
    Bug = 12,
    Rock = 13,
    Ghost = 14,
    Dragon = 15,
    Dark = 16,
    Steel = 17,
    Fairy = 18

class Stats: 
    def __init__(self, HP : int, Attack : int, Defence : int, Sp_Attack : int, Sp_Defence : int, Speed : int):
        
        self.HP = HP 
        self.Attack = Attack
        self.Defence = Defence
        self.Sp_Attack = Sp_Attack
        self.Sp_Defence = Sp_Defence
        self.Speed = Speed

class Beasts: 
    def __init__(self, dex_num : int, name : str, element : list, stats: Stats, shiny = False):
        
        self.dex_num = dex_num
        self.name = name
        self.element = element 
        self.stats = stats
        self.shiny = shiny 

class Trainer: 
    def __init__(self, name : str, gender : str, inventory : list, gang : list):
        
        self.name = name
        self.gender = gender
        self.inventory = inventory
        self.gang = gang      

beast_dex = [
    Beasts(1,"Rowlet", [Types.Grass, Types.Flying], Stats(68, 55, 55, 50, 50, 42)),
    Beasts(2,"Datrix", [Types.Grass, Types.Flying], Stats(78, 75, 75, 70, 70, 52)),
    Beasts(3,"Decidueye", [Types.Grass, Types.Ghost], Stats(78, 107, 75, 100, 100, 70)),
    
    Beasts(4,"Litten", [Types.Fire], Stats(45, 65, 40, 60, 40, 70)),
    Beasts(5,"Torracat", [Types.Fire], Stats(65, 85, 50, 80, 50, 90)),
    Beasts(6,"Incineroar", [Types.Fire, Types.Dark], Stats(95, 115, 90, 80, 90, 60)),
    
    Beasts(7,"Poplio", [Types.Water], Stats(50, 54, 54, 66, 56, 40)),
    Beasts(8,"Brionne", [Types.Water], Stats(60, 69, 69, 91, 81, 50)),
    Beasts(9,"Primarina", [Types.Water, Types.Fairy], Stats(80, 74, 74, 126, 116, 60))
]

trainer_list = [
    Trainer("Rasmus", "Man", [], [beast_dex[3], beast_dex[8], beast_dex[5]]),
    Trainer("Anton", "Kvinna", [], [beast_dex[0], beast_dex[1]])
]



        

