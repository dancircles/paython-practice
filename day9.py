import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]   # 用黑体
plt.rcParams["axes.unicode_minus"] = False      # 负号正常显示


df = pd.read_csv("data.csv")
print(df.sort_values("age"))
print(df.sort_values("age",ascending=False))

df2 = pd.read_csv("data2.csv")
print(df2.groupby("city")["age"].mean())
print(df2.groupby("city")["age"].count())

df.plot(x = "name", y = "age", kind = "bar")

plt.show()