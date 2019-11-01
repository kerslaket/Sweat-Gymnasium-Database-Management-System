from PyQt4.QtGui import *
from gym_add_function import *
from gym_edit_function import *

class AddEditRegimeTableWidget(QWidget):
	"""This class creates the widget for the regime table in the add and edit dialog boxes"""
	
	def __init__(self):
		super().__init__()
		
		#create widgets
		
		self.lineEdits = {}
		
		for count in range(5):
			self.lineEdits["self.enter_text {0}".format(count)] = QLineEdit()#creates 5 QLineEdits, 1 for each column in the regime database
			
		self.memberID_Label = QLabel("MemberID")
		self.exerciseID_Label = QLabel("Exercise ID")
		self.start_date_Label = QLabel("Start Date")
		self.end_date_Label = QLabel("End Date")
		self.description_Label = QLabel("Description")
		
		# create regime layout
		
		self.regimeLayout = QVBoxLayout()
		self.regimeContentLayout = QHBoxLayout()
		self.regimeLabelLayout = QVBoxLayout()
		self.regimeInputLayout = QVBoxLayout()
		
		self.regimeLabelLayout.addWidget(self.memberID_Label)
		self.regimeLabelLayout.addWidget(self.exerciseID_Label)
		self.regimeLabelLayout.addWidget(self.start_date_Label)
		self.regimeLabelLayout.addWidget(self.end_date_Label)
		self.regimeLabelLayout.addWidget(self.description_Label)
		for count in range(5):
			self.regimeInputLayout.addWidget(self.lineEdits["self.enter_text {0}".format(count)])#adds each QLineEdit to the layout
		
		self.regimeContentLayout.addLayout(self.regimeLabelLayout)
		self.regimeContentLayout.addLayout(self.regimeInputLayout)
		self.regimeLayout.addLayout(self.regimeContentLayout)
		
		self.setLayout(self.regimeLayout)

		
	def addRegimeItems(self,database):
                #method for adding items to the regime table
		addRegime(database,self.lineEdits["self.enter_text 0"].text(),self.lineEdits["self.enter_text 1"].text(),self.lineEdits["self.enter_text 2"].text(),self.lineEdits["self.enter_text 3"].text(),self.lineEdits["self.enter_text 3"].text())
	
	def editRegimeItems(self,database):
                #method for editing items in the regime table
		columns = ["StartDate","EndDate","SpecificDescription"]
		items = ""
		for count in range(2,5):
			if self.lineEdits["self.enter_text {0}".format(count)].text() != "":
				if count == 4:
					items +=(columns[count-2] + "='" + self.lineEdits["self.enter_text {0}".format(count)].text() + "' ,")
				else:
					items +=(columns[count-2] + "=" + self.lineEdits["self.enter_text {0}".format(count)].text() + " ,")
		items = items[:-1]
		
		editRegime(database,items,self.lineEdits["self.enter_text 0"].text(),self.lineEdits["self.enter_text 1"].text())
		
		
