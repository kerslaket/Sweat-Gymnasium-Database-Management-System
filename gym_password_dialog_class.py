from PyQt4.QtGui import *

class PasswordDialog(QDialog):
	"""This class creates a dialog box for a password"""

	def __init__(self):
		super().__init__()

		#create widgets
		self.password_lineEdit = QLineEdit()
		self.password_lineEdit.setPlaceholderText("Password")
		self.password_lineEdit.setEchoMode(QLineEdit.Password)
		self.enterButton = QPushButton("Enter Password")
		self.closeButton = QPushButton("Close")

		#create and set layout
		self.layoutMain = QVBoxLayout()
		self.layoutHorizontal = QHBoxLayout()
		self.layoutMain.addWidget(self.password_lineEdit)
		self.layoutHorizontal.addWidget(self.enterButton)
		self.layoutHorizontal.addWidget(self.closeButton)
		self.layoutMain.addLayout(self.layoutHorizontal)
		self.setLayout(self.layoutMain)
		self.setWindowTitle("Password")
		self.setWindowIcon(QIcon("WindowIcon.png"))

		#connections
		self.enterButton.clicked.connect(self.close)
		
	def close_method(self):
                #method for returning the entered password to check if it is correct by the main program file
                return self.password_lineEdit.text()
		
