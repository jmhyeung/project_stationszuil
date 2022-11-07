from tkinter import *
from tkinter.ttk import *
import psycopg2
from config import config

WIDTH = 780
HEIGHT = 520

root = Tk()

root.title('Stationshalscherm')
root.geometry(f'{WIDTH}x{HEIGHT}')

frame = Frame(root, width=WIDTH, height=HEIGHT)
frame.grid(row=0, column=0, sticky='NW')

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
    db_version = cursor.fetchone()
    print(db_version)

    cursor.execute( 'SELECT SS.station_city, SS.country, SS.ov_bike, SS.elevator, SS.toilet, SS.park_and_ride '
                    'FROM public.user_message as UM JOIN public.station_service as SS ON station = station_city '
                    'ORDER BY user_date, user_time DESC LIMIT 5')

    messages = list(cursor.fetchall())

    lbl1 = Label(root, text=f'{messages[-5][1]}\n{messages[-5][5]}', font='Arial 17 bold')
    lbl2 = Label(root, text=f'{messages[-4][1]}\n{messages[-4][5]}', font='Arial 17 bold')
    lbl3 = Label(root, text=f'{messages[-3][1]}\n{messages[-3][5]}', font='Arial 17 bold')
    lbl4 = Label(root, text=f'{messages[-2][1]}\n{messages[-2][5]}', font='Arial 17 bold')
    lbl5 = Label(root, text=f'{messages[-1][1]}\n{messages[-1][5]}', font='Arial 17 bold')

    lbl1.place(relx=0.5, rely=0.1, anchor=CENTER)
    lbl2.place(relx=0.5, rely=0.3, anchor=CENTER)
    lbl3.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl4.place(relx=0.5, rely=0.7, anchor=CENTER)
    lbl5.place(relx=0.5, rely=0.9, anchor=CENTER)

    cursor.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
        print('Database connection terminated.')

root.mainloop()
