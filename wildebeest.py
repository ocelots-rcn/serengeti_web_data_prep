import json
data = {'variables': ['Amount of Shade', 'Distance to Confluence  m ', 'Distance to Kopje  m ', 'Distance to River  m ', 'SeasonalGreenness'], 'wildebeest': {}}

f = open('Serengeti-data-20220713.csv', 'r')
header = f.readline()[:-1].replace('.', ' ').split(',')

for var in data['variables']:
    data['wildebeest'][var] = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [], '12': []}

while True:
    line = f.readline()
    if not line:
        break
    # remove new line
    line = line[:-1]
    parts = line.split(',')
    key = parts[header.index('Species')]
    if key == 'wildebeest':
        month = parts[header.index('Month  1 Jan  ')]
        for var in data['variables']:
            data['wildebeest'][var][month].append(float(parts[header.index(var)]))

f.close()
f = open('wildebeest.json', 'w')
json.dump(data, f)
f.close()
