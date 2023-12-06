import json

with open('package.json', 'r+') as f:
    data = json.load(f)
    data['scripts']['build'] = 'npm install && npm test'
    print(data['scripts'])
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
    