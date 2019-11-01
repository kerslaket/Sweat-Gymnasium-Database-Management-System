from PyQt4.QtGui import *
from gym_add_function import *
from gym_edit_function import *

class AddEditExerciseTableWidget(QWidget):
	"""This class creates the widget for the exercise table in the add and edit dialog boxes"""
	
	def __init__(self):
		super().__init__()
		
		#create widgets
		
		self.lineEdits = {}
		
		for count in range(3):
			self.lineEdits["self.enter_text {0}".format(count)] = QLineEdit()#creates 3 QLineEdits, 1 for each column in the table
			
		self.exerciseID_Label = QLabel("Exercise ID")
		self.name_Label = QLabel("Name")
		self.description_Label = QLabel("Description")
		
		
		# create exercise layout
		self.exerciseLayout = QVBoxLayout()
		self.exerciseContentLayout = QHBoxLayout()
		self.exerciseLabelLayout = QVBoxLayout()
		self.exerciseInputLayout = QVBoxLayout()
		
		self.exerciseLabelLayout.addWidget(self.exerciseID_Label)
		self.exerciseLabelLayout.addWidget(self.name_Label)
		self.exerciseLabelLayout.addWidget(self.description_Label)
		
		for count in range(3):
			self.exerciseInputLayout.addWidget(self.lineEdits["self.enter_text {0}".format(count)])#adds each QLineEdit to the layout
		
		self.exerciseContentLayout.addLayout(self.exerciseLabelLayout)
		self.exerciseContentLayout.addLayout(self.exerciseInputLayout)
		self.exerciseLayout.addLayout(self.exerciseContentLayout)
		
		self.setLayout(self.exerciseLayout)
	
	def addExerciseItems(self, database):
                #method for adding items to the exercise table
		addExercise(database,self.lineEdits["self.enter_text 0"].text(),self.lineEdits["self.enter_text 1"].text(),self.lineEdits["self.enter_text 2"].text())
		
	
	def editExerciseItems(self,database):
                #method for editing items in the exercise table
		columns = ["Name","Description"]
		items = ""
		for count in range(1,3):
			if self.lineEdits["self.enter_text {0}".format(count)].text() != "":
				items +=(columns[count-1] + "='" + self.lineEdits["self.enter_text {0}".format(count)].text() + "' ,")
		items = items[:-1]
		
		editExercise(database,items,self.lineEdits["self.enter_text 0"].text())
