from PyQt4.QtGui import *
from gym_add_edit_dialog_class import *

class EditDialog(AddEditDialog):
	"""This class creates the dialog window for editing items in the database"""

	def __init__(self,database):
		super().__init__(database)
		
		self.add_edit_button.setText("Edit")
		self.setWindowTitle("Edit")

		#connections
		self.add_edit_button.clicked.connect(self.editItems)
		
	def editItems(self):
                #method for using the correct methods to edit items in a table, with the table changing based on which widget is selected from the stacked layout
		if self.stackedLayout.currentIndex() == 0:
			self.memberLayoutWidget.editMemberItems(self.database)
		if self.stackedLayout.currentIndex() == 1:
			self.paymentLayoutWidget.editPaymentItems(self.database)
		if self.stackedLayout.currentIndex() == 2:
			self.regimeLayoutWidget.editRegimeItems(self.database)
		if self.stackedLayout.currentIndex() == 3:
			self.exerciseLayoutWidget.editExerciseItems(self.database)			
		self.close()
		
		
