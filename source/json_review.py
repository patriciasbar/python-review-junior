import json
import pprint

input_filename = "resources/faves.json"
output_filename = "resources/out_faves.json"

def read_json(file=input_filename):
    with open(file, 'r') as f:
        data = json.load(f)  #python obj
        return data

def write_to_json(data, file=output_filename, indent=4):
    with open(file, 'w') as f:
        json.dump(data, f, indent=indent)

def collect_key_paths(obj, parent_key=''):
    paths = []

    if isinstance(obj, dict):
        for key, value in obj.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            paths.extend(collect_key_paths(value, full_key))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            full_key = f"{parent_key}[{i}]"
            paths.extend(collect_key_paths(item, full_key))
    else:
        paths.append((parent_key, obj))
    return paths


obj1 = read_json(file="resources/test_data.json")
pprint.pprint(collect_key_paths(obj1))








