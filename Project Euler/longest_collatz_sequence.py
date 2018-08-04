n = 1
while (n<1000000):
    if n%2 == 0:
        n = 2*n
        print(n)
    else:
        n = (n - 1)//3
        print(n)
    
print("abc: ",n)