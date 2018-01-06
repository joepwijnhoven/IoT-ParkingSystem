from DataLayer.DatabaseManager import DatabaseManager

class TestClass():
    def __init__(self):
        self.DM = DatabaseManager()


    def getSomething(self):
        connection = self.DM.createConnection();
        print self.DM.executeSQL(connection, "select * from car")
        connection.close()

    def insertSomething(self):
        connection = self.DM.createConnection();
        print self.DM.insertRecord((5, "parkingspot 5"), "parkingspot")
        connection.close()