import csv


# class CatHierarchyRecord:
#     def __init__(self, row):
#         self.cat_hierarchy_code = row[0]
#         self.cat_hierarchy_type = row[2]


with open('/home/tim/Desktop/CatHierarchy.ascii.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    catalogues = [line[0] for line in csvreader if len(line) >= 3 and line[2] == "1"]
    print(catalogues)