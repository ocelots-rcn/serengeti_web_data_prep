import json
data = {'variables': ['Amount of Shade','Distance to Confluence  m ', 'Distance to Kopje  m ', 'Distance to River  m ', 'Lion Risk  Dry ', 'Lion Risk  Wet ', 'SeasonalGreenness', 'Tree Density Measure', 'Longitude  m ', 'Latitude  m '], 'species': {}, 'groups': {'predator': [], 'prey': [], 'other': []}}

f = open('Serengeti-data-20220713.csv', 'r')
header = f.readline()[:-1].replace('.', ' ').split(',')

while True:
    line = f.readline()
    if not line:
        break
    # remove new line
    line = line[:-1]
    parts = line.split(',')
    key = parts[header.index('Species')]
    if key not in data['species']:
        data['species'][key] = {}
        for var in data['variables']:
            data['species'][key][var] = []
        data['groups'][parts[header.index('Predator')]].append(key)

    for var in data['variables']:
        data['species'][key][var].append(float(parts[header.index(var)]))

f.close()
f = open('cont_var.json', 'w')
json.dump(data, f)
f.close()
