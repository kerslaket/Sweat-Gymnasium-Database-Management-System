import sqlite3

def addMember(database, memberID, name, address, telNumber, membershipType, inductionDate, joinDate, howPaid, amount, registrationDate, registrationFee, paymentType, comments):
	#function for adding items to the member table
	con = sqlite3.connect(database)
	
	with con:

		sql = "INSERT INTO Members (MemberID, Name, Address, TelephoneNumber, MembershipType, InductionDate, JoinDate, HowPaid, Amount, RegistrationDate, RegistrationFee, PaymentType, Comments) VALUES ('"+memberID+"','"+name+"','"+address+"','"+telNumber+"','"+membershipType+"','"+inductionDate+"','"+joinDate+"','"+howPaid+"','"+amount+"','"+registrationDate+"','"+registrationFee+"','"+paymentType+"','"+comments+"')"
		print(sql)		
		cur = con.cursor()
		cur.execute(sql)

		
def addPayment(database,memberID,paymentDate,howMuch,paid):
	#function for adding items to the payment table        
	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		cur.execute("INSERT INTO Payments (MemberID, PaymentDate, HowMuch, Paid) VALUES ("+memberID+",'"+paymentDate+"',"+howMuch+","+paid+")")

def addRegime(database,memberID,exerciseID,specificDescription,startDate,endDate):
	#function for adding items to the regime table
	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		cur.execute("INSERT INTO Regime(MemberID, ExerciseID, SpecificDescription, StartDate, EndDate) VALUES ("+memberID+","+exerciseID+",'"+specificDescription+"','"+startDate+"','"+endDate+"')")
		
def addExercise(database,exerciseID,name,description):
	#function for adding items to the exercise table
	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		cur.execute("INSERT INTO Exercise(ExerciseID, Name, Description) VALUES ("+exerciseID+",'"+name+"','"+description+"')")
		

		
		

		
