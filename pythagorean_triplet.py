for i in range(500,1,-1):
    for j in range(500,1,-1):
        for k in range(500,1,-1):
            if not (i<j<k):
                continue
            if((i**2)+(j**2)==(k**2) and i+j+k ==1000):
                print(i,j,k)    #values of a, b and c
                print(i*j*k)    #answer
                exit(0)
                