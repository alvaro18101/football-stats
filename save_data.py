from scraping import *
import pandas as pd

def save_data(url):
    columns = ['match_number', 'date', 'competition', 'rival_name', 'local', 'gf', 'ga', 'goals_info', 'shots', 'shots_on_goal', 'possession', 'passing', 'passing_accuracy', 'fouls', 'yellow_cards', 'red_cards', 'offside', 'corner']

    output_folder = 'world_cup_scraped_data'

    team_name_1, data_team_1, team_name_2, data_team_2 = scrape_match(url)
    try:
        df1 = pd.read_excel(f'{output_folder}/raw_{team_name_1}.xlsx')
        data_team_1[0] = list(df1['match_number'])[-1] + 1
    except:
        df1 = pd.DataFrame(columns=columns)
    
    try:
        df2 = pd.read_excel(f'{output_folder}/raw_{team_name_2}.xlsx')
        data_team_2[0] = list(df2['match_number'])[-1] + 1
    except:
        df2 = pd.DataFrame(columns=columns)
    if data_team_1[1] not in list(df1['date']):
        df1.loc[-1] = data_team_1
        df2.loc[-1] = data_team_2

    df1.to_excel(f'{output_folder}/raw_{team_name_1}.xlsx', index=False)
    df2.to_excel(f'{output_folder}/raw_{team_name_2}.xlsx', index=False)
    print('---Saved data---\n')

input_folder = 'links/world_cup'
current_team_name = 'Estados Unidos'

with open(f'{input_folder}/{current_team_name}.txt', 'r') as text_file:
    j = 1
    for i in text_file.readlines():
        if i != '\n':
            print(j, end='. ')
            j+= 1
            save_data(i)