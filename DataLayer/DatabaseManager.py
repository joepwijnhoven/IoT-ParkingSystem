import sqlite3
from sqlite3 import Error

class DatabaseManager():
    database = "C:\\Users\\joep\\Documents\\IoT-ParkingSystem\\pythonsqlite.db"

    sql_create_parkingspot_table = """ CREATE TABLE IF NOT EXISTS parkingspot (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL
                                        ); """

    sql_create_car_table = """ CREATE TABLE IF NOT EXISTS car (
                                                id integer PRIMARY KEY,
                                                licenceplate text NOT NULL
                                            ); """

    sql_create_reservation_table = """ CREATE TABLE IF NOT EXISTS reservation (
                                                id integer PRIMARY KEY,
                                                car_id integer,
                                                parkingspot_id integer,
                                                date text,
                                                FOREIGN KEY(car_id) REFERENCES car(id),
                                                FOREIGN KEY(parkingspot_id) REFERENCES parkingspot(id)
                                            ); """

    def __init__(self):
        connection = self.createConnection(self.database);
        if connection is not None:
            self.createTables(connection)
        else:
            print("Error! cannot create the database connection.")

    def createConnection(self, path):
        try:
            conn = sqlite3.connect(path)
            return conn
        except Error as e:
            print(e)

        return None

    def createTables(self, connection):
        try:
            c = connection.cursor()
            c.execute(self.sql_create_parkingspot_table)
            c.execute(self.sql_create_car_table)
            c.execute(self.sql_create_reservation_table)
        except Error as e:
            print(e)

    def testInsert(self, connection):
        try:
            parkeerplaats = (1, 'parkeerplaats 1')
            sql1 = ''' INSERT INTO parkingspot(id, name)
                          VALUES(?,?) '''
            auto = (1, 'AAXAA')
            sql2 = ''' INSERT INTO car(id, licenceplate)
                                      VALUES(?,?) '''
            reservering = (1, 1, 1, '03-01-2018')
            sql3 = ''' INSERT INTO reservation(id, car_id, parkingspot_id, date)
                                                  VALUES(?,?,?,?) '''
            cur = connection.cursor()
            cur.execute(sql1, parkeerplaats)
            cur.execute(sql2, auto)
            cur.execute(sql3, reservering)
            connection.commit()
        except Error as e:
            print(e)

    def testSelect(self, connection):
        try:
            c = connection.cursor()
            c.execute('SELECT reservation.id, licenceplate, name FROM car INNER JOIN reservation ON car.id = reservation.car_id INNER JOIN parkingspot ON parkingspot.id = reservation.parkingspot_id')
            print c.fetchone()
        except Error as e:
            print(e)

d = DatabaseManager()
con = d.createConnection(d.database)

d.testSelect(con)
con.close()
