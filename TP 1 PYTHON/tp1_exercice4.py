pf=float(input("Prix de fabrication : "))
pv=float(input("Prix de vente : "))
 
if(pv > pf):
    montant = pv - pf
    print("Profit = ", montant)
elif(pf > pv):
     
    montant = pf - pv
    print("Perte = ", montant)
else:
    
    print("Ni profit ni perte.")
