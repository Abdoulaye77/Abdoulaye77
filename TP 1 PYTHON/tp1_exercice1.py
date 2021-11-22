X=int(input("Saisir le nombre 1 : "))
Y=int(input("Saisir le nombre 2 : "))
Z=int(input("Saisir le nombre 3 : "))

if X> Y:
    if X > Z:
        max = X
    else:
        max = Z
else:
    if Y > Z:
        max = Y
    else:
        max = Z

print("le maximum est = ", max)
