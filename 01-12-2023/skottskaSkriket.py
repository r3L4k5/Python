
text = input("Mata in här: ").lower()

scottish = ""

for vocals in text:
    if vocals == "a" or vocals == "o" or vocals == "i" or vocals == "u" or vocals == "y" or vocals == "å" or vocals == "ä" or vocals == "ö":
        vocals = "e"

    scottish += vocals

print(scottish.upper())