n = input()
for i in range(n):
    for j in range(n):
        if i==n-1 or (i==j and i>=n/2) or (i+j==(n-1) and i>n/2):
            print "* ",
        else:
            print "  ",
    print ""