n = int(input())

for i in range(n):
    a = input()
    i = 0
    count = 0
    while(2*i)<len(a):
        if ord(a[i]) == ord(a[(i+1)*-1]):
            i += 1
            continue
        elif ord(a[i]) > ord(a[(i+1)*-1]):
            count += ord(a[i])-ord(a[(i+1)*(-1)])
        else:
            count += ord(a[(i+1)*(-1)])-ord(a[i])
        i += 1
        # print(i)
    print(count)
    