import json
import os

script_dir = os.path.dirname(__file__)
print("Le script est dans:" + script_dir)
script_absolute_path = os.path.join(script_dir, 'Files/exemple.json')

json = json.loads(open(script_absolute_path).read())
value = json['name']
print(value)

for key in json:
	value = json[key]
	print(f"{value} = {key}")
