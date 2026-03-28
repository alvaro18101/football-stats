import pandas as pd
from pathlib import Path

team_name = "Barcelona"
data_path = Path("scraped_data")

df_barca = pd.read_excel(data_path / f"raw_{team_name}.xlsx")

stats_cols = [
    'goals_info','shots','shots_on_goal','possession','passing',
    'passing_accuracy','fouls','yellow_cards','red_cards','offside','corner'
]

rival_dfs = []

for rival in df_barca['rival_name'].unique():

    file_path = data_path / f"raw_{rival}.xlsx"

    if not file_path.exists():
        continue

    df_rival = pd.read_excel(file_path)

    # partidos contra Barcelona
    df_rival = df_rival[df_rival['rival_name'] == team_name]

    df_rival = df_rival[['date'] + stats_cols]

    # renombrar columnas
    df_rival = df_rival.rename(
        columns={col: f"{col}_against" for col in stats_cols}
    )

    rival_dfs.append(df_rival)

# unir todos los rivales
df_rivals_all = pd.concat(rival_dfs, ignore_index=True)

# merge final
df_final = df_barca.merge(
    df_rivals_all,
    on="date",
    how="left"
)

df_final.to_excel("barcelona_matches_complete.xlsx", index=False)