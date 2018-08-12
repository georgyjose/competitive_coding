n = int(input())
l = [2,3,5,7,11,13,17,19]
p = n**0.5
c = 0
for i in l:
    if n%i ==0:
        c += 1

print(2**c-1)