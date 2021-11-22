a=int(input("veillez entrer un nombre"))
b=int(input("veillez entrer un nombre"))
c,d=a,b
while a!=b:
    if a > b:
        b+=d      
    elif a < b:
        a+=c
    print (a,b)    

print ()        
print ("Le PPCM de", c,"et",d,"est :",a)
