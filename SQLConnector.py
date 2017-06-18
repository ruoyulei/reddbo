import MySQLdb as sql
import json
import datetime
from datetime import timedelta
import time

# Parameter: a string of post_id

def insert_into_db(post_id):
	login_info = []
	with open('db_credential.json') as data_file:
		login_info = json.load(data_file)
	data_file.close()

	db = sql.connect(host=login_info['host'],
			user=login_info['user'],
			passwd=login_info['passwd'],
			db=login_info['db'])

	timestamps = get_time()

	cur = db.cursor()

	cur.execute('SELECT * FROM succ WHERE pTime >= %s AND pTime < %s AND postid=%s',
		(timestamps[1],
		timestamps[0],
		post_id))

	fetched = cur.fetchall()

	if len(fetched) == 0:
		# can post
		try:
			cur.execute('INSERT INTO succ VALUES(%s,%s)',(post_id,timestamps[0]))
			db.commit()
			db.close()
			return True
		except:
			print "exception catched"
			db.rollback()
			db.close()
			return False
	else:
		# already posted in the last 24 hours. DO NOT post
		print post_id + " already posted"
		db.close()
		return False


# return: t[0] = current timestamp
#		  t[1] = one day ago timestamp
def get_time():
	t = []
	ts = time.time()
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	ys = datetime.datetime.today() - timedelta(days=1)
	oneday_ago = ys.strftime('%Y-%m-%d %H:%M:%S')

	t.append(timestamp)
	t.append(oneday_ago)
	
	return t
