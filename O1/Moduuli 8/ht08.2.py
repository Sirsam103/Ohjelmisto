import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='M4ri4nn€k4rkki',
         autocommit=True
         )


def haelentokentat(maakoodi):
    param_tuple = (maakoodi, )
    sql = "SELECT * FROM airport WHERE iso_country = %s AND type = %s "
    kursori = yhteys.cursor(dictionary=False)
    kursori.execute(sql, param_tuple)
    tulos = kursori.fetchall()
    return tulos


maakoodi = input('Anna maakoodi: ')
kentat = haelentokentat(maakoodi)
closed, small, medium, large, sea, heli, ball, oth = 0, 0, 0, 0, 0, 0, 0, 0
for x in kentat:
    if x[2] == 'closed':
        closed += 1
    elif x[2] == 'small_airport':
        small += 1
    elif x[2] == 'medium_airport':
        medium += 1
    elif x[2] == 'large_airport':
        large += 1
    elif x[2] == 'seaplane_base':
        sea += 1
    elif x[2] == 'heliport':
        heli += 1
    elif x[2] == 'balloonport':
        ball += 1
    else:
        oth += 1
        print(x[2])
print(f"Suljettuja lentokenttiä: {closed}\nPieniä lentokenttiä: {small}\nKeskikokoisia lentokenttiä: {medium}\nSuuria lentokenttiä: {large}\nVesitasokenttiä: {sea}\nHelikopterikenttiä: {heli}\nKuumailmapallokenttiä: {ball}")

