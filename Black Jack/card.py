import random

class card:
    def __init__(self, deno, value):
        self.deno = deno
        self.value = value

    def __str__(self):
        return(self.deno + " " + str(self.value))
    
    

deck = [card("Hjärter", 11), card("Spader", 11), card("Klöver", 11), card("Ruter", 11)]

for i in range(2, 11):
    deck.append(card("Hjärter", i))

for i in range(2, 11):
    deck.append(card("Spader", i))

for i in range(2, 11):
    deck.append(card("Klöver", i))

for i in range(2, 11):
    deck.append(card("Ruter", i))

for i in range(3):
    deck.append(card("Hjärter", 10))

for i in range(3):
    deck.append(card("Spader", 10))

for i in range(3):
    deck.append(card("Klöver", 10))

for i in range(3):
    deck.append(card("Ruter", 10))

random.shuffle(deck)

def random_card():
        temp = deck[0]
        deck.remove(temp)
        return temp