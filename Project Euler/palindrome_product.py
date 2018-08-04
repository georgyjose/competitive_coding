def palindrome(n):
    if n == int(str(n)[::-1]):
        return True
    return False

for i in range(998001,10000,-1):
    if(palindrome(i)):
        for j in range(100,1000):
            if i%j ==0 and len(str(i//j))==3:
                print(i,j,i//j)
                break