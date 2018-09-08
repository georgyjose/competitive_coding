n = input()
k = 1
for i in range(n):
    for j in range(n-i,0,-1):
        print " ",
    l = 0
    while(l<k):
        print "*",
        l += 1
    k = (k*2)-1
    print ""
