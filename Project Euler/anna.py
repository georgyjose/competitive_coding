from itertools import permutations
a = list(input())
b = list(permutations(a))

c = []
for i in b:
    c.append(''.join(i))
for i in c:
    print(i)