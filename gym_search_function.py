import sqlite3

def searchQuery(database,table,constraint):
        #function that searches the correct table in the database with the correct constraints
	
	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		if table == "MEMBERS":
			cur.execute("SELECT * FROM "+table+" WHERE MEMBERID Like "+constraint+" OR Name Like "+constraint+" OR Address Like "+constraint+" OR TelephoneNumber Like "+constraint+" OR MembershipType Like "+constraint+" OR InductionDate Like "+constraint+" OR JoinDate Like "+constraint+" OR HowPaid Like "+constraint+" OR Amount Like "+constraint+" OR RegistrationFee Like "+constraint+" OR RegistrationDate Like "+constraint+" OR PaymentType Like "+constraint+" OR Comments Like "+constraint)
			result = cur.fetchall()
			return result
		if table == "PAYMENTS":
			cur.execute("SELECT * FROM "+table+" WHERE MEMBERID Like "+constraint+" OR PaymentDate Like "+constraint+" OR HowMuch Like "+constraint+" OR Paid Like "+constraint)
			result = cur.fetchall()
			return result
		if table == "REGIME":
			cur.execute("SELECT * FROM "+table+" WHERE MEMBERID Like "+constraint+" OR EXERCISEID Like "+constraint+" OR SpecificDescription Like "+constraint+" OR StartDate Like "+constraint+" OR EndDate Like "+constraint)
			result = cur.fetchall()
			return result
		if table == "EXERCISE":
			cur.execute("SELECT * FROM "+table+" WHERE EXERCISEID Like "+constraint+" OR Name Like "+constraint+" OR Description Like "+constraint)		
			result = cur.fetchall()
			return result
			
