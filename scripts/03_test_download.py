import pandas as pd

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

df = pd.read_csv(url)

print(df.head())
print()
print("Rows:", len(df))