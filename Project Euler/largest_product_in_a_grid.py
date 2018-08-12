import numpy

path = "input_for_largest_product_in_a_grid.txt"

def downmax(b,m):
    d = 20-4
    for j in range(20):
        for i in range(d):
            m = max(m,numpy.prod([b[i][j],b[i+1][j],b[i+2][j],b[i+3][j]]))
    return m
            

def rightmax(b,m):
    d = 20-4
    for i in range(20):
        for j in range(d):
            m = max(m,numpy.prod([b[i][j],b[i][j+1],b[i][j+2],b[i][j+3]]))
    return m

def ondiagonalmax(b,m):
    i = 0
    while i+4<20:
        j = 0
        while j+4<20:
            m = max(m,numpy.prod([b[i][j],b[i+1][j+1],b[i+2][j+2],b[i+3][j+3]]))
            j += 1
        i += 1
    return m

def offdiagonalmax(b,m):
    i = 0
    while i<20:
        j=0
        while j+4<20:
            if i-4>0:
                m = max(m,numpy.prod([b[i][j],b[i-1][j+1],b[i-2][j+2],b[i-3][j+3]]))
                # print(numpy.prod([b[i][j],b[i-1][j+1],b[i-2][j+2],b[i-3][j+3]]))
            j += 1
        i += 1
    return m
    

with open(path,"r") as a:
    b = [list(map(int,i.split())) for i in a]
    
print(downmax(b,0),rightmax(b,0),offdiagonalmax(b,0),ondiagonalmax(b,0))
print("Maximum:",max([downmax(b,0),rightmax(b,0),offdiagonalmax(b,0),ondiagonalmax(b,0)]))