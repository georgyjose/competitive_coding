n = int(input())
for i in range(n):
    px, py, qx, qy = map(int,input().split())
    print (str((2*qx)-px)+" "+str(((2*qy)-py)))
    