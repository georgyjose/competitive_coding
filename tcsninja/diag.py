n = input()

for i in range(n):
    for j in range(n):
        if i+j == n-1 or i == j:
            print "* ",
        else:
            print "   ",
    print ""