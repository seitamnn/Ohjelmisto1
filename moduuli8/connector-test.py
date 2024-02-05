import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         #^tai localhost^
         port= 3306,
         # ^mariadb^
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         # sitoutetaanko jokainen SQL-operaatio välittömästi omana transaktionaan. Tähän kannattaa normaalisti asettaa arvoksi True, jolloin yksittäisten päivityslauseiden (esim. UPDATE) sitouttamisesta COMMIT-lausein ei tarvitse erikseen huolehtia.
         )

