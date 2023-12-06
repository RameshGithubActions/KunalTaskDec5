import json

with open('package.json', 'r+') as f:
    data = json.load(f)
    data['scripts']['build'] = "echo 'Build not configured'"
    data['scripts']['test'] = "echo 'Test not configured'"
    print(data['scripts'])
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
    