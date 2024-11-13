import customtkinter as ctk
import requests
from .main_frame import app
from ..read_json import read_json
import json
from ..write_json import create_json


class HorizontalScroll(ctk.CTkScrollableFrame):
    def __init__(self, child_master: object, child_width: int, child_height: int ,**kwargs):
        ctk.CTkScrollableFrame.__init__(
            self,
            master = child_master,
            width= child_width,
            height = child_height,
            border_width= 5,
            border_color = "#ffffff",
            orientation = "horizontal",
            fg_color = "#5da7b1",
            corner_radius = 20,
            **kwargs
        )
        self.place(x = 325, y = 420)

    def get_forecast(self):
        dict = read_json(name_json = "config_forecast.json")
        CITY_NAME = "Dnipro"
        API_KEY = dict["api_key"]
        URL = dict["api_forecast"].format(CITY_NAME, API_KEY)
        # URL = "api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric&lang=uk".format(CITY_NAME, API_KEY)#
        try:
            response = requests.get(URL)
            data = response.json()
            create_json(name_json = 'hourly_weather.json', data_dict = data)
            
        except requests.exceptions.RequestException as exeption:
            print(f"An error occurred: {exeption}")
             
        



horizontal_scroll = HorizontalScroll(child_master= app, child_width = 820, child_height= 240)
horizontal_scroll.get_forecast()