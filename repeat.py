n =int(input())
for z in range(n):
	a = list(input())
	i = j = 0
	count = 0
	flag = True

	while j<len(a) and flag:
		flag = False
		temp = 'C'
		while i<len(a):
			if temp == a[i]:
				a.remove(a[i-1])
				count += 1
				flag = True
				i -=1
			temp = a[i]
			i += 1
	print (count)