import customtkinter as ctk
from .main_frame import app
from ..read_json import read_json
from ..write_json import create_json
import requests

class VerticalScroll(ctk.CTkScrollableFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self, 
            master= child_master,
            width= 275,
            height= 800,
            fg_color= "#096c82",
            **kwargs
        )
        self.grid(row= 0, column= 0)
        self.request_api()

    def request_api(self):
        
        dict = read_json(name_json = "config_current_weather.json")
        CITY_NAME = "Dnipro"
        API_KEY = dict["api_key"]
        URL = dict["api_current"].format(CITY_NAME, API_KEY)

        try:
            response = requests.get(URL)
            data = response.json()
            create_json(name_json = 'current_weather.json', data_dict = data)
            
        except requests.exceptions.RequestException as exeption:
            print(f"An error occurred: {exeption}")

v_scroll = VerticalScroll(child_master= app)