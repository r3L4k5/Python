
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','å','ä','å']

word =(input("Vad är det för ord du vill konvertera?: ")).lower()

con_Word = ""

def converter():
    global con_Word
    for letter in word:
        con_Word += alphabet[alphabet.index(letter) + 1]
    return con_Word
x = converter()

print(x)
                   