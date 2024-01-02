# with a DictReader
import csv

with open("favs_0.csv", "r") as file:
    reader = csv.DictReader(file)
    count = {}
    # phone, laptop, cable = 0, 0, 0
    for row in reader:
        favs = row["item"]
        if favs in count:
            count[favs] += 1
        else:
            count[favs] = 1

favs = input("Favorite item: ").title()
if favs in count:
    print(f"{favs}: {count[favs]}")

def get_value(item):
    return count[item]

#for favs in sorted(count, reverse = True):
#    print(f"{favs}: {count[favs]}")
