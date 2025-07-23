import pandas as pd

frame = pd.read_csv("students.csv")
print("dataframes")
print(frame.head(1))
print(frame.shape)


def multiply_by_100(n):
    return n * 100


frame["NewMathScore"] = frame["MathScore"].apply(multiply_by_100)
print(frame)
# print(frame.groupby("LastName").max())
avg_scores = frame.groupby("LastName")[["MathScore", "ScienceScore", "Grade"]].mean()
# print(avg_scores)
print(frame[["MathScore", "ScienceScore", "Grade"]].apply(pd.Series.round, axis=1))
# print(frame)
