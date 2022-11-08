# import van een extra module
# tip: deze moet je wel eerst installeren met pip install psycopg2
# tip: op een mac met een m1 chip: check met je docent
import psycopg2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':  # start van python script
    print('Start de connectie met de postgress databse')

# maak de connectie met de database
conn = psycopg2.connect(
    host="localhost",
    database="project_zuil",  # database naam
    user="postgres",  # user naam
    password="31415926535")  # wachtwoord van de user

# maak een cursor
cursor1 = conn.cursor()
# execute a statement
print('Check of het werk door de PostgreSQL database version op te vragen:')
cursor1.execute('SELECT version()')
db_version = cursor1.fetchone()
print(' db version:' + db_version[0])

# maal een nieuwe cursor aan
cursor = conn.cursor()

# maak de sql query aan die je naar de database wilt sturen
sql_query1 = 'select * from user_message'  # van de klant tabel
print('query is: ' + sql_query1)

# sql_query1 = 'INSERT INTO public.user_message(user_id, message, date, name, station) VALUES ('

# run de query
cursor.execute(sql_query1)

# haal het result op van de query (alles)
resultaat = cursor.fetchall()
print('resultaat van de query is: ')
if resultaat:  # check of er een resultaat is
    for row in resultaat:
        print(row)  # print alle rows van de tabel
