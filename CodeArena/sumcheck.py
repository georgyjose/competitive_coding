t = int(input())
for i in range(t):
    input()
    a = sorted(list(map(int,input().split())))
    summ = int(input())
    # print (a)
    s = 0
    i = 0
    flag = True
    while i<len(a) and flag:
        s += a[i]
        if s>summ:
            flag = False
            print("NO")
        elif s==summ:
            print("YES")
            flag = False
        i += 1