import requests
import pandas as pd

users = ["torvalds", "gvanrossum", "yzhang-gh","不存在的用户xyz"]
results = []

for user in users:
    url = f"https://api.github.com/users/{user}"
    try:
       response = requests.get(url)
       if response.status_code == 200:
         data = response.json()
         results.append(data)
       else:
         print(f"{user} 拿不到，状态码 {response.status_code}")
    except:
       print(f"{user} 出错，跳过")

df = pd.DataFrame(results)
print(df[["login", "name", "followers", "public_repos"]])

df.to_csv("github_users.csv", index=False)