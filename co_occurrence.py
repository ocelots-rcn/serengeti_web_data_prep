import json
import pyproj

data = {'species': {}, 'camera_sites': {}}
variables = ['Amount of Shade','Distance to Confluence  m ', 'Distance to Kopje  m ', 'Distance to River  m ', 'Lion Risk  Dry ', 'Lion Risk  Wet ', 'Tree Density Measure']

f = open('Serengeti-data-20220713.csv', 'r')
header = f.readline()[:-1].replace('.', ' ').split(',')

transformer = pyproj.Transformer.from_crs(21036, 4326)

while True:
    line = f.readline()
    if not line:
        break
    # remove new line
    line = line[:-1]
    parts = line.split(',')
    species = parts[header.index('Species')]
    camera = parts[header.index('Camera Site')]
    if camera not in data['camera_sites']:
        coor = transformer.transform(int(parts[header.index('Longitude  m ')]), int(parts[header.index('Latitude  m ')]))
        # Making asumption that site ids are unique and coordinates are accurate and the same throughout the data
        # data['camera_sites'][camera] = {'latitude': coor[1], 'longitude': coor[0]}
        data['camera_sites'][camera] = {'latitude': coor[0], 'longitude': coor[1]}
        for var in variables:
            data['camera_sites'][camera][var] = float(parts[header.index(var)])
        # all other variables are single values by camera site, SeasonalGreenness
        # needs to be computed on the fly based on date range
        data['camera_sites'][camera]['SeasonalGreenness'] = 0
    if species not in data['species']:
        data['species'][species] = {}
    if camera not in data['species'][species]:
        data['species'][species][camera] = []

    date = parts[header.index('Date')].split('/')
    payload = {'date': '20{}-{:02d}-{:02d}'.format(date[2], int(date[0]), int(date[1])), 'SeasonalGreenness': float(parts[header.index('SeasonalGreenness')])}
    data['species'][species][camera].append(payload)

f.close()
f = open('co_occurrence.json', 'w')
json.dump(data, f)
f.close()
