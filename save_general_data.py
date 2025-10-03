import os
import pandas as pd

general_df = pd.DataFrame(columns=['id', 'name', 'matches_played', 'GF', 'GC'])
dict_ids = dict()

for i in range(len(os.listdir('raw_data'))):
    dict_ids[i+1] = os.listdir('raw_data')[i]

for i in dict_ids:
    df = pd.read_excel(f'raw_data/{dict_ids[i]}')
    name = dict_ids[i].replace('raw_', '').replace('.xlsx', '')
    general_df.loc[i-1] = [i, name, len(df) , sum(list(df['GF'])), sum(list(df['GC']))]

ids_df = general_df[['id', 'name']]

general_df.to_excel('general_data/general_df.xlsx', index=False)
ids_df.to_excel('general_data/ids.xlsx', index=False)
print('---Data saved in general_data/---')