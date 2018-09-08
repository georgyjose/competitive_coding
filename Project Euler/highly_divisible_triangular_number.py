"""a= []

n = 0

while True:
    n += 1
    triangular_no = (n*(n+1)//2)
    count = 0
    print(triangular_no,end=' ')
    for i in range(1,triangular_no+1):
        if triangular_no%i==0 and triangular_no>0:
            # triangular_no = triangular_no//i
            count += 1

        if count>500:
            print("Answer:",n*(n+1)//2)
            exit(0)
    print(count)"""
	
"""import math

def prime(n):
	k = int(math.sqrt(n))
	for i in range(2,k+1):
		if n%i == 0:
			return False
	return True

count = 0
start = 1
i = 2
while True:
	if count == 500:
		print("start:",start)
		exit(0)
	if prime(i):
		start *= i
		count += 1
		print(count)
	i += 1"""