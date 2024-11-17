import customtkinter as ctk
from ..read_json import read_json
from .image_weather import ImageWeather
from .horizontal_scroll import horizontal_scroll

data = read_json(name_json= 'hourly_weather.json')

class HourlyData(ctk.CTkFrame):
    def __init__(self, child_master: object, count: int= 0, **kwargs):
        ctk.CTkFrame.__init__(
           self, 
           master = child_master,
           fg_color= '#5DA7B1',
           **kwargs
        )
        self.COUNT = count
        self.grid(row= 0, column= self.COUNT)
        if self.COUNT == 0:
            self.TIME = ctk.CTkLabel(
                master = self,
                text = 'Зараз',
                font = ('Arial', 32, 'bold')
            )
        else:
            self.TIME = ctk.CTkLabel(
                master = self,
                text = data["list"][self.COUNT]["dt_txt"][11:16],
                font = ('Arial', 32, 'bold')
            )
        self.TIME.grid(row= 0, column= 0, padx = 10)
        #
        self.IMAGE = ImageWeather(
            chlid_master= self,
            name_json = 'hourly_weather.json',
            count = self.COUNT,
            size = (70, 70)
        )

        self.IMAGE.grid(row= 1, column = 0, pady = 10, padx = 10)
        #
        self.TEMP = ctk.CTkLabel(
            master= self,
            text= f'{int(data["list"][self.COUNT]["main"]["temp"])}°',
            font = ('Arial', 32, 'bold')
        )
        self.TEMP.grid(row= 3, column = 0, pady = 10, padx = 10)
        print(data["list"][self.COUNT]["main"]["temp"])
        
for el in range(len(data["list"])):
    data_hourly = HourlyData(child_master= horizontal_scroll, count= el)