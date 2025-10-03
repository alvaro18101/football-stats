from scraping import *
import pandas as pd

def save_data(url):
    columns = ['match_number', 'date', 'competition', 'rival_name', 'local', 'gf', 'ga', 'info_goals', 'shots', 'shots_on_goal', 'possession', 'passing', 'passing_accuracy', 'fouls', 'yellow_cards', 'red_cards', 'offside', 'corner']

    team_1_name, data_team_1, team_2_name, data_team_2 = scrape_match(url)

    try:
        df1 = pd.read_excel(f'raw_data/raw_{team_1_name}.xlsx')
        data_team_1[0] = list(df1['match_number'])[-1] + 1
    except:
        df1 = pd.DataFrame(columns=columns)
    
    try:
        df2 = pd.read_excel(f'raw_data/raw_{team_2_name}.xlsx')
        data_team_2[0] = list(df2['match_number'])[-1] + 1
    except:
        df2 = pd.DataFrame(columns=columns)

    if data_team_1[1] not in list(df1['date']):
        df1.loc[-1] = data_team_1
        df2.loc[-1] = data_team_2

    df1.to_excel(f'raw_data/raw_{team_1_name}.xlsx', index=False)
    df2.to_excel(f'raw_data/raw_{team_2_name}.xlsx', index=False)
    print('---Saved data---')

with open('links/barcelona.txt', 'r') as text_file:
    j = 1
    for i in text_file.readlines():
        if i != '\n':
            print(j)
            j+= 1
            save_data(i)