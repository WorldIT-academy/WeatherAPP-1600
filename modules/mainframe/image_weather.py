import customtkinter as ctk
from ..read_json import read_json
import os
import PIL.Image
# from PIL.Image import open

class ImageWeather(ctk.CTkLabel):
    def __init__(self, chlid_master: object, name_json: str, count: int = 0 , size: tuple = [int, int], **kwargs):
        self.COUNT = count
        self.NAME_JSON = name_json
        self.SIZE = size
        ctk.CTkLabel.__init__(
            self,
            master= chlid_master,
            text = '',
            fg_color= '#5DA7B1',
            image= self.load_image(),
            **kwargs
        )
    def load_image(self):
        data = read_json(name_json= self.NAME_JSON)
        if 'current' in self.NAME_JSON:
            image = data['weather'][0]['icon']
        elif 'hourly' in self.NAME_JSON:
            image = data['list'][self.COUNT]['weather'][0]['icon']
        path = os.path.abspath(__file__ + f'/../../../media/images/{image}.png')
        weather_image = PIL.Image.open(fp= path)

        return ctk.CTkImage(light_image= weather_image, size= self.SIZE)