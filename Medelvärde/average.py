
seq = input("Mata in en nummer sikvens: ").split()
newSeq = list(map(int, seq))


if len(newSeq) >= 3:
    for i in range(len(newSeq)):
        
        if i != 0 and i != len(newSeq) -1:
            avg = (newSeq[i] + newSeq[i+1] + newSeq[i-1]) / 3
            print(round(avg, 2))
        else:
            print(newSeq[i])