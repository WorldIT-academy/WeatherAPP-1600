import customtkinter as ctk
from ..read_json import read_json

dict = read_json(name_json= 'config.json')

width = dict['main_frame']['width']
height = dict['main_frame']['height']  
title = dict['main_frame']['title']

app = ctk.CTk(fg_color = '#5da7b1')
app.geometry(f"{width}x{height}")
app.title(title)



frame = ctk.CTkScrollableFrame(app, width = 275 , height = height, fg_color= "#096C82")
frame.pack(anchor = 'w')
button_list = []
for number in range(1, 21):
    button = ctk.CTkButton(frame , text= f"button{number}")
    button.pack(padx = 20 , pady = 20)
    button_list.append(button)

