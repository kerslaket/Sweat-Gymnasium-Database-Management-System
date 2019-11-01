from PyQt4.QtGui import *
from gym_search_results_dialog_class import *
from gym_search_function import *

class SearchDialog(QDialog):
	"""This class creates the dialog window for searching for something"""

	def __init__(self,database):
		super().__init__()

		self.database = database	
		
		#create widgets
		self.table_combo_box = QComboBox()
		self.search_box = QLineEdit()
		self.search_push_button = QPushButton("Search")

		self.table_combo_box.addItem("Select Table")
		self.table_combo_box.addItem("MEMBERS")
		self.table_combo_box.addItem("PAYMENTS")
		self.table_combo_box.addItem("REGIME")
		self.table_combo_box.addItem("EXERCISE")
		self.search_box.setPlaceholderText("Enter Search Term")

		#create layout
		self.layout = QVBoxLayout()

		#add widgets to layout
		self.layout.addWidget(self.table_combo_box)
		self.layout.addWidget(self.search_box)
		self.layout.addWidget(self.search_push_button)

		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("Search")
		self.setWindowIcon(QIcon("WindowIcon.png"))

		#connections
		self.search_push_button.clicked.connect(self.search)

		
	def search(self):
                #method for searching the database
		results = searchQuery(self.database,self.table_combo_box.currentText(),'"'+self.search_box.text()+'"')
		results_dialog = ResultsDialog(results)
		results_dialog.exec_()
