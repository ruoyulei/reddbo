import MySQLdb as sql

db = sql.connect(host='localhost',
		user='bot',
		passwd='ubuntu',
		db='reddboDB')

cur = db.cursor()

cur.execute('SELECT * FROM succ')

for row in cur.fetchall():
	print row[0]
	print row[1]

db.close()
