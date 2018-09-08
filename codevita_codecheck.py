n = int(input())
l = [2,3,5,7,11,13,17,19]

c = 0

for i in l:
    if n%i == 0:
        c += 1

print(c)
print(2**c-1)