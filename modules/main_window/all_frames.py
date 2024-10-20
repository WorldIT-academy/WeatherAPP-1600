from ..json_functions.read_json import read_json
from  .main_frame import app , WIDTH, HEIGHT
import customtkinter as ctk 

data_weather = read_json(name_json = "config_weather.json")
current_city = data_weather["name"]
current_temp = round(data_weather["main"]["temp"])

scrolling_frame = ctk.CTkScrollableFrame(
    app,
    height = HEIGHT,
    width = 275,
    fg_color = "#096C82"
)
scrolling_frame.pack(side = "left")

city_frame = ctk.CTkFrame(
    scrolling_frame,
    height = 100,
    width = 236,
    fg_color = "#4599A4",
    corner_radius = 15,
    border_color = "white",
    border_width = 2

)
city_frame.pack(pady = (30, 35))

label_current_possition = ctk.CTkLabel(
    city_frame,
    text= "Поточна позиція", 
    font = ("Roboto Slab", 16, "bold")
)
# label_current_possition.grid(row = 0, column = 0)
label_current_possition.place(x = 14, y = 8)
label_current_temp = ctk.CTkLabel(
    master = city_frame,
    text = f"{current_temp}°",
    font = ("Roboto Slab", 50, "bold")
)
label_current_temp.place(x = 165, y = 12)