from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gym_print_sql_function import *
from gym_delete_function import *

class PrintDialog(QDialog):
	"""This class creatres the dialog window for creating forms and printing them"""

	def __init__(self,database):
		super().__init__()
		
		self.database = database

		#create widgets
		self.form_combo_box = QComboBox()
		self.item_select_combo_box = QComboBox()
		self.print_push_button = QPushButton("Print")

		self.form_combo_box.addItem("Select Form")
		self.form_combo_box.addItem("Invoice")
		self.form_combo_box.addItem("Member Details")
		self.form_combo_box.addItem("Regime")


		#create layout
		self.layout = QVBoxLayout()

		#add widgets to layout
		self.layout.addWidget(self.form_combo_box)
		self.layout.addWidget(self.item_select_combo_box)
		self.layout.addWidget(self.print_push_button)

		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("Print")
		self.setWindowIcon(QIcon("Hugobells.png"))

		#connections
		self.form_combo_box.currentIndexChanged.connect(self.itemComboBoxPopulate)
		self.print_push_button.clicked.connect(self.printInfo)
		
	def printFunction(self,itemToPrint):
				#function that sends the textEdit to be printed and allows the user to select a printer through the print dialog
		dialog = QPrintDialog()
		if dialog.exec_() == QDialog.Accepted:
			itemToPrint.print_(dialog.printer())
		
	def generateMemberInfo(self):
				#method that creates the textEdit containg the correct information for a member info print out
		columns = ["MemberID","Name","Address","TelephoneNumber","MembershipType","InductionDate","JoinDate","HowPaid","Amount","RegistrationFee","RegistrationDate","PaymentType","Comments"]
		sep = "."
		info = getMemberInfo(self.database, str(self.item_select_combo_box.currentText()).split(sep,1)[0])
		infoToPrint = QTextEdit()
		infoString = ""
		for item in info:
			count = 0
			for piece in item:
				infoToPrint.setText(infoToPrint.toPlainText()+columns[count]+" : "+str(piece)+"\n")
				count += 1
		self.printFunction(infoToPrint)
		
	def generateInvoice(self):
				#method that creates the textEdit containg the correct information for a print out of an invoice
		columns = ["MemberID","Payment Date","How Much","Paid"]
		sep = "."
		info,name = getInvoice(self.database, str(self.item_select_combo_box.currentText()).split(sep,1)[0])
		infoToPrint = QTextEdit()
		for list in name:
			for word in name:
				for item in word:
					infoToPrint.setText("Member Name : "+str(item)+"\n\n")
		for item in info:
			count = 0
			for piece in item:
				infoToPrint.setText(infoToPrint.toPlainText()+columns[count]+" : "+str(piece)+"\n")
				count += 1
			infoToPrint.setText(infoToPrint.toPlainText()+"\n")
		self.printFunction(infoToPrint)
	
	def generateRegime(self):
				#method that creates the textEdit containg the correct information for a members regime print out
		columns = ["MemberID","ExerciseID","Description","Start Date","End Date"]
		sep = "."
		info,name = getRegime(self.database, str(self.item_select_combo_box.currentText()).split(sep,1)[0])
		infoToPrint = QTextEdit()
		for list in name:
			for word in name:
				for item in word:
					infoToPrint.setText("Member Name : "+str(item)+"\n\n")
		for item in info:
			count = 0
			for piece in item:
				infoToPrint.setText(infoToPrint.toPlainText()+columns[count]+" : "+str(piece)+"\n")
				count += 1
			infoToPrint.setText(infoToPrint.toPlainText()+"\n")
		self.printFunction(infoToPrint)
		
	def itemComboBoxPopulate(self):
		if self.form_combo_box.currentIndex() == 0:
			self.item_select_combo_box.clear()
			self.item_select_combo_box.addItem("Select Item")
		else:
			items = getItems(self.database, "MEMBERS")
			self.item_select_combo_box.clear()
			for count in range(len(items)):
				self.item_select_combo_box.addItem(items[count])

	def printInfo(self):
		if self.form_combo_box.currentIndex() == 1:
			self.generateInvoice()
		if self.form_combo_box.currentIndex() == 2:
			self.generateMemberInfo()
		if self.form_combo_box.currentIndex() == 3:
			self.generateRegime()

