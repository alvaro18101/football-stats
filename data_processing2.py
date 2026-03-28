# Functions

to_boolean = lambda x: True if x == 'Home' else False

import pandas as pd
name = 'barcelona'
df = pd.read_excel(f'barcelona_matches_complete.xlsx')

df['local'] = df['local'].apply(to_boolean)
df['possession'] = pd.to_numeric(df['possession'].str[:-1], errors='coerce')/100
df['passing_accuracy'] = pd.to_numeric(df['passing_accuracy'].str[:-1], errors='coerce')/100
df['possession_against'] = pd.to_numeric(df['possession_against'].str[:-1], errors='coerce')/100
df['passing_accuracy_against'] = pd.to_numeric(df['passing_accuracy_against'].str[:-1], errors='coerce')/100

df.to_excel(f'processed_data/{name}.xlsx', index=False)
df.to_csv(f'processed_data/{name}.csv', index=False)
df.info()
print('---Saved data---')