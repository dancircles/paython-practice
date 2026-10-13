import requests
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# users = ["torvalds","gvanrossum", "yzhang-gh"]
# results = []

# for user in users:
#     url = f"https://api.github.com/users/{user}"
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             results.append(data)
#         else:
#             print(f"{user}拿不到，状态码{response.status_code}")
#     except Exception as e:
#         print(f"{user} 出错：{e}")

# df = pd.DataFrame(results)
# df = df[["login","name","followers","public_repos"]]
# print(df)

# df.to_csv("github_data.csv",index = False)
# print("已存 github_data.csv")

data = [
    {"login": "torvalds", "name": "Linus Torvalds", "followers": 327495, "public_repos": 12},
    {"login": "gvanrossum", "name": "Guido van Rossum", "followers": 27086, "public_repos": 28},
    {"login": "yzhang-gh", "name": "Yu Zhang", "followers": 265, "public_repos": 27},
]

df = pd.DataFrame(data)
print(df)

df.to_csv("github_data.csv", index=False)
print("已存 github_data.csv")

df2 = pd.read_csv("github_data.csv")
print(df2)

print("总粉丝数：", df2["followers"].sum())
print("平均仓库数：",df2["public_repos"].mean())

df2.plot(x = "login",y = "followers",kind = "bar")
plt.title("GitHub 用户粉丝数")
plt.ylabel("粉丝数")
plt.show()

conn = sqlite3.connect("github.db")
df2.to_sql("users",conn,if_exists="replace",index = False)
conn.close
print("已存数据库 github.db")


conn = sqlite3.connect("github.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close

        