import csv

with open('ab.csv',newline='') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=' ')
    for row in spamreader:
        print (', '.join(row))
        break