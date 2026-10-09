import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT city, COUNT(*) FROM users GROUP BY city")
cursor.execute("SELECT * FROM users ORDER BY age")
cursor.execute("SELECT * FROM users ORDER BY age DESC")


rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()