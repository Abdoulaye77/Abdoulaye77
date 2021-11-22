# Demandez à l'utilisateur d'entrer un nombre
nbr = int(input("Entrez un nombre: "))

# initialiser la somme
s = 0

# trouver la somme du cube de chaque chiffre
tmp = nbr
while tmp > 0:
   d = tmp % 10
   s += d ** 3
   tmp //= 10

# Afficher le résultat
if nbr == s:
   print(nbr,"est un nombre Armstrong")
else:
   print(nbr,"n'est pas un nombre Armstrong")
