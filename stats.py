import pandas as pd

# id = int(input('Enter the club id: '))
id = 1

ids_df = pd.read_excel('general_data/ids.xlsx')

if id<1 or id>len(ids_df):
    print("id doesn't exist")
else:
    team_name = ids_df['name'][id-1]
    print(f'\t---{team_name}---')

df = pd.read_excel(f'raw_data/raw_{team_name}.xlsx')

print(f'General stats of {team_name}')
print(f'Number of matches: {len(df)}')
print(f'Competitions: {[i for i in df['competition'].unique()]}')
print('')

