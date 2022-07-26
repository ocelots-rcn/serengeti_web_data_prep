import json
import time
data = {'species': {}, 'groups': {'predator': [], 'prey': [], 'other': []}}

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
        data['species'][key] = []
        data['groups'][parts[header.index('Predator')]].append(key)

    try:
        # ctime = time.strftime('%T', time.strptime(parts[3], '%I:%M:%S %p'))
        ctime = time.strptime(parts[header.index('Time  24 hour ')], '%I:%M:%S %p').tm_hour
        data['species'][key].append(ctime)
    except ValueError:
        pass

data['groups']['predator'].sort()
data['groups']['prey'].sort()
data['groups']['other'].sort()

f.close()
f = open('daily.json', 'w')
json.dump(data, f)
f.close()
