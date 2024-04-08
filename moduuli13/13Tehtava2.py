# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
# lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä
# lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

#http://127.0.0.1:3000/kenttä/<ICAO>
@app.route('/kenttä/<ICAO>')
def search_airport(ICAO):
    try:
        koodi = ICAO
        tilakoodi = 200
        sql = f"SELECT name, municipality FROM airport WHERE ident= '{koodi}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        vastaus = {
            "ICAO": ICAO,
            "Name": result[0],
            "Municipality": result[1]
        }
    except mysql.connector.Error:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen ICAO"
        }
    json_vast = json.dumps(vastaus)
    return Response(response=json_vast, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)