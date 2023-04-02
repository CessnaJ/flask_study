from flask_mysqldb import MySQL

def get_all_bus_stops_from_database(mysql: MySQL):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT ARO_BUSSTOP_ID, GPS_LATI, GPS_LONG FROM bus_stop")
    bus_stops = cursor.fetchall()
    cursor.close()

    bus_stop_data = []
    for bus_stop in bus_stops:
        bus_stop_data.append({
            'ARO_BUSSTOP_ID': bus_stop[0],
            'lat': bus_stop[1],
            'lng': bus_stop[2]
        })

    return bus_stop_data


def create_bus_stop_table(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bus_stop (
            ARO_BUSSTOP_ID INT PRIMARY KEY,
            BUSSTOP_NM VARCHAR(255),
            GPS_LATI DOUBLE,
            GPS_LONG DOUBLE
        )
        """)
    mysql.connection.commit()
    cursor.close()


def insert_bus_stop_data(mysql, data):
    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO bus_stop (ARO_BUSSTOP, INSERT_ID, BUSSTOP_NM, GPS_LATI, GPS_LONG)
        VALUES (%s, %s, %s, %s)
        """
    cursor.executemany(query, data)
    mysql.connection.commit()
    cursor.close()