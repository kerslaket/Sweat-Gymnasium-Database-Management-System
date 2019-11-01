from PyQt4.QtGui import *
from gym_add_edit_dialog_class import *

class AddDialog(AddEditDialog):
	"""This class creates the dialog window for Adding items to the database"""

	def __init__(self,database):
		super().__init__(database)

		self.add_edit_button.setText("Add")
		self.setWindowTitle("Add")
		
		#connections
		self.add_edit_button.clicked.connect(self.addItems)
		
	def addItems(self):
                #method for using the correct methods to add items to a table, with the table changing based on which widget is selected from the stacked layout
		if self.stackedLayout.currentIndex() == 0:
			self.memberLayoutWidget.addMemberItems(self.database)
		if self.stackedLayout.currentIndex() == 1:
			self.paymentLayoutWidget.addPaymentItems(self.database)
		if self.stackedLayout.currentIndex() == 2:
			self.regimeLayoutWidget.addRegimeItems(self.database)
		if self.stackedLayout.currentIndex() == 3:
			self.exerciseLayoutWidget.addExerciseItems(self.database)			
		self.close()
		
