
import pandas as pd

df = pd.read_csv('partnerize.csv', usecols=['price'])

count = df[df <50].count()


print(count)
