from flask import Flask, request, jsonify
import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='M4ri4nn€k4rkki',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def airport(ICAO):
    param_tuple = (ICAO,)
    sql = "SELECT * FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, param_tuple)
    tulos = kursori.fetchone()
    try:
        return {"ICAO": tulos[1], "Name": tulos[3], "Municipality": tulos[10]}
    except ValueError:
        return {'No airport matches the icao: ', ICAO}


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)