from datetime import datetime
import psycopg2
from config import config

name_mod = input('Moderator\'s naam:\n')
mail_mod = input('Moderator\'s email-adres:\n')

timestamp = datetime.now()

with open('user_messages', 'r+') as f:
    lines = f.readlines()
    info_message = []
    pointer = 0

    for line in lines:
        print(line.replace('\t\t', '').replace('\n', ''))
        struct_line = line.replace('\t\t', '').replace('\n', '').replace(',', '')

        while True:
            approval = input('Is het bericht goedgekeurd (Ja of nee)?\n')

            if approval.lower()[0] == 'j':
                info_message.append(line + ', \t\t1, \t\t' + timestamp.strftime("%d-%B-%Y, \t\t%H:%M:%S, \t\t") +
                                    name_mod + ', \t\t' + mail_mod)
                break
            elif approval.lower()[0] == 'n':
                info_message.append(line + ', \t\t0, \t\t' + timestamp.strftime("%d-%B-%Y, \t\t%H:%M:%S, \t\t") +
                                    name_mod + ', \t\t' + mail_mod)
                break
            else:
                print('Dat is geen ja of nee')

        f.seek(0)
        print(line)
        #TODO: remove messages
        if line != lines.index[pointer]:
            f.write(line)
        pointer += 1


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
            struct_message = message.split(', \t\t')

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
                           (struct_message[0],
                            struct_message[1],
                            struct_message[2],
                            struct_message[3],
                            struct_message[4],
                            struct_message[5],
                            struct_message[6],
                            struct_message[7],
                            struct_message[8],
                            struct_message[9]))

        # connection.commit()
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')


if __name__ == '__main__':
    connect()
