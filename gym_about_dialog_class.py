from PyQt4.QtGui import *
from PyQt4.QtCore import *
import webbrowser

class AboutDialog(QDialog):
	"""This is the about page"""

	def __init__(self):
		super().__init__()

		#create widgets
		self.text = QTextEdit()
		self.text.setPlainText("Created By Toby Kerslake \n\n\n\n User Manual available for download below")
		self.text.setReadOnly(True)#set the textEdit so the user can't rewrite the text
		self.userManualButton = QPushButton("User Manual")
		
		#create layout
		self.layout = QVBoxLayout()


		#add widgets to layout

		self.layout.addWidget(self.text)
		self.layout.addWidget(self.userManualButton)


		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("About")
		self.setWindowIcon(QIcon("WindowIcon.png"))

		#connections
		self.userManualButton.clicked.connect(self.openUserManual)

	def openUserManual(self):
                #method that opens up the user manual inside the users default browser
		webbrowser.open('https://www.dropbox.com/s/61n4soosnvo1cnc/User%20Manual.docx?dl=0')
