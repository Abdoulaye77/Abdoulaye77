
from random import randrange

n = 0
 

print("\t\t\t\t=== LE JEU DU PLUS OU MOINS ===\n\n")

nm = randrange(1, 100)
 
while n != nm:
     
    print("Quel est le nombre ?")
 
    
    n = input()
    n = int(n)
 
    
    if n < nm:
        print("C'est trop petit !\n")

    elif n > nm:
        print("C'est trop grand !\n")
 

    else:
        print("Félicitations, vous avez trouvé le nombre mystère !!!\n")

 
