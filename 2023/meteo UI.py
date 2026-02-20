from tkinter import *
import meteo_api_1000
from time import sleep
from PIL import ImageTk, Image


weather_info = meteo_api_1000.weather()

measureHour = weather_info['Dernière mesure']
temperature = weather_info['Température']
temps = weather_info['Temps']
humidity = weather_info['Humidité']
rain = weather_info['Précipitation']
wind = weather_info['Vents']
pressure = weather_info['Pression atmos.']
networkState = weather_info['Online']
moment = weather_info['Moment']

###################################################################################################
# moment = 'day'
if moment == 'day':
    bg_color = '#9caddc'#272822
    title_color = '#4d4d4d'
    label_color = '#202020'
else:
    bg_color = '#272822'
    title_color = 'gray'
    label_color = '#dfdfdf'

# config
win = Tk()
win.title('Météo')
win.iconbitmap(r"C:\Users\HP\Documents\Files\scripts\Test ressources\ico_bitmap\meteo.ico")
win.state('zoomed')
win.minsize(700, 600)
win.config(background=bg_color)

# Frames principales
upper_main_frame = Frame(win, bg=bg_color)
middle_main_frame = Frame(win, bg=bg_color)
lower_main_frame = Frame(win, bg=bg_color)

################# TOP FRAME #######################################################################
fontUpper = ("Roboto", 20)

networkState_label = Label(upper_main_frame, text='Connectez-vous pour mettre à jour les données météorologiques', font=fontUpper, bg=bg_color, fg=title_color, state='disabled')

if networkState == False:
    networkState_label.pack(expand=True, side='top')

cityName_label = Label(upper_main_frame, text='Bamako, ML (12.65, -8)', font=fontUpper, bg=bg_color, fg=title_color)
cityName_label.pack(expand=True, side='left', padx=90, pady=10)

measureHour_label = Label(upper_main_frame, text='Dernière mesure : ' + measureHour, font=fontUpper, bg=bg_color, fg=title_color)
measureHour_label.pack(expand=True, side='right', padx=90, pady=10)

################# MIDDLE FRAME ####################################################################
canvas = Canvas(middle_main_frame, width=1366, height=400)
canvas.pack()

background = ImageTk.PhotoImage(Image.open(fr"C:\Users\HP\Documents\Files\scripts\Test ressources\meteo\{moment}.png"))
canvas.create_image(0, 0, image=background, anchor='nw')

icon_code = weather_info['Illustration']
icon_path = fr"C:\Users\HP\Documents\Files\scripts\Test ressources\meteo\icons\premium\{icon_code}.png"
print("Icon path: ", icon_path)
image = ImageTk.PhotoImage(Image.open(icon_path))
canvas.create_image(500, 200, image= image)

canvas.create_text(850, 150, text=temperature, font=("Roboto", 80, 'bold'), fill=label_color)
canvas.create_text(850, 250, text=temps, font=("Roboto", 50), fill=label_color)

################# BOTTOM FRAME ####################################################################
humidity_frame = Frame(lower_main_frame, bg=bg_color)
rain_frame = Frame(lower_main_frame, bg=bg_color)
wind_frame = Frame(lower_main_frame, bg=bg_color)
pressure_frame = Frame(lower_main_frame, bg=bg_color)

    
humidity_label_title = Label(humidity_frame, text='Humidité', font=("Roboto", 25), bg=bg_color, fg=title_color)
humidity_label_title.pack(side='top')
humidity_label_value = Label(humidity_frame, text=humidity, font=("Roboto", 25), bg=bg_color, fg=label_color)
humidity_label_value.pack(side='bottom')

rain_label_title = Label(rain_frame, text='Précipitation', font=("Roboto", 25), bg=bg_color, fg=title_color)
rain_label_title.pack(side='top')
rain_label_value = Label(rain_frame, text=rain, font=("Roboto", 25), bg=bg_color, fg=label_color)
rain_label_value.pack(side='bottom')

wind_label_title = Label(wind_frame, text='Vents', font=("Roboto", 25), bg=bg_color, fg=title_color)
wind_label_title.pack(side='top')
wind_label_value = Label(wind_frame, text=wind, font=("Roboto", 25), bg=bg_color, fg=label_color)
wind_label_value.pack(side='bottom')

pressure_label_title = Label(pressure_frame, text='Pression atmos.', font=("Roboto", 25), bg=bg_color, fg=title_color)
pressure_label_title.pack(side='top')
pressure_label_value = Label(pressure_frame, text=pressure, font=("Roboto", 25), bg=bg_color, fg=label_color)
pressure_label_value.pack(side='bottom')


humidity_frame.grid(column=0, row=0, padx=60)
rain_frame.grid(column=1, row=0, padx=60)
wind_frame.grid(column=2, row=0, padx=60)
pressure_frame.grid(column=3, row=0, padx=60)

###################################################################################################

upper_main_frame.pack(expand=YES)
middle_main_frame.pack(expand=YES)
lower_main_frame.pack(expand=YES)
win.mainloop()

