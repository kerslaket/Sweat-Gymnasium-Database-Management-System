from PyQt4.QtGui import *
from gym_add_function import *
from gym_edit_function import *

class AddEditMemberTableWidget(QWidget):
	"""This class creates the widget for the members table in the add and edit dialog boxes"""
	
	def __init__(self):
		super().__init__()
		
		#create widgets
		
		self.lineEdits = {}
		
		for count in range(13):
			self.lineEdits["self.enter_text {0}".format(count)] = QLineEdit("")#creates 13 QLineEdits, 1 for each column in the table
		self.memberID_Label = QLabel("MemberID")
		self.name_Label = QLabel("Name")
		self.address_Label = QLabel("Address")
		self.telephone_number_Label = QLabel("Telephone Number")
		self.membership_type_Label = QLabel("Membership Type")
		self.induction_date_Label = QLabel("Induction Date")
		self.join_date_Label = QLabel("Join Date")
		self.how_paid_Label = QLabel("How Paid")
		self.amount_Label = QLabel("Amount")
		self.registration_fee_Label = QLabel("Registration Fee")
		self.registration_date_Label = QLabel("Registration Date")
		self.payment_type_Label = QLabel("Payment Type")
		self.comments_Label = QLabel("Comments")
		
		#create member layout
		
		self.mainMemberLayout = QVBoxLayout()
		self.memberContentLayout = QHBoxLayout()
		self.memberLabelLayout = QVBoxLayout()
		self.memberInputLayout = QVBoxLayout()
		
		self.memberLabelLayout.addWidget(self.memberID_Label)
		self.memberLabelLayout.addWidget(self.name_Label)
		self.memberLabelLayout.addWidget(self.address_Label)
		self.memberLabelLayout.addWidget(self.telephone_number_Label)
		self.memberLabelLayout.addWidget(self.membership_type_Label)
		self.memberLabelLayout.addWidget(self.induction_date_Label)
		self.memberLabelLayout.addWidget(self.join_date_Label)
		self.memberLabelLayout.addWidget(self.how_paid_Label)
		self.memberLabelLayout.addWidget(self.amount_Label)
		self.memberLabelLayout.addWidget(self.registration_fee_Label)
		self.memberLabelLayout.addWidget(self.registration_date_Label)
		self.memberLabelLayout.addWidget(self.payment_type_Label)
		self.memberLabelLayout.addWidget(self.comments_Label)
		for count in range(13):
			self.memberInputLayout.addWidget(self.lineEdits["self.enter_text {0}".format(count)])#adds each QLineEdit to the layout
		
		self.memberContentLayout.addLayout(self.memberLabelLayout)
		self.memberContentLayout.addLayout(self.memberInputLayout)
		self.mainMemberLayout.addLayout(self.memberContentLayout)

		self.setLayout(self.mainMemberLayout)
		
	def addMemberItems(self,database):
                #method for adding items to the member table
		addMember(database,self.lineEdits["self.enter_text 0"].text(),self.lineEdits["self.enter_text 1"].text(),self.lineEdits["self.enter_text 2"].text(),self.lineEdits["self.enter_text 3"].text(),self.lineEdits["self.enter_text 4"].text(),self.lineEdits["self.enter_text 5"].text(),self.lineEdits["self.enter_text 6"].text(),self.lineEdits["self.enter_text 7"].text(),self.lineEdits["self.enter_text 8"].text(),self.lineEdits["self.enter_text 9"].text(),self.lineEdits["self.enter_text 10"].text(),self.lineEdits["self.enter_text 11"].text(),self.lineEdits["self.enter_text 12"].text())
		
	def editMemberItems(self,database):
                #method for editting items in the member table
		columns = ["Name","Address","TelephoneNumber","MembershipType","InductionDate","JoinDate","HowPaid","Amount","RegistrationFee","RegistrationDate","PaymentType","Comments"]
		items = ""
		for count in range(1,12):
			if self.lineEdits["self.enter_text {0}".format(count)].text() != "":
				if count == 1 or 2 or 3 or 4 or 8 or 11 or 12:
					items +=(columns[count-1] + "='" + self.lineEdits["self.enter_text {0}".format(count)].text() + "' ,")
				else:
					items +=(columns[count-1] + "=" + self.lineEdits["self.enter_text {0}".format(count)].text() + " ,")
		items = items[:-1]
		
		editMember(database,items,self.lineEdits["self.enter_text 0"].text())
		
		
		
		
