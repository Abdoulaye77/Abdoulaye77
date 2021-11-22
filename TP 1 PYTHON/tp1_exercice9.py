nombre=5
 
somme=0 
n_min=20
n_max=0
 
for i in range(1,nombre+1):
    note=float(input("Veuillez entrer la note suivante"))
     
    while note>20 or note<0: 
        print("Attention! une note est comprise entre 0 et 20")
        note=float(input("Veuillez entrer la note suivante"))
     
    somme +=note 
     
    if n_min>note:
        n_min=note 
    if n_max<note:
        n_max=note 
     
moyenne=somme/nombre
     
print("La moyenne des notes est",moyenne)
print("La note minimale est:",n_min)
print("La note maximale est:",n_max)
