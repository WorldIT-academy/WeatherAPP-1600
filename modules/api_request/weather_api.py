import requests
import json
from ..json_functions.read_json import read_json
from ..json_functions.write_json import write_json

api_dict = read_json(name_json = "config_api.json")

API_KEY = api_dict["api_key"]
CITY_NAME = api_dict["city_name"]

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data_list = json.loads(response.content)
    write_json(name_file = "config_weather.json", value_file = data_list)
    print(json.dumps(data_list, indent = 4))