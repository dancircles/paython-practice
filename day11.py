import requests

ur1 = "https://api.github.com/users/torvalds"
response = requests.get(ur1)
# print(response.status_code)  #看状态码
# print(response.json())   #转字典

data = response.json()
print(data["name"])
print(data["followers"])
print(data["public_repos"])

import pandas as pd

df = pd.DataFrame([data])
df.to_csv("github_user.csv",index=False)