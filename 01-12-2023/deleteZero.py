number = str(input("Vilket tal ska vi förenkla?: "))

def cutter():
    y = number.strip("0")
    return y

x = cutter()

print(x)