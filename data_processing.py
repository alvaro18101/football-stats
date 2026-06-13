# Functions

to_boolean = lambda x: True if x == 'Home' else False

import pandas as pd

input_folder = 'world_cup_scraped_data'
name = 'México'
df = pd.read_excel(f'{input_folder}/raw_{name}.xlsx')

df['local'] = df['local'].apply(to_boolean)
df['possession'] = pd.to_numeric(df['possession'].str[:-1], errors='coerce')/100
df['passing_accuracy'] = pd.to_numeric(df['passing_accuracy'].str[:-1], errors='coerce')/100


output_folder = 'processed_data'

df.to_excel(f'{output_folder}/{name}.xlsx', index=False)
df.to_csv(f'{output_folder}/{name}.csv', index=False)
print(f'---Saved data in {output_folder}---')