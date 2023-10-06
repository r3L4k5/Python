import random

class lott:

    def __init__(self):

        self.list_vinster = [
            "Kruka",
            "Fot massage från Amin",
            "Strumpa med hål",
            "Trasig ballong",
            "Fri entré på soptippen",
            "Ruta Marabou cholklad",
            "Ofungerande whiteboard tavla",
            "Sten från 1700-talet",
            "Date med Emil",
            "Liter påse med mjäll"
        ]
    
    def get_vinst(self):
        slumptal = random.randint(0, len(self.list_vinster)-1)
        return self.list_vinster[slumptal]