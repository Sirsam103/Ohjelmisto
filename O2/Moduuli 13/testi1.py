import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='M4ri4nn€k4rkki',

         autocommit=True
         )


def haelentokentat(maakoodi):
    param_tuple = (maakoodi, )
    sql = "SELECT * FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, param_tuple)
    tulos = kursori.fetchall()
    if tulos:
        print(tulos)
    '''if kursori.rowcount > 0:
        for x in tulos:
            print(x[1], x[3], x[10])#koordinaatit ovat: {x[4]}, {x[5]}')'''


haelentokentat(input('Anna lentokentän ICAO koodi: '))