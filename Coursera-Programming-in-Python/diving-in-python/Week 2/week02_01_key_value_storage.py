"""
Week 2 Programming Assignment: Key-value storage
"""

import os
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str)
parser.add_argument("--value", type=str)
args = parser.parse_args()
key = args.key
value = args.value
data = dict()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if value == None:
    try:
        result = []
        with open(storage_path, 'r') as f:
            json_data = json.load(f)
            if key in json_data.keys():
                print(json_data[key])
            else:
                print("")
    except FileNotFoundError:
        print("")
else:
    try:
        with open(storage_path, 'r') as f:
            json_data = json.load(f)
            if key in json_data.keys():
                json_data[key] = json_data[key] + ', ' + value
            else:
                json_data[key] = value
        with open(storage_path, 'w') as f:
            json.dump(json_data, f, indent=4)
    except FileNotFoundError:
        data[key] = value
        with open(storage_path, 'w') as f:
            json.dump(data, f, indent=4)
    
    


