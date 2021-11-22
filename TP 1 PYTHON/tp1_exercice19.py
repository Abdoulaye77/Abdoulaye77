n=int(input('entrer un nombre'))

for a in range(1,n+1):
    sa=0
    for i in range(1,a):
        if a%i==0:
            sa=sa+i
    if sa==a:
        print(a)
