
base_num = int(input("Vilket tal ska användas?: "))

bin_num = bin(base_num)  

print(bin_num.strip("0b"))

i = base_num + 1

while True:
    
    if bin(i).count("1") == bin_num.count("1"):
        print(i)
        break
    i += 1