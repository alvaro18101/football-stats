## Libraries installed:
- Matplotlib
- Pandas
- Selenium
- webdriver-manager
- beautifulsoup4
- openpyxl

## Correct order of codes:
1. `scraping.py`: Funcion that scraps the web info of stats footbal teams using a link, the code returns lists called team_1_name, data_team_1, team_2_name and data_team_2. **(No run)**

2. `save_data.py`: **Run first**. In the links/ folder, there are `.txt` files with the names of soccer teams, each containing links to the statistics displayed on Google for their matches. This script searches for the `.txt` file with the team name specified in the `current_team_name` variable and iterates through each link, applying the `scraping.py` function each time. The data obtained from each link is saved in an `.xlsx` file (or `.csv`, depending on the `format_file` variable) in the raw_data/ folder (if the file doesn't exist, it is created). For each link, data must be added to two `.xlsx` (or `.csv`) files: one for the home team and one for the away team (or these files must be created). The data for each match is added as a new row, and the columns contain the respective statistics. The columns are: match number, date, competition, rival name, local, goals for, goals against, goal information, shots, shots on goal, possession, passing, passing_accuracy, fouls, yellow_cards, red_cards, offside, corner. Only one team's statistics are saved in its file; the opponent's statistics are saved in their own file.

2. `save_data2.py`: Here, the statistics of the chosen team and the opponent they faced are saved in a single file (named according to `current_team_name`).

3. `save_general_data.py`: This code save two `.xlsx` files inside the `general_data/` folder: `general_df.xlsx` which contains general data for all football teams and `ids.xlsx` which generates an id for each football team.

4. `data_processing.py`: This code reads `.xlsx` files and processes their data using Pandas and saves them in the processed_data/ folder.

5. `stats.py`: Show the team stats for a team.

6. `filtering_functions`: This code reads `.xlsx` files and filters their data according to given criteria using Pandas.

## Formats
## Format of .txt files
All links must lead to the statistics that Google displays at the end of each match, for example: https://www.google.com/search?q=barcelona+vs&oq=barce&gs_lcrp=EgZjaHJvbWUqEwgAEEUYJxg7GEYY_QEYgAQYigUyEwgAEEUYJxg7GEYY_QEYgAQYigUyBggBEEUYOTIOCAIQRRgnGDsYgAQYigUyBggDEEUYOzIKCAQQLhixAxiABDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPNIBBzg3NmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8#sie=m;/g/11yfnc0n2f; 2;/m/09gqx;dt;fp;1;;;;-1&wptab=si:AL3DRZGGPnnVaiK67YqdUfewzBcS-upM6Qijh dUU6Jr8AWsjr8v9CvA-SnNnnxtCTH-Iycrz5Hfiy-o4IHk920D1F5HguzudSJBINLsQJs59 tzpsV_DoE3teFj2StyQBu6wTFVQRHxAkZnNilYk5UX14zeC2J8cvyMEij66lv5a54Lb3tXT NH6EwDjyO9HmSby9uktlmw334vuaRUSjGAk8JkgNu1ms_j6cVIbsxZLNpcq6GWPT4U0U%3D

He The file contains all the links from which you want to obtain information. These links must be separated by two line breaks, for example:

```
link 1

link 2

link 3
```

## Format of `.xlsx` (or `.csv`) files in processed_data/ folder
The columns are:
- match_number: **(integer)** number of match 
- date: **(string)** date of match
- competition: **(string)** name of competition (Champions League, LaLiga, etc.)
- rival_name: **(string)** name of rival
- local: **(boolean)** `True` if the team plays at home, else `False`
- gf: **(integer)** goals for
- ga: **(integer)** goals against
- goals_info: **(string)** Information of the match goals with the format: [[Player, minute], [Player, minute], ...], e.g., [['Raphinha', "7'"], ['Ferran Torres', "23'"], ['Lamine Yamal', "90+4'"]]
- shots: **(integer)** number of shots
- shots_on_goal: **(integer)** number of shots on goal
- possession: **(float)** ball possession percentage (0 - 1), e.g., 0.71
- passing: **(integer)** number of passes in the match
- passing_accuracy: **(float)** pass accuracy (percentage), e.g., 0.93
- fouls: **(integer)** number of fouls
- yellow_cards: **(integer)** number of yellow cards
- red_cards: **(integer)** number of red cards
- offside: **(integer)** number of offsides
- corner: **(integer)** number of corners

Note: The statistics correspond to this team; the opponent's cards, offsides, corners, etc. are in their file.

## Features:
Code a neural network who clasifies the types of games for each team based in theis stats.
Pd: La idea es hacer una red neuronal que clasifique los tipos de juegos de cada equipo según sus stats.