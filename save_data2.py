from scraping import *
import pandas as pd

def save_data(url, current_team_name):
    columns = ['match_number', 'date', 'competition', 'rival_name', 'local', 'gf', 'ga', 'goals_info', 'shots', 'shots_on_goal', 'possession', 'passing', 'passing_accuracy', 'fouls', 'yellow_cards', 'red_cards', 'offside', 'corner', 'goals_info_against', 'shots_against', 'shots_on_goal_against', 'possession_against', 'passing_against', 'passing_accuracy_against', 'fouls_against', 'yellow_cards_against', 'red_cards_against', 'offside_against', 'corner_against']

    team_name_1, data_team_1, team_name_2, data_team_2 = scrape_match(url)
    try:
        df1 = pd.read_excel(f'scraped_data/raw_{team_name_1}.xlsx')
        data_team_1[0] = list(df1['match_number'])[-1] + 1
    except:
        df1 = pd.DataFrame(columns=columns)
    
    try:
        df2 = pd.read_excel(f'scraped_data/raw_{team_name_2}.xlsx')
        data_team_2[0] = list(df2['match_number'])[-1] + 1
    except:
        df2 = pd.DataFrame(columns=columns)
    if data_team_1[1] not in list(df1['date']):
        df1.loc[-1] = data_team_1
        df2.loc[-1] = data_team_2

    # df1.to_excel(f'scraped_data/raw_{team_name_1}.xlsx', index=False)
    # df2.to_excel(f'scraped_data/raw_{team_name_2}.xlsx', index=False)

    if df1['rival_name'] == current_team_name:
        df_local = 0
    print('---Saved data---\n')

current_team_name = 'barcelona'

with open(f'links/{current_team_name}.txt', 'r') as text_file:
    j = 1
    for i in text_file.readlines():
        if i != '\n':
            print(j, end='. ')
            j+= 1
            save_data(i, current_team_name)