import random
import time

flower = random.randint(5,10)


while flower > 0:
    
    time.sleep(3)
    print("Älskar mig")

    flower -= 1
    time.sleep(3)
    
    if flower > 0:
        print("Älskar mig inte")

        flower -= 1

time.sleep(3)
print("Slut på blad!")
        
        
    
    
   
    
    
  