import sqlite3
from sqlite3 import Error

class DatabaseManager():
    database = "C:\\Users\\joep\\Documents\\IoT-ParkingSystem\\pythonsqlite.db"

    sql_create_parkingspot_table = """ CREATE TABLE IF NOT EXISTS parkingspot (
                                            id text PRIMARY KEY,
                                            billingrate REAL NOT NULL,
                                            state text NOT NULL
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
                                                begintime text,
                                                endtime text,
                                                FOREIGN KEY(car_id) REFERENCES car(id),
                                                FOREIGN KEY(parkingspot_id) REFERENCES parkingspot(id)
                                            ); """

    def __init__(self):
        connection = self.createConnection();
        if connection is not None:
            self.createTables(connection)
        else:
            print("Error! cannot create the database connection.")
        connection.close()

    def createConnection(self):
        try:
            conn = sqlite3.connect(self.database)
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

    def insertRecord(self, object, tablename, connection):
        try:
            if tablename == "car":
                sql = 'INSERT INTO car(id, licenceplate) VALUES(?,?) '
            elif tablename == "parkingspot":
                sql = ' INSERT INTO parkingspot(id, billingrate, state) VALUES(?,?,?) '
            elif tablename == "reservation":
                sql = ' INSERT INTO reservation(id, car_id, parkingspot_id, date, begintime, endtime) VALUES(?,?,?,?,?,?) '
            else:
                raise Exception("tablename not found")

            cur = connection.cursor()
            cur.execute(sql, object)
            connection.commit()
        except Error as e:
            print(e)

    def executeSQL(self, connection, sql):
        try:
            c = connection.cursor()
            c.execute(sql)
            return c.fetchall()
        except Error as e:
            return None;

    def testInsert(self, connection):
        try:
            parkeerplaats = (1, 'parkeerplaats 2', 'RED')
            sql1 = ''' INSERT INTO parkingspot(id, billingrate, state)
                          VALUES(?,?,?) '''
            auto = (2, 'BBXAA')
            sql2 = ''' INSERT INTO car(id, licenceplate)
                                      VALUES(?,?) '''
            reservering = (2, 2, 2, '04-01-2018', '13:00', '14:00')
            sql3 = ''' INSERT INTO reservation(id, car_id, parkingspot_id, date, begintime, endtime)
                                                  VALUES(?,?,?,?,?,?) '''
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
            c.execute('SELECT reservation.id, licenceplate, name, date FROM car INNER JOIN reservation ON car.id = reservation.car_id INNER JOIN parkingspot ON parkingspot.id = reservation.parkingspot_id')
            print c.fetchall()
        except Error as e:
            print(e)


##dm = DatabaseManager()
##con = dm.createConnection()
##print dm.executeSQL(con, "select * from parkingspot")