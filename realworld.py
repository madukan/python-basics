import csv

with open('/home/tim/Desktop/CatHierarchy.csv') as csvfile:
    csvfilereader = csv.reader(csvfile)
    for row in csvfilereader:
        print row
