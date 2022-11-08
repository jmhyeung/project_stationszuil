import textwrap
import tkinter as tk
from tkinter import scrolledtext
import requests

WEATHER_KEY = '115f419b9fbe1130e711816717d39573'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q='

HEIGHT = 800
WIDTH = 1000

light_blue = '#80c1ff'
white = '#F9F9F9'

root = tk.Tk()


def get_weather(city):
    url = f'{BASE_URL}{city}&appid={WEATHER_KEY}&units=metric'
    weather_json = requests.get(url).json()

    print(weather_json['main']['temp'])
    return weather_json['main']['temp']


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


# station_frame = tk.Frame(root, bg=light_blue, bd=10)
# station_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
#
# station_label = tk.Label(station_frame, text='Utrecht', font='Arial 30 bold', bg=light_blue, fg=white)
# station_label.place(relwidth=1, relheight=1)
#
# message_frame = tk.Frame(root, bg=light_blue, bd=10)
# message_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')
#
# message_label = tk.Label(message_frame, text='Dit is random tekst voor mijn message', bg=white)
# message_label.place(relwidth=1, relheight=1)
#
# lower_frame = tk.Frame(root, bg=light_blue, bd=10)
# lower_frame.place(relx=0.5, rely=0.775, relwidth=0.75, relheight=0.2, anchor='n')
#
# facility_frame = tk.Frame(lower_frame, bg=white, bd=10)
# facility_frame.place(relx=0.325, relwidth=0.65, relheight=1, anchor='n')
#
# facility_label = tk.Label(facility_frame, text=f'Beschikbare faciliteiten:\nToiletten park and v', font='Arial 12 bold',
#                           bg=white, bd=10, anchor='w')
# facility_label.place(relx=0.5, relwidth=1, relheight=1, anchor='n')
#
# weather_frame = tk.Frame(lower_frame, bg=white, bd=10)
# weather_frame.place(relx=0.8375, relwidth=0.325, relheight=1, anchor='n')
#
# weather_label = tk.Label(weather_frame, text=get_weather('Boston'), font='Arial 25 bold', bg=white, bd=10)
# weather_label.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

frame1 = tk.Frame(root, bg=light_blue, bd=10)
frame1.place(relx=0.4, rely=0.075, relwidth=0.7, relheight=0.15, anchor='n')
station1 = tk.Label(frame1, text='Utrecht', font='Arial 12 bold', bg=light_blue, bd=3, anchor='w')
station1.place(relwidth=0.3, relheight=0.3)

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sapien viverra.'
txt = '\n'.join(textwrap.wrap(lorem, 60))
message1 = tk.Label(frame1, text=txt, font='Arial 10 bold', bg=light_blue, bd=3, anchor='w')
message1.place(rely=0.35, relwidth=0.7, relheight=0.7)

frame2 = tk.Frame(root, bg=light_blue, bd=10)
frame2.place(relx=0.4, rely=0.25, relwidth=0.7, relheight=0.15, anchor='n')

frame3 = tk.Frame(root, bg=light_blue, bd=10)
frame3.place(relx=0.4, rely=0.425, relwidth=0.7, relheight=0.15, anchor='n')

frame4 = tk.Frame(root, bg=light_blue, bd=10)
frame4.place(relx=0.4, rely=0.6, relwidth=0.7, relheight=0.15, anchor='n')

frame5 = tk.Frame(root, bg=light_blue, bd=10)
frame5.place(relx=0.4, rely=0.775, relwidth=0.7, relheight=0.15, anchor='n')



root.mainloop()
