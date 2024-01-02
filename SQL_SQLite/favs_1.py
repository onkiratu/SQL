import csv

with open("favs_0.csv", "r") as file:
    reader = csv.DictReader(file)
    phone, laptop, cable = 0, 0, 0
    for row in reader: 
        favs = row["item"]
        if favs == "Phone":
            phone += 1
        elif favs == "Laptop":
            laptop += 1
        elif favs == "Cable":
            cable =+ 1

print(f"Phone: {phone}")
print(f"Laptop: {laptop}")
print(f"Cable: {cable}")