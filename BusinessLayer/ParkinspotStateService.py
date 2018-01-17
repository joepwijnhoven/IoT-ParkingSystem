
from datetime import datetime, timedelta

from DataLayer.DatabaseManager import DatabaseManager

class ParkingspotStateService():
    def __init__(self):
        self.db = DatabaseManager()

    def getParkingSpotState(self, object, ip, updateIfExists):
        self.createParkingSpotIfNotExist(object[2], ip, updateIfExists)
        con = self.db.createConnection()
        state = self.db.executeSQL(con, "select state from parkingspot where id='" + str(object[2].get(32800)) + "'")
        con.close()
        return ''.join(state[0])

    def createParkingSpotIfNotExist(self, object, ip, updateIfExists):
        con = self.db.createConnection()
        parkingspot = self.db.executeSQL(con, "select state from parkingspot where id='" + str(object.get(32800)) + "'")
        if len(parkingspot) == 0:
            self.db.insertRecord((str(object.get(32800)), object.get(32803), str(object.get(32801)), str(ip)), "parkingspot", con)
        elif updateIfExists:
            self.db.executeSQL(con, "UPDATE parkingspot SET billingrate='" + str(object.get(32803)) + "', state='" + str(object.get(32801)) + "', IP='" + ip + "' WHERE id='" + str(object.get(32800)) + "'")
        con.close()

    def getParkingSpotById(self, id):
        con = self.db.createConnection()
        parkingspot = self.db.executeSQL(con, "select * from parkingspot where id='" + id + "'")
        con.close()
        return parkingspot

    def getFreeParkingSpots(self, date, duration):
        begin = datetime.strptime(date, '%Y-%m-%d %H:%M')
        end = begin + timedelta(minutes=duration)
        con = self.db.createConnection()

        parkingspots = self.db.executeSQL(con,
                                    "select id from parkingspot where id NOT IN (select parkingspot_id from reservation where begindate <= '" + str(
                                        begin) + "' AND enddate >='" + str(end) + "')")
        con.close()
        return parkingspots





