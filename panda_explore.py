import pandas as pd
df=pd.read_csv("students.csv")
print(df.head())
print(df.sort_values("MathScore",ascending=False))
print(df.groupby("LastName")["MathScore"]\
      .agg(["mean","min","max"]))


data = {
    "Name": ["Bob", "Alice", "Charlie","Allen"],
    "MathScore": [88, 95, 95, None],
    "EnglishScore": [90, 85, 78,67]
}
df = pd.DataFrame(data)
df.set_index("Name", inplace=True)
print(df)
print(df.info())
print(df.describe())
# # Sort columns (axis=1 means sort along columns)
sorted_columns_df = df.sort_index(axis=0)#sort index by row

print(sorted_columns_df)
print(df.sort_values(by=["MathScore","EnglishScore"],\
                     ascending=[True, True],na_position="first"))
print(df.dropna())



