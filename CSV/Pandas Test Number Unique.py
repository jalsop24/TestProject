import pandas as pd

df = pd.read_csv('partnerize.csv', usecols=['category'])

print(df.nunique())
