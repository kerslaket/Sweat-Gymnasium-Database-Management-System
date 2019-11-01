from PyQt4.QtGui import *
from PyQt4.QtSql import *
from sqlite3 import *

from gym_database_class import *

class BrowseDataWidget(QWidget):
	"""A widget for displaying Database data"""
	
	def __init__(self):
	
		self.loadDataBase = None
		super().__init__()
		self.layout = QVBoxLayout()
		
		self.table_view = QTableView()
		
		self.layout.addWidget(self.table_view)
		
		self.setLayout(self.layout)

		self.database = None 

		
	def PopulateTable(self,item,labels):
                #method for adding all the information from the database to the table view based on the currently opened database
				self.database = Database(self.loadDataBase)
				self.database.loadDatabase()
				data = self.database.getAllData(item)
				model = QStandardItemModel()
				model.setHorizontalHeaderLabels(labels)
				row = 0
				for item in data:
					for column in range(len(item)):
						if item[column] == "None":
							print(item[column])
							item = (" ")
						else:
							StandardItem = QStandardItem("{}".format(item[column]))
							model.setItem(row, column, StandardItem)
					row += 1
				self.table_view.setModel(model)

												
												
								

								
	def UpdateTable(self,newDataBase):
                #method for loading a new database when the user opens a new database or reopens a database
		self.loadDataBase = newDataBase








