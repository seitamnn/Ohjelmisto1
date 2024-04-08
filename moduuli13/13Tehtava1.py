# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
from flask import Flask, Response
import json

app = Flask(__name__)

# http://127.0.0.1:3000/alkuluku/<luku>
@app.route('/alkuluku/<luku>')
def onko_alkuluku(luku):
    try:
        luku = int(luku)
        onko = None
        if luku < 2:
            onko = False
        else:
            onko = True
            for n in range(2, int(luku / 2) + 1):
                if luku % n == 0:
                    onko = False
                    break
        tila = 200
        vastaus = {
            "Number": luku,
            "isPrime": onko
        }
    except ValueError:
        tila = 400
        vastaus = {
            "status": tila,
            "teksti": "Virheellinen yhteenlaskettava"
        }
    json_vast = json.dumps(vastaus)
    return Response(response=json_vast, status=tila, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)