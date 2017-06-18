#coding=utf8

import BaiduTranslator
import ImageGetter
import RedditContent
import urllib
import json
import httplib
import requests
import SQLConnector

def test_trans():
	q = "To be or not to be, that is the question."
	result = BaiduTranslator.translate(q)
	dct = json.loads(result)
	zn = dct['trans_result'][0]['dst']

	print zn.encode('utf-8')

def test_reddit():
	content = RedditContent.get_content()
	print len(content)
	print len(content[0])
	print len(content[1])
	print len(content[2])
	print len(content[3])
	for i in content[3]:
		print i[-4:]

def test_image():
	content = RedditContent.get_content()
	for u in content[3]:
		url = ImageGetter.get_image_url(u)
		print url

def test_get_images():
	content = RedditContent.get_content()
	ImageGetter.download_images(content[3])

def test_time():
	ts = time.time()
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print timestamp

	ys = datetime.datetime.today() - timedelta(days=1)
	oneday_ago = ys.strftime('%Y-%m-%d %H:%M:%S')
	print oneday_ago

def test_sqlconnector():
	info = "run test"
	SQLConnector.insert_into_db(info)

test_sqlconnector()
