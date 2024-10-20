import customtkinter as ctk
from ..json_functions.read_json import read_json

dict = read_json(name_json= 'config.json')

WIDTH = dict['main_frame']['width']
HEIGHT = dict['main_frame']['height']  
TITLE = dict['main_frame']['title']


app = ctk.CTk(fg_color = 'white')
app.geometry(f"{WIDTH}x{HEIGHT}")
app.title(TITLE)

# label1 = ctk.CTkLabel(app, text = "label1", font=('Roboto', 50))
# label1.grid(row = 0, column=0, padx = 20, pady = 40)
# label2 = ctk.CTkLabel(app, text = "label2", font=('Roboto', 50))
# label2.grid(row = 0, column=1)    (∪.∪ )...zzz
# label3 = ctk.CTkLabel(app, text = "label3", font=('Roboto', 50))
# label3.grid(row = 1, column=0)(=ↀωↀ=)
# label4 = ctk.CTkLabel(app, text = "label4", font=('Roboto', 50))
# label4.grid(row = 1, column=1) 0_0

# label1 = ctk.CTkLabel(app, text = "label 1")
# label1.place(x = 0, y = 0) -_-
# label2 = ctk.CTkLabel(app, text = "label 2")
# label2.place(x = 0, y = 125)
# button3 = ctk.CTkButton(app, text = "button 3")
# button3.place(x = 125, y = 0)
# button4 = ctk.CTkButton(app, text = "button 4")
# button4.place(x = 125, y = 125)LOL

# frame = ctk.CTkScrollableFrame(app, width = 200 , height = height, fg_color= "green")
# frame.pack(side="left")
# button_list = []

# for number in range(1, 21):
#     button = ctk.CTkButton(frame , text= f"button{number}")
#     button.pack(padx = 20 , pady = 20)
#     button_list.append(button)

