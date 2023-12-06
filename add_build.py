import json

with open('package_Copy.json', 'r+') as f:
    data = json.load(f)
    data['scripts']['build'] = 'webpack --config webpack.config.js'
    print(data['scripts'])
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
    