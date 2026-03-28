import pandas as pd

current_name = 'Barcelona'

df = pd.read_excel(f'processed_data/{current_name.lower()}.xlsx')

matches_number = len(df)
gf = df['gf'].sum()
ga = df['ga'].sum()
yellow_cards = df['yellow_cards'].sum()
yellow_cards_against = df['yellow_cards_against'].sum()
red_cards = df['red_cards'].sum()
red_cards_against = df['red_cards_against'].sum()
corner = df['corner'].sum()
corner_against = df['corner_against'].sum()


# print(f'Number of matches: {matches_number}')
# print('\n\tGoals')
# print(f'Number of goals for: {gf} ({round(gf/matches_number, 3)})')
# print(f'Number of goals against: {ga} ({round(ga/matches_number, 3)})')
# # ---> Filter for type of championship <---

# print('\n\tCards')
# print(f'Number of yellow cards: {yellow_cards} ({round(yellow_cards/matches_number, 3)})')
# print(f'Number of yellow cards against: {yellow_cards_against} ({round(yellow_cards_against/matches_number, 3)})')
# print(f'Number of yellow cards total: {yellow_cards + yellow_cards_against} ({round((yellow_cards + yellow_cards_against)/matches_number, 3)})')

# print(f'Number of red cards: {red_cards} ({round(red_cards/matches_number, 3)})')
# print(f'Number of red cards against: {red_cards_against} ({round(red_cards_against/matches_number, 3)})')
# print(f'Number of red cards total: {red_cards + red_cards_against} ({round((red_cards + red_cards_against)/matches_number, 3)})')


# print('\n\tCorners')
# print(f'Number of corners: {corner} ({round(corner/matches_number, 3)})')
# print(f'Number of corners against: {corner_against} ({round(corner_against/matches_number, 3)})')
# print(f'Number of corners total: {corner + corner_against} ({round((corner + corner_against)/matches_number, 3)})')


a = df['goals_info'][26]
a = a[1:-1]

a = a.replace('"', '')
a = a.replace('\'', '')
print(a)
b = []

for i in range(a.count('[')):
    c = a.index('[')
    d = a.index(']')
    # Fix goals_info in data_processing2.py
    e = a[c+1:d].split(',')
    b.append(e)
    print(a[c:d+1])
    a = a.replace(a[c:d+1], '', 1)

print(b)