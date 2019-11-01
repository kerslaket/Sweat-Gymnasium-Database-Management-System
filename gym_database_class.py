import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def loadDatabase(self):
        #method that connects to the right database based on the file that was opened by the user
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()

    def getAllData(self,table):
        #method for retrieving all the data from a specific table in the database with a Select Query
        with sqlite3.connect(self.db_name) as db:
          allData = []
          cursor = db.cursor()
          query = "Select * From " + str(table)
          cursor.execute(query)
          data = cursor.fetchall()
          for item in data:
              allData.append(item)
          return allData




