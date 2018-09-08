a = map(int,raw_input().split(':'))
b = map(int,raw_input().split(':'))
c = [0,0,0]
for i in range(len(a)-1,-1,-1):
    if a[i] >= b[i]:
        c[i] = a[i]-b[i]