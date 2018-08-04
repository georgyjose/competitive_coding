import math

def prime(n):
    k = int(math.sqrt(n))
    for i in range(2,k+1):
        if n%i == 0:
            return False
    return True

k = 2000000
s = 0
for i in range(2,k+1):
    if prime(i):
        s += i

print(s)