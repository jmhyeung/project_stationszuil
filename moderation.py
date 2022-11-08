from datetime import datetime
import psycopg2
from config import config

name_mod = input('Moderator\'s naam:\n')
mail_mod = input('Moderator\'s email-adres:\n')

timestamp = datetime.now()

with open('user_messages', 'r+') as f:
    lines = f.readlines()
    info_message = []

for line in lines:
    print(line.replace('\t\t', '').replace('\n', ''))   # Make the lines readable for the moderator
    line = line.replace('\n', '')   # Make the line readable for the program

    is_approved = -1

    while is_approved == -1:
        approval = input('Is het bericht goedgekeurd (Ja of nee)?\n')

        # Check if the message is approved or not
        if approval.lower()[0] == 'j':
            is_approved = 1
        elif approval.lower()[0] == 'n':
            is_approved = 0
        else:
            print('Dat is geen ja of nee')

    user_time = timestamp.strftime("%d-%B-%Y, \t\t%H:%M:%S")
    # Append all the information to a list
    info_message.append(f'{line}, \t\t{is_approved}, \t\t{user_time}, \t\t{name_mod}, \t\t{mail_mod}')

# Delete the content in 'user_messages' file
with open('user_messages', 'w') as f:
    pass


def connect():
    # Makes a connection with the database
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

        for message in info_message:
            struct_message = message.split(', \t\t')

            # Split the list and commit all the information to the database
            cursor.execute('INSERT INTO public.user_message('
                           'user_message,'
                           'user_date,'
                           'user_time,'
                           'user_name,'
                           'station,'
                           'approved,'
                           'mod_date,'
                           'mod_time,'
                           'mod_name,'
                           'mod_email)'
                           'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           struct_message)

        connection.commit()
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')


if __name__ == '__main__':
    connect()
