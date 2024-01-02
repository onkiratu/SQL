from CS50 import SQL

db = SQL("sqlite:///favs_0.db")

favorite = input("Favorite: ")
rows = db.execute("SELECT * FROM favs_0 WHERE item = 'Phone' ")

for row in rows:
    print(row["Price"])
    
    