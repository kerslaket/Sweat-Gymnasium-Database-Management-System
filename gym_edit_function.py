import sqlite3

def editMember(database,items,memberID):
	#function for editing items in the member table
	con = sqlite3.connect(database)
	
	with con:
		
		sql = "UPDATE Members SET "+items+" WHERE MemberID = "+memberID
		cur = con.cursor()
		cur.execute(sql)
			
def editPayment(database,items,memberID,paymentDate):
	#function for editing items in the payment table
	con = sqlite3.connect(database)
	
	with con:
		sql = "UPDATE Payments SET "+items+" WHERE MemberID="+memberID+" AND PaymentDate = "+paymentDate
		cur = con.cursor()
		cur.execute(sql)
		
def editRegime(database,items,memberID,exerciseID):
	#function for editing items in the regimetable
	con = sqlite3.connect(database)
	
	with con:
		sql = "UPDATE Regime SET "+items+" WHERE MemberID = "+memberID+" AND ExerciseID = "+exerciseID
		cur = con.cursor()
		cur.execute(sql)
		
def editExercise(database,items,exerciseID):
	#function for editing items in the exercise table
	con = sqlite3.connect(database)
	
	with con:
		sql = "UPDATE Exercise SET "+items+"WHERE EXERCISEID = "+exerciseID
		cur = con.cursor()
		cur.execute(sql)
		
