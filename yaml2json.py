import yaml
import json

with open('xmas.yaml','r') as file:
    data = yaml.safe_load(file)

with open('xmas.json','w') as jsonfile:
    json.dump(data,jsonfile)


#enhence
import os

def yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r') as yfile:
        data = yaml.safe_load(yfile)
    with open(json_file, 'w') as jfile:
        json.dump(data, jfile)

def convert_all_yaml_to_json(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            yaml_file = os.path.join(directory, filename)
            json_file = os.path.splitext(yaml_file)[0] + '.json'
            yaml_to_json(yaml_file, json_file)
            print(f"Converted {yaml_file} to {json_file}")

if __name__ == "__main__":
    directory = "."
    convert_all_yaml_to_json(directory)