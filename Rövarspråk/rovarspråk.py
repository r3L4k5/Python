
vocals = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]

user_text = list(input("Vad vill du omvandla till rövarspråk?: ").lower())
new_list = []

for letter in user_text:
   
    if letter in vocals:
        
        letter += "o" + letter
        new_list.append(letter)
        continue

    new_list.append(letter)

new_text = "".join(new_list)

print(new_text)
    
