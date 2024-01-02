#Fetching quantity

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("favs_0.db")
cursor = conn.cursor()

# Get user input for favorite item
favorite = input("Favorite: ")

# Use parameterized query to avoid SQL injection
cursor.execute("SELECT * FROM favs WHERE item = ?", (favorite,))

# Fetch all rows
rows = cursor.fetchall()

# Print the prices
for row in rows:
    print(row[2])  # Assuming the price is in the second column (index 1)

# Close the database connection
conn.close()
