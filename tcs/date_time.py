# 0,0,1,2,2,2,3,5,9,9,9,9

def MonthMax(a,b):
    if 0 not in a or 1 not in a:
        print(0)
        exit(0)
    if 1 in a:
        b.append(1)
        a.remove(1)
        if 2 in a:
            b.append(2)
            a.remove(2)
            return a,b
        if 1 in a:
            b.append(1)
            a.remove(1)
            return a,b
        if 0 in a:
            b.append(0)
            a.remove(0)
            return a,b
    if 0 in a:
        b.append(0)
        a.remove(0)
        m = max(a)
        a.remove(m)
        b.append(m)
    print(0)
    exit(0)    
    
def DateMax(a,b):
    if 0 not in a or 1 not in a or 3 not in a:
        print(0)
        exit(0)
    if 3 in a:
        b.append(3)
        a.remove(3)
        if 1 in a:
            b.append(1)
            a.remove(1)
            return a,b
        if 0 in a:
            b.append(1)
            a.remove(1)
            return a,b
    if 2 in a:
        b.append(2)
        a.remove(2)
        m = max(a)
        a.remove(m)
        b.append(m)
        return a,b

    if 1 in a:
        b.append(2)
        a.remove(2)
        m = max(a)
        a.remove(m)
        b.append(m)
        return a,b

    if 0 in a:
        b.append(2)
        a.remove(2)
        m = max(a)
        a.remove(m)
        b.append(m)
        return a,b


        


a = list(map(int,input().split(",")))
b = []
print(a)
a,b=MonthMax(a,b)
print(a)
print(b)
a,b=DateMax(a,b)
print(a)
print(b)