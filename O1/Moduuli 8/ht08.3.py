import mysql.connector
from geopy import distance
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='M4ri4nn€k4rkki',
         autocommit=True
         )


def haenimsij(ICAO):
    param_tuple = (ICAO, )
    sql = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s "
    kursori = yhteys.cursor(dictionary=False)
    kursori.execute(sql, param_tuple)
    tulos = kursori.fetchone()
    return tulos


lent1 = input('Kerro ensimmäisen lentokentän ICAO koodi: ')
lent2 = input('Kerro toisen lentokentän ICAO koodi: ')

lent1nimsij = haenimsij(lent1)
lent2nimsij = haenimsij(lent2)
lent1nimi, lent1lat, lent1lon = lent1nimsij
lent2nimi, lent2lat, lent2lon = lent2nimsij

etais = distance.great_circle((lent1lat, lent1lon), (lent2lat, lent2lon)).km
print(f'Lentokenttien {lent1nimi} ja {lent2nimi} välillä on {etais:.2f} kilometriä etäisyyttä')
