from DataLayer.DatabaseManager import DatabaseManager

class VehicleService():
    def __init__(self):
        self.db = DatabaseManager()

    def getVehicle(self, licenceplate):
        con = self.db.createConnection()
        vehicle = self.db.executeSQL(con, "select rowid from car where licenceplate='" + licenceplate + "'")
        con.close()
        return vehicle

    def createVehicle(self, licence):
        con = self.db.createConnection()
        self.db.insertRecord((licence,), "car", con)
        con.close()
        return self.getVehicle(licence)