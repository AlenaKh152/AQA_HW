import json

with open('data_json.json', 'r',  encoding="utf-8") as file:
    start_data = json.load(file)


def winner_team():
    max_count = 0
    team = ''
    for key in start_data.keys():
        if int(start_data[key][1]) >= max_count:
            max_count = int(start_data[key][1])
            team = key
    return f'The {team} club from {start_data[team][0]} has most wins: {start_data[team][1]}.'


print(winner_team())
