path="sheet.txt"
with open(path,"w") as a:
    for i in range(1,600):
        for j in range(1,51):
            a.write("Person "+str(i)+"\n")
        # a.write("\n")