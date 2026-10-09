# import sqlite3

# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#        id INTEGER,
#        name TEXT,
#        age INTEGER,
#        city TEXT
# )
# """)

# conn.commit()
# print("表建好了")

# cursor.execute("INSERT INTO users VALUES (1, '小明', 18, '西安')")
# cursor.execute("INSERT INTO users VALUES (2, '小红', 20, '北京')")
# cursor.execute("INSERT INTO users VALUES (3, '小刚', 22, '上海')")
# cursor.execute("INSERT INTO users VALUES (4, '小美', 25, '西安')")
# conn.commit()
# print("插入完成")

# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


#     print("--- 西安的人 ---")
# cursor.execute("SELECT * FROM users WHERE city = '西安'")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

cursor.execute("INSERT INTO users VALUES (1, '小明', 18, '西安')")
cursor.execute("INSERT INTO users VALUES (2, '小红', 20, '北京')")
cursor.execute("INSERT INTO users VALUES (3, '小刚', 22, '上海')")
cursor.execute("INSERT INTO users VALUES (4, '小美', 25, '西安')")

conn.commit()
conn.close()
print("建表+插入完成")

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE city = '西安'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()