import math
no = 10**9
l = []
with open("output.txt","w") as a:
    for i in range(no):
        if math.sqrt(i) == float(int(math.sqrt(i))):
            print(i)
            a.write(str(i)+" ")