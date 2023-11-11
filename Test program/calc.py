import time

opr = input(" \n + -> Addition \n\n - -> Subtraktion \n\n * -> Multiplikation \n\n / -> Division \n \n")

numbers = []

cont = "ja"

numbers[0] = int(input("Mata in ett tal: "))
numbers[1] = int(input("Mata in ännu ett tal: "))

while cont == "ja":
    
    cont = input("Vill du ha ett till tal? (ja eller nej): ").lower()
    
    if cont == "nej":
        break
    else:
         entry = input("Mata in ett tal: ")
         numbers.append()
           
i = 0

def addition():
   
   for i in range(len(numbers)):
      result = numbers[i] / numbers[i+1]
      print("Resultat: " + result)

      i+=1

       
def subtraktion():

    for i in range(len(numbers)):
        result = numbers[i] / numbers[i+1]
        print("Resultat: " + result)

        i+=1

def multiplikation():

    for i in range(len(numbers)):
        result = numbers[i] / numbers[i+1]
        print("Resultat: " + result)

        i+=1

def division():

    for i in range(len(numbers)):
        result = numbers[i] / numbers[i+1]
        print("Resultat: " + result)

        i+=1


#nr1 = int(input("\n Första talet: "))
#nr2 = int(input("\n Andra talet: "))

match opr:
    case "+":
       addition()
    case "-": 
       subtraktion()
    case "*":
        multiplikation()
    case "/":
        division()
    
time.sleep(10)
