import os

chat = open('exempel text konversation.txt', 'r', encoding="utf-8-sig")
data = chat.readlines()

delete = input("Vilket namn vill du ta bort?: ")

#print(range(len(data)))
i=0
for line in data:
    name = data[i].split(":")
    #print(name[0])
    if name[0] == delete:
        data.pop(i)

    i += 1



print(data)