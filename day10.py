import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


df = pd.read_csv("project.csv")
print("清洗前缺失数：")
print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["city"] = df["city"].fillna("未知")

print("清洗后")
print(df)
print("清洗后缺失数：")
print(df.isnull().sum())

print("各城市平均工资：")
print(df.groupby("city")["salary"].mean())

df.groupby("city")["salary"].mean().plot(kind = "bar")
plt.title("各城市平均工资")
plt.ylabel("工资")
plt.show()

df.to_csv("project_clean.csv", index=False)