from PyQt4.QtGui import *
from gym_delete_function import *

class DeleteDialog(QDialog):
	"""This class creates the dialog window for deleting items from the database"""

	def __init__(self,database):
		super().__init__()
		
		self.database = database

		#create widgets
		self.table_select_combo_box = QComboBox()
		self.item_select_combo_box = QComboBox()
		self.delete_push_button = QPushButton("Delete")
		self.delete_all_push_button = QPushButton("Delete All Items")

		self.table_select_combo_box.addItem("Select Table")
		self.table_select_combo_box.addItem("Members")
		self.table_select_combo_box.addItem("Payments")
		self.table_select_combo_box.addItem("Regimes")
		self.table_select_combo_box.addItem("Exercises")
		
		self.item_select_combo_box.addItem("Select Item")

		#create layout
		self.layout = QVBoxLayout()

		#add widgets to layout
		self.layout.addWidget(self.table_select_combo_box)
		self.layout.addWidget(self.item_select_combo_box)
		self.layout.addWidget(self.delete_push_button)
		self.layout.addWidget(self.delete_all_push_button)

		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("Delete")
		self.setWindowIcon(QIcon("WindowIcon.png"))

		#connections
		self.table_select_combo_box.currentIndexChanged.connect(self.itemComboBoxPopulate)
		self.delete_push_button.clicked.connect(self.deleteItems)
		self.delete_all_push_button.clicked.connect(self.deleteAllItems)
		
	def itemComboBoxPopulate(self):
                #method for populating the item select combobox with the correct items and formating from the correct tables
		if self.table_select_combo_box.currentIndex() == 0:
			self.item_select_combo_box.clear()
			self.item_select_combo_box.addItem("Select Item")
		if self.table_select_combo_box.currentIndex() == 1:
			items = getItems(self.database, "MEMBERS")
			self.item_select_combo_box.clear()
			for count in range(len(items)):
				self.item_select_combo_box.addItem(items[count])
		if self.table_select_combo_box.currentIndex() == 2:
			items = getItems(self.database, "PAYMENTS")
			self.item_select_combo_box.clear()
			for count in range(len(items)):
				self.item_select_combo_box.addItem(items[count])
		if self.table_select_combo_box.currentIndex() == 3:
			items = getItems(self.database, "REGIME")
			self.item_select_combo_box.clear()
			for count in range(len(items)):
				self.item_select_combo_box.addItem(items[count])
		if self.table_select_combo_box.currentIndex() == 4:
			items = getItems(self.database, "EXERCISE")
			self.item_select_combo_box.clear()
			for count in range(len(items)):
				self.item_select_combo_box.addItem(items[count])
				
	def deleteItems(self):
                #method for deleting the correct items from the correct table
		if self.table_select_combo_box.currentIndex() == 0:
			return
		if self.table_select_combo_box.currentIndex() == 1:
			deleteQueryPrimaryKey(self.database,"MEMBERS","MEMBERID",str(self.item_select_combo_box.currentText())[0])
		if self.table_select_combo_box.currentIndex() == 2:
			sep = " - "
			deleteQueryCompositeKey(self.database,"PAYMENTS","MEMBERID","PAYMENTDATE",str(self.item_select_combo_box.currentText())[0],str(self.item_select_combo_box.currentText()).split(sep,1)[1])
		if self.table_select_combo_box.currentIndex() == 3:
			sep = " - "
			deleteQueryCompositeKey(self.database,"REGIME","MEMBERID","EXERCISEID",str(self.item_select_combo_box.currentText())[0],str(self.item_select_combo_box.currentText()).split(sep,1)[1][0])
		if self.table_select_combo_box.currentIndex() == 4:
			deleteQueryPrimaryKey(self.database,"EXERCISE","EXERCISEID",str(self.item_select_combo_box.currentText())[0])
		
	def deleteAllItems(self):
                #method for deleting every item in a certain table
		if self.table_select_combo_box.currentIndex() == 0:
			return
		if self.table_select_combo_box.currentIndex() == 1:
			deleteAll(self.database,"MEMBERS")
		if self.table_select_combo_box.currentIndex() == 2:
			deleteAll(self.database,"PAYMENTS")
		if self.table_select_combo_box.currentIndex() == 3:
			deleteAll(self.database,"REGIME")
		if self.table_select_combo_box.currentIndex() == 4:
			deleteAll(self.database,"EXERCISE")
