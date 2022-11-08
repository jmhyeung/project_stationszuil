import tkinter as tk
import psycopg2
from config import config
import requests
import textwrap
import random

WEATHER_KEY = '115f419b9fbe1130e711816717d39573'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q='

HEIGHT = 500
WIDTH = 800

light_blue = '#80c1ff'
white = '#F9F9F9'

root = tk.Tk()

root.title('Stationshalscherm')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Makes a connection with the database
connection = None
try:
    params = config()
    print('Connecting to the postgreSQL database . . .')
    connection = psycopg2.connect(**params)

    cursor = connection.cursor()
    print('PostgreSQL database version: ')
    cursor.execute('SELECT version()')
    db_version, = cursor.fetchone()
    print(db_version)

    # Select all the information that I need from the database
    cursor.execute('SELECT UM.user_message,'
                   'SS.station_city, SS.country, SS.ov_bike, SS.elevator, SS.toilet, SS.park_and_ride '
                   'FROM public.user_message as UM JOIN public.station_service as SS ON station = station_city '
                   'WHERE approved = 1 '
                   'ORDER BY user_date, user_time DESC LIMIT 5')

    messages = list(cursor.fetchall())

    msg = []

    # Put all the relevant information in a 3D list
    for i in messages:
        temp_list = [i[0], i[1]]

        if i[3]:
            temp_list.append('ov bike')
        if i[4]:
            temp_list.append('elevator')
        if i[5]:
            temp_list.append('toilet')
        if i[6]:
            temp_list.append('park and ride')

        msg.append(temp_list)

    print(msg)

    cursor.close()

except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
        print('Database connection terminated.')


def get_weather(city):
    url = f'{BASE_URL}{city}&appid={WEATHER_KEY}&units=metric'
    weather_json = requests.get(url).json()

    print(weather_json['main']['temp'])
    return weather_json['main']['temp']


frame1 = tk.Frame(root, bg=light_blue, bd=10)
frame1.place(relx=0.4, rely=0.075, relwidth=0.7, relheight=0.15, anchor='n')
station1 = tk.Label(frame1, text=msg[0][1], font='Arial 12 bold', bg=light_blue, bd=3, anchor='w')
station1.place(relwidth=0.3, relheight=0.3)
txt1 = '\n'.join(textwrap.wrap(msg[0][0], 60))
message1 = tk.Label(frame1, text=txt1, font='Arial 10 bold', bg=light_blue, bd=3, anchor='w')
message1.place(rely=0.35, relwidth=0.7, relheight=0.7)
facility1 = tk.Label(frame1, text=f'beschikbare faciliteiten:\n{" and ".join(msg[0][2:])}', font='Arial 10 bold', bg=light_blue,
                     bd=3, anchor='e')
facility1.place(relx=0.8, relwidth=0.4, relheight=1, anchor='n')

frame2 = tk.Frame(root, bg=light_blue, bd=10)
frame2.place(relx=0.4, rely=0.25, relwidth=0.7, relheight=0.15, anchor='n')
station2 = tk.Label(frame2, text=msg[1][1], font='Arial 12 bold', bg=light_blue, bd=3, anchor='w')
station2.place(relwidth=0.3, relheight=0.3)
txt2 = '\n'.join(textwrap.wrap(msg[1][0], 60))
message2 = tk.Label(frame2, text=txt2, font='Arial 10 bold', bg=light_blue, bd=3, anchor='w')
message2.place(rely=0.35, relwidth=0.7, relheight=0.7)
facility2 = tk.Label(frame2, text=f'beschikbare faciliteiten:\n{" and ".join(msg[1][2:])}', font='Arial 10 bold', bg=light_blue,
                     bd=3, anchor='e')
facility2.place(relx=0.8, relwidth=0.4, relheight=1, anchor='n')

frame3 = tk.Frame(root, bg=light_blue, bd=10)
frame3.place(relx=0.4, rely=0.425, relwidth=0.7, relheight=0.15, anchor='n')
station3 = tk.Label(frame3, text=msg[2][1], font='Arial 12 bold', bg=light_blue, bd=3, anchor='w')
station3.place(relwidth=0.3, relheight=0.3)
txt3 = '\n'.join(textwrap.wrap(msg[2][0], 60))
message3 = tk.Label(frame3, text=txt3, font='Arial 10 bold', bg=light_blue, bd=3, anchor='w')
message3.place(rely=0.35, relwidth=0.7, relheight=0.7)
facility3 = tk.Label(frame3, text=f'beschikbare faciliteiten:\n{" and ".join(msg[2][2:])}', font='Arial 10 bold', bg=light_blue,
                     bd=3, anchor='e')
facility3.place(relx=0.8, relwidth=0.4, relheight=1, anchor='n')

frame4 = tk.Frame(root, bg=light_blue, bd=10)
frame4.place(relx=0.4, rely=0.6, relwidth=0.7, relheight=0.15, anchor='n')
station4 = tk.Label(frame4, text=msg[3][1], font='Arial 12 bold', bg=light_blue, bd=3, anchor='w')
station4.place(relwidth=0.3, relheight=0.3)
txt4 = '\n'.join(textwrap.wrap(msg[3][0], 60))
message4 = tk.Label(frame4, text=txt4, font='Arial 10 bold', bg=light_blue, bd=3, anchor='w')
message4.place(rely=0.35, relwidth=0.7, relheight=0.7)
facility4 = tk.Label(frame4, text=f'beschikbare faciliteiten:\n{" and ".join(msg[3][2:])}', font='Arial 10 bold', bg=light_blue,
                     bd=3, anchor='e')
facility4.place(relx=0.8, relwidth=0.4, relheight=1, anchor='n')

frame5 = tk.Frame(root, bg=light_blue, bd=10)
frame5.place(relx=0.4, rely=0.775, relwidth=0.7, relheight=0.15, anchor='n')
station5 = tk.Label(frame5, text=msg[4][1], font='Arial 12 bold', bg=light_blue, bd=3, anchor='w')
station5.place(relwidth=0.3, relheight=0.3)
txt5 = '\n'.join(textwrap.wrap(msg[4][0], 60))
message5 = tk.Label(frame5, text=txt5, font='Arial 10 bold', bg=light_blue, bd=3, anchor='w')
message5.place(rely=0.35, relwidth=0.7, relheight=0.7)
facility5 = tk.Label(frame5, text=f'beschikbare faciliteiten:\n{" and ".join(msg[4][2:])}', font='Arial 10 bold', bg=light_blue,
                     bd=3, anchor='e')
facility5.place(relx=0.8, relwidth=0.4, relheight=1, anchor='n')

with open('stations') as f:
    stations = f.readlines()
    station = random.choice(stations)
    print(station)

weather_frame = tk.Frame(root, bg=light_blue, bd=10)
weather_frame.place(relx=0.875, rely=0.075, relwidth=0.2, relheight=0.85, anchor='n')
weather_label = tk.Label(weather_frame, text=f'Het is\n{get_weather(station)}\n graden in\n{station}',
                         font='Arial 12 bold', bg=light_blue, bd=3, anchor='n')
weather_label.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
