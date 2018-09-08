import csv

with open('at.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    temp = 0
    for row in spamreader:
        name = row[0]
        print(name)