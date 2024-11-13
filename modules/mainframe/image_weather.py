import customtkinter as ctk
from ..read_json import read_json


class ImageWeather(ctk.CTkLabel):
    def __init__(self, chlid_master: object, name_json: str,**kwargs):
        self.NAME_JSON = name_json
        ctk.CTkLabel.__init__(
            self,
            master= chlid_master,
            **kwargs
        )
    
    def load_image(self):
        data = read_json(name_json= self.NAME_JSON)
        



