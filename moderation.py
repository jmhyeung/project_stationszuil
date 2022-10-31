from datetime import datetime
import psycopg2
from config import config

name_mod = input('Moderator\'s naam:\n')
mail_mod = input('Moderator\'s email-adres:\n')

timestamp = datetime.now()

with open('user_messages', 'r') as f:
    lines = f.readlines()
    info_message = []

    for line in lines:
        print(line.replace('\t\t', '').replace('\n', ''))
        struct_line = line.replace('\t\t', '').replace('\n', '').replace(',', '')

        #TODO: Is it approved or not then connect it to a database
        approval = input('Is het bericht goedgekeurd (Ja of nee)?\n')

        while True:
            if approval.lower()[0] == 'j':
                info_message.append(struct_line + ' 1 ' + timestamp.strftime("%d-%B-%Y %H:%M:%S") + ' '
                                    + name_mod + ' ' + mail_mod)
                break
            elif approval.lower()[0] == 'n':
                info_message.append(struct_line + ' 0 ' + timestamp.strftime("%d-%B-%Y %H:%M:%S") + ' '
                                    + name_mod + ' ' + mail_mod)
                break
            else:
                print('Dat is geen ja of nee')


        #TODO: remove messages

for x in info_message:
    print(x)


def connect():
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

            struct_message = message.split()
            print(struct_message)

            cursor.execute('INSERT INTO public.user_message(message, date, time, name, station)'
                           'VALUES (%s, %s, %s, %s, %s)',
                           (struct_message[0],
                            struct_message[1],
                            struct_message[2],
                            struct_message[3],
                            struct_message[4]))

            cursor.execute('INSERT INTO public.approved_message(approved, date, mod_name, mod_email)'
                           'VALUES (%s, %s, %s, %s)',
                           (struct_message[5],
                            struct_message[6],
                            struct_message[7],
                            struct_message[8]))

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
