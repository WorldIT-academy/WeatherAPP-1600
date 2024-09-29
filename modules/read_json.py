import json
import os

def read_json(name_json : str):
    path_file = os.path.abspath(__file__ + f'../../../static/{name_json}')
    with open(path_file, "r") as file:
        return json.load(file)