import mysql.connector
import os
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='M4ri4nn€k4rkki',
         autocommit=True
         )

def lentokentta(zzz):
    param_tuple = (zzz, )
    sql = "SELECT * FROM airport WHERE name LIKE %s AND type = 'closed' AND continent = 'EU'"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, param_tuple)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        i = 0
        for x in tulos:
            print(f'{x}')
            i += 1
        os.system('cls')
        print(i)


lentokentta('%Air Base%')
