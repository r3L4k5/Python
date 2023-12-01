number = input("Vilket tal ska vi förenkla?: ")
ind = list(number)

def cutter():
    for num in ind:
        if num == "0":
            ind.remove(num)
        elif num == ",":
            def cutterDec():
                

