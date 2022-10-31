from datetime import datetime
import random

user_name = input('Wat is uw naam?\n')

if user_name == '':
    user_name = 'Anoniem'

while True:
    user_message = input('Voer een bericht met maximaal 140 karakters.\n')

    if len(user_message) < 141:
        break

    print('Uw bericht is te lang.')

timestamp = datetime.now()

with open('stations') as f:
    stations = f.readlines()
    station = random.choice(stations)

with open('user_messages', 'a') as f:
    f.write(f'{user_message}, \t\t{timestamp.strftime("%d-%B-%Y, %H:%M:%S")}, \t\t{user_name}, \t\t{station}')
