import csv

with open ("favs_0.csv", 'r') as file:
    reader = csv.reader(file)
    #next(row) #ignores header
    for row in reader:
        print(row[1])
        
'''        
import csv

with open ("favs_0.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
    favs = row[1]
        print(favs)
'''