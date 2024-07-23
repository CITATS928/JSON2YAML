import yaml
import json

#original
with open('emojis.json','r') as file:
    configuration = json.load(file)

with open('emojis.yaml','w') as yaml_file:
    yaml.dump(configuration, yaml_file)

#enhance
import os
def json_to_yaml(json_file,yaml_file):
    with open(json_file,'r') as jfile:
        data = json.load(jfile)
    with open(yaml_file,'w') as yfiile:
        yaml.dump(data,yfiile)

def convert_all_j2y(directory):
    for filename in os.listdir(directory):
        if filename.endwith('.json'):
            json_file = os.path.join(directory,filename)
            yaml_file = os.path.splitext(json_file)[0]+ '.yaml'
            json_to_yaml(json_file,yaml_file)
            print(f"Converted {json_file} to {yaml_file}")

if __name__=="__main__":
    directory="."
    convert_all_j2y(directory)