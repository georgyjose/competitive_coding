no_of_samples , no_of_ranges = map(int,input().split())
list_of_samples = list(map(int,input().split()))
ranges = []
for i in range(no_of_ranges):
    a,b=map(int,input().split())
    ranges.append([a,b,0])
for i in list_of_samples:
    for j in ranges:
        if i in range(j[0],j[1]):
            j[2] += 1
for j in ranges:
    print (j[2])