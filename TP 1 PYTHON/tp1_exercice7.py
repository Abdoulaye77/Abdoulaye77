mot=str(print("Pour sortir de la boucle suivante, il suffira d'entrer le mot \"fin.\n\n"))
    
while mot != "fin" :
    mot=input("Rentrez un mot (sans accent) : ")
    mot_min=mot.lower()     
    
    liste_voyelles=["a","e","i","o","u","y"] 
    nb_voyelles = 0         
    for lettre in mot_min : 
        if lettre in liste_voyelles :
            nb_voyelles+=1
    
    if   nb_voyelles == 0 : 
        print("Il n'y a pas de voyelles dans le mot \"" + mot + "\".\n")
    elif  nb_voyelles == 1 :
        print("Il y a une seule voyelle dans le mot \"" + mot + "\".\n")
    else :  
        print("Le mot \"" + mot + "\" contient " + str(nb_voyelles) + " voyelles.\n")
print("\n\n")
input("Appuyer sur ENTER pour terminer le programme. ")
