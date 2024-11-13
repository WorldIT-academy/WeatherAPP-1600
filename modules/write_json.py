import json
import os

def create_json(name_json: str, data_dict: dict):
    path = os.path.abspath(__file__ + f"/../../static/{name_json}")
    with open(path, "w", encoding = "utf-8") as file:
        json.dump(obj = data_dict, fp = file, indent = 4, ensure_ascii= False)