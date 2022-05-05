import pandas as pd

url="https://gist.githubusercontent.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv"

df=pd.read_csv(url, sep=",")

print(df.shape[0])

df['Profit (in millions)'] = pd.to_numeric(df['Profit (in millions)'], errors='coerce')

print(df.shape[0] - df['Profit (in millions)'].isnull().sum())

df[~df['Profit (in millions)'].isnull()].to_json("data2.json", orient='records')

df = df[~df['Profit (in millions)'].isnull()]

print(df.sort_values(by=['Profit (in millions)'], ascending=False).head(20))




