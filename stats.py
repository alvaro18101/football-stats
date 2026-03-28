import pandas as pd

# id = int(input('Enter the club id: '))
id = 1

ids_df = pd.read_excel('general_data/ids.xlsx')

if id<1 or id>len(ids_df):
    print("id doesn't exist")
else:
    team_name = ids_df['name'][id-1]
    print(f'\t---{team_name}---')

df = pd.read_excel(f'scraped_data/raw_{team_name}.xlsx')

print(f'General stats of {team_name}')
print(f'Number of matches: {len(df)}')
print(f'Competitions: {[i for i in df['competition'].unique()]}')
print('')

def average_stats(df, column):
    print(f'Stat: {column} ({len(df)} matches)')
    print(f'Total: {df[column].sum()}')
    print(f'Average: {round(df[column].sum()/len(df), 3)}')
    print()

from filtering_functions import *

print("---UEFA---")
df_filtered = filter_by_competition(competition_name="UEFA")
average_stats(df_filtered, 'gf')
average_stats(df_filtered, 'ga')
average_stats(df_filtered, 'corner')

print("---LaLiga in home---")
df_filtered_2 = filter_by_competition("LaLiga")
df_filtered_2 = filter_by_local(True, df_filtered_2)
average_stats(df_filtered_2, 'gf')
average_stats(df_filtered_2, 'ga')
average_stats(df_filtered_2, 'corner')

# Print only some stats
print(print_df(df[df['rival_name'] == 'Sevilla']))