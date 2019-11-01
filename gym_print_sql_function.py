import sqlite3

def getMemberInfo(database,memberID):
        #gets the items from the database for a member info printout
	
	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		cur.execute("SELECT * FROM MEMBERS WHERE MEMBERID = "+memberID)
		result = cur.fetchall()
		return result
		
def getInvoice(database,memberID):
        #gets the items from the database for a print out of an invoice

	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		cur.execute("SELECT * FROM PAYMENTS WHERE MEMBERID = "+memberID)
		result = cur.fetchall()
		cur.execute("SELECT Name FROM MEMBERS WHERE MEMBERID = "+memberID)
		name = cur.fetchall()
		
		return result,name
		
def getRegime(database,memberID):
        #gets the items from the database for an invoice printout

	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		cur.execute("SELECT * FROM REGIME WHERE MEMBERID = "+memberID)
		result = cur.fetchall()
		cur.execute("SELECT Name FROM MEMBERS WHERE MEMBERID = "+memberID)
		name = cur.fetchall()
		
		return result,name
