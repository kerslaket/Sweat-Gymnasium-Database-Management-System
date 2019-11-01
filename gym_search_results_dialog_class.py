from PyQt4.QtGui import *

class ResultsDialog(QDialog):
	"""This class creates the dialog window for the search results"""

	def __init__(self,searchResults):
		super().__init__()
		
		self.searchResults = searchResults

		#create widgets 
		self.results = QTextEdit()
 
		#create layout
		self.layout = QVBoxLayout()

		#add widgets to layout
		self.layout.addWidget(self.results)

		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("Results")
		self.setWindowIcon(QIcon("WindowIcon.png"))
		
		self.searchResults = searchResults
		self.populateResultsBox()
		
	def populateResultsBox(self):
                #method for populating the textEdit in the results dialog with the results from the search sql query
		self.string = ""
		for item in self.searchResults:
			self.string = ((self.string)+"\n\n"+str(item))
		self.results.setText(self.string)
