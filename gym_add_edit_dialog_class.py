from PyQt4.QtGui import *
from add_edit_member_table_widget_class import *
from add_edit_payment_table_widget_class import *
from add_edit_regime_table_widget_class import *
from add_edit_exercise_table_widget_class import *
from gym_add_function import *

class AddEditDialog(QDialog):
	"""This class creates the dialog window for Adding items to the database and answering them"""
	
	def __init__(self, database):
		super().__init__()
		
		self.table_combo_box = QComboBox()
		self.table_combo_box.addItem("Members")
		self.table_combo_box.addItem("Payments")
		self.table_combo_box.addItem("Regimes")
		self.table_combo_box.addItem("Exercises")
		self.add_edit_button = QPushButton()
		self.database = database

		self.stackedLayout = QStackedLayout()
		self.mainLayout = QVBoxLayout()
		self.topLayout = QHBoxLayout()
		
		self.setWindowTitle(" ")
		self.setWindowIcon(QIcon("WindowIcon.png"))
		
		self.memberLayoutWidget = AddEditMemberTableWidget()
		self.paymentLayoutWidget = AddEditPaymentTableWidget()
		self.regimeLayoutWidget = AddEditRegimeTableWidget()
		self.exerciseLayoutWidget = AddEditExerciseTableWidget()
		self.stackedLayout.addWidget(self.memberLayoutWidget)
		self.stackedLayout.addWidget(self.paymentLayoutWidget)
		self.stackedLayout.addWidget(self.regimeLayoutWidget)
		self.stackedLayout.addWidget(self.exerciseLayoutWidget)
		
		self.topLayout.addWidget(self.table_combo_box)
		self.topLayout.addWidget(self.add_edit_button)
		self.mainLayout.addLayout(self.topLayout)
		self.mainLayout.addLayout(self.stackedLayout)
		
		self.setLayout(self.mainLayout)
		
		#connections
		self.table_combo_box.currentIndexChanged.connect(self.updateTable)#when the comboboxes currently selected table is changed the updateTable method is run
		
		
	def updateTable(self,index):
                #method for chaning the widget based on the table selected in the combobox
		self.stackedLayout.setCurrentIndex(index)
		
	
		
		


		
