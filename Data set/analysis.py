import pandas as pd

df = pd.read_csv('IBM_HR_Attrition_Enhanced.csv')

print("Dataset Shape:", df.shape)

print(df.info())

print(df.describe())

print(df.isna().sum())

print(df.duplicated().sum())

print(df.head())