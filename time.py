a = list(map(int,input().split(',')))
b = []

if 2 in a:
    a.remove(2)
    b.append(2)
    element = -1
    for i in a:
        if i > element and i<=4:
            element = i
    if element == -1:
        a.remove(2)
    else:
        a.remove(element)
        b.append(element)