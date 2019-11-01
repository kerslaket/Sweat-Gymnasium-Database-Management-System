from PyQt4.QtGui import *
from gym_add_function import *
from gym_edit_function import *

class AddEditPaymentTableWidget(QWidget):
	"""This class creates the widget for the payment table in the add and edit dialog boxes"""
	
	def __init__(self):
		super().__init__()
		
		#create widgets
		
		self.lineEdits = {}
		
		for count in range(4):
			self.lineEdits["self.enter_text {0}".format(count)] = QLineEdit()#creates 4 QLineEdits, 1 for each column in the payments table
			
		self.memberID_Label = QLabel("MemberID")
		self.payment_date_Label = QLabel("Payment Date")
		self.how_much_Label = QLabel("How Much")
		self.paid_label = QLabel("Paid")
		
		# create payment layout
		
		self.paymentLayout = QVBoxLayout()
		self.paymentContentLayout = QHBoxLayout()
		self.paymentLabelLayout = QVBoxLayout()
		self.paymentInputLayout = QVBoxLayout()
		
		self.paymentLabelLayout.addWidget(self.memberID_Label)
		self.paymentLabelLayout.addWidget(self.payment_date_Label)
		self.paymentLabelLayout.addWidget(self.how_much_Label)
		self.paymentLabelLayout.addWidget(self.paid_label)
		for count in range(4):
			self.paymentInputLayout.addWidget(self.lineEdits["self.enter_text {0}".format(count)])#adds all the QLineEdits to the layout
		
		self.paymentContentLayout.addLayout(self.paymentLabelLayout)
		self.paymentContentLayout.addLayout(self.paymentInputLayout)
		self.paymentLayout.addLayout(self.paymentContentLayout)
		
		self.setLayout(self.paymentLayout)
		
	def addPaymentItems(self, database):
                #method for adding items to the payment table
		addPayment(database,self.lineEdits["self.enter_text 0"].text(),self.lineEdits["self.enter_text 1"].text(),self.lineEdits["self.enter_text 2"].text(),self.lineEdits["self.enter_text 3"].text())

	def editPaymentItems(self,database):
                #method for editing items in the payment table
		columns = ["HowMuch","Paid"]
		items = ""
		for count in range(2,4):
			print(count)
			if self.lineEdits["self.enter_text {0}".format(count)].text() != "":
				items +=(columns[count-2] + "=" + self.lineEdits["self.enter_text {0}".format(count)].text() + " ,")
		items = items[:-1]
		
		editPayment(database,items,self.lineEdits["self.enter_text 0"].text(),self.lineEdits["self.enter_text 1"].text())
