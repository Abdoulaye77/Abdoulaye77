annee=int(input("Saisir une année : "))
 
if(((annee % 4 == 0) and (annee % 100 !=0)) or (annee % 400==0)):
    print(annee," est une année bissextile")
else:
    print("Année simple")
