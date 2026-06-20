import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

print("Dataset Preview:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# Clean missing data
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Department"] = df["Department"].fillna("Unknown")

# Filter students with marks > 75
high_scorers = df[df["Marks"] > 75]

print("\nStudents scoring above 75:")
print(high_scorers)

# Grouping and aggregation
dept_avg = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(dept_avg)

print("\nOverall Average Marks:", df["Marks"].mean())
