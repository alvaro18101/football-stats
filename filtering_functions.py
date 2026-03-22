import pandas as pd
name = 'barcelona'
df = pd.read_excel(f'processed_data/{name}.xlsx')
# df = pd.read_csv(f'processed_data/{name}.csv')

# def filter_by_competition(competition_name:str):
#     competition_name = competition_name.strip().lower()
#     df['is_competition'] =  df.competition.apply(lambda x: competition_name in x.strip().lower())

print_df = lambda df: df[['rival_name', 'local', 'gf',
       'ga', 'shots', 'fouls', 'yellow_cards', 'red_cards', 'offside', 'corner']]

def filter_by_competition(competition_name:str, df=df,save=False, format='xlsx'):
    competition_name = competition_name.strip().lower()
    df_filtered = df.copy()
    df_filtered['is_competition'] =  df.competition.str.contains(competition_name, case=False, na=False)
    df_filtered = df_filtered[df_filtered['is_competition'] == True].drop(columns=['is_competition'])
    if save:
        if format == 'xlsx':
            df_filtered.to_excel(f'processed_data/{name}_filtered.xlsx', index=False)
            print(f'---Data saved as {name}_filtered.xlsx---')
        if format == 'csv':
            df_filtered.to_csv(f'processed_data/{name}_filtered.csv', index=False)
            print(f'---Data saved as {name}_filtered.csv---')
    return print_df(df_filtered)

def filter_by_local(local_name:bool, df=df, save=False, format='xlsx'):
    df_filtered = df[df['local'] == True]
    if save:
        if format == 'xlsx':
            df_filtered.to_excel(f'processed_data/{name}_filtered.xlsx', index=False)
            print(f'---Data saved as {name}_filtered.xlsx---')
        if format == 'csv':
            df_filtered.to_csv(f'processed_data/{name}_filtered.csv', index=False)
            print(f'---Data saved as {name}_filtered.csv---')
    return df_filtered

def search_rival(rival_name: str, df=df):
    pass

if __name__ == '__main__':
    print(filter_by_competition(competition_name="Campeones", save=True))