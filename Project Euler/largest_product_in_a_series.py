import numpy

path = "input_for_largest_product_in_a_series.txt"
with open(path,'r') as a:
    b = list(map(int,(''.join(a.read().split()))))

n = len(b)-13
m = 0
i = 0
while(i<n):
    if numpy.prod(b[i:i+13])>m:
        m = numpy.prod(b[i:i+13])
    i += 1
print (m)