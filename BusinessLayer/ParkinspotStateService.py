from DataLayer.DatabaseManager import DatabaseManager

class ParkingspotStateService():
    def __init__(self):
        self.db = DatabaseManager()

    def getParkingSpotState(self, object):
        print object[2]
        print object[2].get(32800)
        self.createParkingSpotIfNotExist(object[2])
        con = self.db.createConnection()
        state = self.db.executeSQL(con, "select state from parkingspot where id='" + str(object[2].get(32800)) + "'")
        con.close()
        return ''.join(state[0])

    def createParkingSpotIfNotExist(self, object):
        con = self.db.createConnection()
        parkingspot = self.db.executeSQL(con, "select state from parkingspot where id='" + str(object.get(32800)) + "'")
        if parkingspot is None:
            self.db.insertRecord((str(object.get(32800)), object.get(32803), str(object.get(32801))), "parkingspot", con)
        print parkingspot
        con.close()