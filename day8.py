import pandas as pd
df = pd.read_csv("data2.csv")
print(df)
print(df.isnull())

# print(df.dropna())
# print(df.fillna(0))

# df.columns = ("姓名","年龄","城市")
# print(df)

# df.to_csv("result2.csv",index = False)