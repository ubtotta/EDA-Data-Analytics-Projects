import pandas as pd
df=pd.read_csv('titanic.csv')
df['name'].str.split(',',)