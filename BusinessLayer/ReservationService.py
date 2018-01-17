from BusinessLayer.VehicleService import VehicleService
from DataLayer.DatabaseManager import DatabaseManager
from datetime import datetime, timedelta

class ReservationService():
    def __init__(self):
        self.db = DatabaseManager()
        self.vs = VehicleService()

    def makeReservation(self, parkingspotId, licenceplate, begindate, duration):
        carid = self.vs.getVehicle(licenceplate)
        if len(carid) == 0:
            carid = self.vs.createVehicle(licenceplate)
        print carid
        begin = datetime.strptime(begindate, '%Y-%m-%d %H:%M')
        end = begin + timedelta(minutes=int(duration))
        con = self.db.createConnection()
        self.db.insertRecord((carid[0][0], str(parkingspotId), str(begin), str(end)), "reservation", con)
        con.close()

