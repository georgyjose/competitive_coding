
n,m = map(int,input().split())
if m==1 and n==1:
    print (1)
elif set([m,n])==set([1,2]):
    print(1)
elif set([m,n])==set([1,3]):
    print(2)
elif (m%2!=0 and n%2==0) or (m%2==0 and n%2!=0):
    print(((m*n)//4)+1)
elif (m%2!=0 and n%2!=0):
        print(((m*n)//4)+2)
else:
    print((m*n)//4)