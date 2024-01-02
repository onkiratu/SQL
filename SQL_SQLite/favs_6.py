import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

try:
    # Begin the transaction
    conn.execute("BEGIN TRANSACTION")

    # Fetch the current likes from the posts table
    post_id = 1  # Replace with the actual post ID
    cursor.execute("SELECT likes FROM posts WHERE id = ?", (post_id,))
    current_likes = cursor.fetchone()[0]

    # Update the likes count
    new_likes = current_likes + 1
    cursor.execute("UPDATE posts SET likes = ? WHERE id = ?", (new_likes, post_id))

    # Commit the transaction
    conn.commit()

except Exception as e:
    # Rollback the transaction if an exception occurs
    print(f"Error: {e}")
    conn.rollback()

finally:
    # Close the database connection
    conn.close()
