def prime(number):
    limit = int(number**0.5)
    for i in range(2,limit):
        if number %i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for i in range(1,n):
        if n%i == 0:
            if prime(i):
                count += 1
    print (count)