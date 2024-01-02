# Begin Transaction, Commit
#Likes management on a social media post

db.execute("BEGIN TRANSACTION")
rows = db.execute("SELECT likes FROM posts")
likes = rows[0]["likes"]
db.execute("UPDATE posts SET likes = ? WHERE id = ?", likes + 1, id); 
db.execute("COMMIT")
