import sqlite3

def deleteQueryPrimaryKey(database,table,item,constraint):
        #method for deleting items from the Members or Exercise Tables as they have a primary key
	
	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		cur.execute("DELETE FROM "+table+" WHERE "+item+" = "+constraint)
		
def deleteQueryCompositeKey(database,table,item1,item2,constraint1,constraint2):
	#method for deleting items from the payments or regimes tables as they have composite keys
	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		sql = "DELETE FROM "+table+" WHERE "+item1+" = "+constraint1+" AND "+item2+" = "+constraint2
		print(sql)
		cur.execute(sql)
		
def deleteAll(database,table):
        #delete all items from any table
	con = sqlite3.connect(database)
	
	with con:
		
		cur = con.cursor()
		cur.execute("DELETE FROM "+table)
		
	
def getItems(database,table):
        #function to retrieve all the data from the tables 
	
	con = sqlite3.connect(database)
	
	with con:
	
		cur = con.cursor()
		cur.execute("SELECT * FROM "+table)
		
		results = cur.fetchall()
		items = []
		
		for count in range(len(results)):
			column = results[count]
			if table == "MEMBERS":
				items.append(str(column[0])+". "+str(column[1]))
			if table == "PAYMENTS":
				cur.execute("SELECT Name FROM MEMBERS WHERE MEMBERID="+str(column[0]))
				memberName = cur.fetchall()
				for part in memberName:
					items.append(str(column[0])+". "+str(part[0])+" - "+str(column[1]))
			if table == "REGIME":
				cur.execute("SELECT Name FROM MEMBERS WHERE MEMBERID="+str(column[0]))
				memberName = cur.fetchall()
				cur.execute("SELECT Name FROM EXERCISE WHERE EXERCISEID="+str(column[1]))
				exerciseName = cur.fetchall()
				name = ""
				exercise = ""
				for part in memberName:
					name = str(part[0])
				for part in exerciseName:
					exercise = str(part[0])
				items.append(str(column[0])+". "+name+" - "+str(column[1])+". "+exercise)
			if table == "EXERCISE":
				items.append(str(column[0])+". "+str(column[1]))
				
	return items
