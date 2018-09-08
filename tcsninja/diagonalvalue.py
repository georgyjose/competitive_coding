n = list(raw_input())
i = 0
j = 0

while i<len(n):
    while j<len(n):
        if i==j or i+j==len(n)-1:
            print n[i]+str(" "),
        else:
            print "  ",
        j += 1
    j = 0
    i += 1
    print ""
