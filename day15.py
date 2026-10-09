# import sqlite3

# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS orders (
#     order_id INTEGER,
#     user_id INTEGER,
#     amount INTEGER
# )
# """)

# cursor.execute("INSERT INTO orders VALUES (101, 1, 500)")
# cursor.execute("INSERT INTO orders VALUES (102, 1, 300)")
# cursor.execute("INSERT INTO orders VALUES (103, 2, 800)")
# cursor.execute("INSERT INTO orders VALUES (104, 4, 200)")

# conn.commit()
# conn.close()
# print("orders 表建好，数据插入完成")

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# cursor.execute("""
# SELECT users.name, orders.amount
# FROM users
# JOIN orders ON users.id = orders.user_id
# """)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

cursor.execute("""
SELECT users.name, SUM(orders.amount)
FROM users
JOIN orders ON users.id = orders.user_id
GROUP BY users.name
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()