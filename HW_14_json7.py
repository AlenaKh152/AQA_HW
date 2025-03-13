import json

# start_data = {'Real':['Spain','100'], 'Juventus':['Italy','95'],
# 'Bavaria':['Germany','91'],'Manchester':['UK','103']}

# with open('C:/Users/Admin/Documents/AQA_HW/data_json.json', 'w') as fp:
#    json.dump(start_data, fp)

with open('C:/Users/Admin/Documents/AQA_HW/data_json.json', 'r',  encoding="utf-8") as file:
    start_data = json.load(file)

max_count = 0
team = ''

for key in start_data.keys():
    if int(start_data[key][1]) >= max_count:
        max_count = int(start_data[key][1])
        team = key
print(f'The {team} club from {start_data[team][0]} has most wins: {start_data[team][1]}.')
