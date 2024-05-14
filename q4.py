import pandas as pd

df = pd.read_csv('country_vaccination_stats.csv')


min_vaccinations = df.groupby('country')['daily_vaccinations'].min()

for index, row in df.iterrows():
    if pd.isna(row['daily_vaccinations']):  
        df.at[index, 'daily_vaccinations'] = min_vaccinations.get(row['country'], 0)

print(df)