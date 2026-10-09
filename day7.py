
# import pandas as pd
# print(pd.__version__)

import pandas as pd
df = pd.read_csv("data.csv")
# print(df)

# print(df["name"])
# print(df["age"].sum())
# print(df["age"].mean())

print(df[df["age"] > 18])
print(df.groupby("city")["age"].sum())