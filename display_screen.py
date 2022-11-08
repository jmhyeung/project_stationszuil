from tkinter import *
import psycopg2
from config import config
import time

WIDTH = 780
HEIGHT = 400

root = Tk()

root.title('Stationshalscherm')
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# # lbl = Label(window, text='Hello World!', font=('Arial Bold', 50))
# # lbl.grid(column=0, row=0)
# #
# #
# # def clicked():
# #     lbl.configure(text='The button has been pressed!')
# #
# #
# # btn = Button(window, text='Click on me', command=clicked)
# # btn.grid(column=1, row=0)
#
# combo = Combobox(window)
#
# combo['values']=(1,2,3, 'First line', 'Second line', 'Third line')
# combo.current(0)
# combo.grid(column=0, row=0)

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

    cursor.execute('SELECT UM.user_message,'
                   'SS.station_city, SS.country, SS.ov_bike, SS.elevator, SS.toilet, SS.park_and_ride '
                   'FROM public.user_message as UM JOIN public.station_service as SS ON station = station_city '
                   'WHERE approved = 1 '
                   'ORDER BY user_date, user_time DESC LIMIT 5')

    messages = list(cursor.fetchall())

    msg = []

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


    station_frame = Frame(root, bg='white')
    station_frame.place(relx=0.2, relwidth=0.6, relheight=0.2)

    station_label = Label(station_frame, text=msg[0][1], font='Arial 25 bold', bg='white', fg='black')
    station_label.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

    message_frame = Frame(root, bg='purple')
    message_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

    message_label = Label(message_frame, text=msg[0][0], font='Arial 18 bold', bg='white')
    message_label.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

    facility_frame = Frame(root, bg='cyan')
    facility_frame.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.2)

    facility_label = Label(facility_frame, text=f'Er zijn: {msg[0][2:]} beschikbaar', font='Arial 12 bold')
    facility_label.place(relx=0.1, rely=0.7, relwidth=1, relheight=1, anchor=W)

root.mainloop()
