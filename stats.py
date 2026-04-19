from statsbombpy import sb
competitions = sb.competitions()
import pandas as pd




matches = sb.matches(competition_id= 55, season_id=282)
print(matches.shape)
matches.head()
print(matches.columns.tolist())

spain_matches = matches[(matches['home_team'] == 'Spain') | (matches['away_team'] == 'Spain')]
print(spain_matches[['match_id', 'match_date', 'home_team', 'away_team', 'home_score', 'away_score', 'competition_stage']])

game1 = sb.events(match_id= 3930160)
print(game1["type"].value_counts())

lineup= game1[ (game1['type'] == 'Starting XI')]
print (lineup)
print(lineup.columns.tolist())

print(lineup['tactics'].iloc[0])
players_list = lineup['tactics'].iloc[0]['lineup']

spain_lineup = []

for p in players_list:
    spain_lineup.append({
    "player": p['player']['name'],
    "position": p['position']["name"],
    "jersey_number": p['jersey_number']
    })

print(spain_lineup)

print(pd.DataFrame(spain_lineup))



