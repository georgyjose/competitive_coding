import math
no = int(input())
count = 0

for i in range(2,no):
    int_root = int(math.sqrt(i))
    if math.sqrt(i) != float(int_root):
        # l.append(i)
        if no%i == 0:
            count += 1
print(count)


# print(l)

# for i in l:
#     if no%i == 0:
#         count += 1
        # print(i)
