ll = int(input("Enter starting range: "))
ul = ll*10
pow = len(str(ll))

for n in range(ll,ul):
    a = 10**(pow-1)
    k = list(map(int,str(n)))
    for i,j in enumerate(k):
        k[i]=k[i]**pow
    if sum(k) == int(n):
        print(n)