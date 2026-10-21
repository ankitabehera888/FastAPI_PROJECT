import sqlite3

conn = sqlite3.connect("blog.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE posts
SET user_id = 2
WHERE id = 1
""")

conn.commit()

print("Updated successfully!")

conn.close()