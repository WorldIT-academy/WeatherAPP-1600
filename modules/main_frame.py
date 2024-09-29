import customtkinter
from .read_json import read_json

dict = read_json(name_json= 'config.json')

width = dict['main_frame']['width']
height = dict['main_frame']['height']  
title = dict['main_frame']['title']

app = customtkinter.CTk()
app.geometry(f"{width}x{height}")
app.title(title)

