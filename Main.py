#Sweat Gymnasium Datbase Management System 9001

import sys

from gym_delete_dialog_class import *
from gym_print_dialog_class import *
from gym_search_dialog_class import *
from gym_edit_dialog_class import *
from gym_add_edit_dialog_class import *
from gym_add_dialog_class import *
from gym_about_dialog_class import *
from gym_password_dialog_class import *

from data_browser import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AppWindow(QMainWindow):
    """creates the main window"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gym Database Management System 9001")#sets the title for the window
        self.setWindowIcon(QIcon("Logo.png"))#sets the window icon

        #variable for database
        self.file = None
        
        #toolbars
        self.open_push_button = QPushButton("Open")#sets the main button for opening the Open GUI and function
        self.add_push_button = QPushButton("Add")#sets the main button for opening the Add GUI and function
        self.edit_push_button = QPushButton("Edit")#sets the main button for opening the Edit GUI and function
        self.delete_push_button = QPushButton("Delete")#sets the main button for opening the Delete GUI and function
        self.search_push_button = QPushButton("Search")#sets the main button for opening the Search GUI and function
        self.print_push_button = QPushButton("Print")#sets the main button for opening the Print GUI and function

        self.tab_bar = QTabWidget() #creates the widget to display the tables in a tabular layout
        
        self.tabs = {}#creates a dictionary for the table names/tab names
        self.tabNames = ['Members','Payments','Regime','Exercise']#The 4 tab/table names
        for count in range(4):
            self.tabs["{0}".format(self.tabNames[count])] = BrowseDataWidget()
            self.tab_bar.addTab(self.tabs["{0}".format(self.tabNames[count])],"{0}".format(self.tabNames[count]))
        #a for loop that creates a new tab and adds a "BrowseDataWidget" into each of them

        self.labels = {"Members":["MemberID","Name","Address","Telephone Number","Membership Type","Induction Date","Join Date","How Paid", "Amount", "RegistrationFee","Registration Date","PaymentType","Comments"],
                       "Payments":["MemberID","Payment Date","How Much","Paid"],
                       "Regime":["MemberID","ExerciseID","Specific Description", "Start Date", "End Date"],
                       "Exercise":["ExerciseID","Name","Description"]}
        #labels for the table headers that are referenced later in the program

        self.toolBar = QMenuBar()#creates a menu bar
        self.file_menu = self.toolBar.addMenu("File")#adds File option to the tool bar
        self.help_menu = self.toolBar.addMenu("Help")#adds Help option to the tool bar
        self.about = self.help_menu.addAction("About Gym Database Management System 9001")#adds options into the Help menu
        self.open_shortcut = self.file_menu.addAction("Open")#adds Open shortcut to the File menu
        self.add_shortcut = self.file_menu.addAction("Add")#adds Add shortcut to the File menu
        self.edit_shortcut = self.file_menu.addAction("Edit")#adds Edit shortcut to the File menu
        self.delete_shortcut = self.file_menu.addAction("Delete")#adds Delete shortcut to the File menu
        self.search_shortcut = self.file_menu.addAction("Search")#adds Search shortcut to the File menu
        self.print_shortcut = self.file_menu.addAction("Print")#adds Print shortcut to the File menu


        #layout
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QVBoxLayout()
        self.layout1.addWidget(self.open_push_button)
        self.layout1.addWidget(self.add_push_button)
        self.layout1.addWidget(self.edit_push_button)

        self.layout2.addWidget(self.delete_push_button)
        self.layout2.addWidget(self.search_push_button)
        self.layout2.addWidget(self.print_push_button)

        self.layout3.addWidget(self.tab_bar)
        self.layout3.addLayout(self.layout1)
        self.layout3.addLayout(self.layout2)

        self.mainWidget = QWidget()
        self.setMenuWidget(self.toolBar)
        self.mainWidget.setLayout(self.layout3)
        self.setCentralWidget(self.mainWidget)

        #connections
        #connections linking the main pushbuttons to their respective functions
        self.open_push_button.clicked.connect(self.open_file_menu)
        self.delete_push_button.clicked.connect(self.delete)
        self.print_push_button.clicked.connect(self.print_stuff)
        self.search_push_button.clicked.connect(self.search)
        self.edit_push_button.clicked.connect(self.edit)
        self.add_push_button.clicked.connect(self.add)
        self.about.triggered.connect(self.about_the_program)
        self.open_shortcut.triggered.connect(self.open_file_menu)
        self.add_shortcut.triggered.connect(self.add)
        self.edit_shortcut.triggered.connect(self.edit)
        self.delete_shortcut.triggered.connect(self.delete)
        self.search_shortcut.triggered.connect(self.search)
        self.print_shortcut.triggered.connect(self.print_stuff)
        #Keyboard Shortcuts for accessing the 6 main Functions
        self.connect(QShortcut(QKeySequence("Ctrl+o"), self), SIGNAL('activated()'), self.open_file_menu)
        self.connect(QShortcut(QKeySequence("Ctrl+a"), self), SIGNAL('activated()'), self.add)
        self.connect(QShortcut(QKeySequence("Ctrl+e"), self), SIGNAL('activated()'), self.edit)
        self.connect(QShortcut(QKeySequence("Ctrl+d"), self), SIGNAL('activated()'), self.delete)
        self.connect(QShortcut(QKeySequence("Ctrl+s"), self), SIGNAL('activated()'), self.search)
        self.connect(QShortcut(QKeySequence("Ctrl+p"), self), SIGNAL('activated()'), self.print_stuff)
        self.connect(QShortcut(QKeySequence("Ctrl+h"), self), SIGNAL('activated()'), self.about_the_program)



    def open_file_menu(self):
        self.file = QFileDialog.getOpenFileName(caption="Open Database",filter = "Database file (*.db *.dat)")#opens the windows folder tree allowing the user to select the database they want to open. File type restricted to .db or .dat files
        try: #Restricts the user to only opening correct database or a version of it 
            for item in self.tabNames:
                self.tabs["{0}".format(item)].UpdateTable(self.file)#loads selected database into tabs 
                self.tabs["{0}".format(item)].PopulateTable(item, self.labels[item])#populates the tabs with relevent information
        except NameError:
            return
        except sqlite3.OperationalError:
            return

        
    def delete(self):
        self.password("niel")#sets delete password to "niel" and opens the password function
        delete_dialog = DeleteDialog(self.file)#opens delete dialog
        delete_dialog.exec_()

    def print_stuff(self):
        print_dialog = PrintDialog(self.file)#opens print dialog
        print_dialog.exec_()
        
    def search(self):
        search_dialog = SearchDialog(self.file)#opens search dialog
        search_dialog.exec_()

    def edit(self):
        edit_dialog = EditDialog(self.file)#opens edit dialog
        edit_dialog.exec_()

    def add(self):
        add_dialog = AddDialog(self.file)#opens add dialog
        add_dialog.exec_()
        
    def about_the_program(self):
        about_dialog = AboutDialog()#opens about dialog
        about_dialog.exec_()

    def password(self,currentPass):
        passWord = ""#sets entered password to the wrong password 
        while passWord != currentPass:#while the correct password hasn't been entered
            password_dialog = PasswordDialog()#opens password dialog
            password_dialog.exec_()
            passWord = password_dialog.close_method()

        
def main():   
    gym_program = QApplication(sys.argv)#creates application
    gym_window = AppWindow()#creates Main Window
    gym_window.resize(700,600)#Locks inital window size
    password_dialog = gym_window.password("a")
    gym_window.show()
    gym_window.raise_()
    gym_program.exec_()
    

if __name__ == "__main__":
    main()
