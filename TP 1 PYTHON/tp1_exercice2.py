lettre=(input("Saisir un lettre : "))[0]
 
if(lettre=='a' or lettre=='e' or lettre=='i' or lettre=='o' or lettre=='u' or lettre=='A' or lettre=='E' or lettre=='I' or lettre=='O' or lettre=='U'):
        print(lettre,"est voyelle.")
elif((lettre>= 'a' and lettre <= 'z') or (lettre >= 'A' and lettre <= 'Z')):
    # consonnes */
    print(lettre, "est consonnes.")
else:
    # Ni voyelle ni consonne
    print(lettre," est Ni voyelle ni consonne.")
