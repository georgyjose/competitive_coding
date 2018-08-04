# import math

n,m = map(int,input().split())
if (m%2!=0 and n%2==0) or (m%2==0 and n%2!=0):
    print(((m*n)//4)+1)
elif (m%2!=0 and n%2!=0):
        print(((m*n)//4)+2)
else:
    print((m*n)//4)