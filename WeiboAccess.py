# -*- coding: utf-8 -*-
from weibo import APIClient
import urllib
import requests
import urllib2
import base64
import cookielib
import json
import time
import schedule

user_agent = (
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) '
	'Chrome/20.0.1132.57 Safari/536.11'
)

session = requests.session()
session.headers['User-Agent'] = user_agent
session.headers['Host'] = 'api.weibo.com'

global credentials,api_key, api_secret, callback_url, userid, password
with open('weibo_credential.json') as data_file:    
	credentials = json.load(data_file)
data_file.close()

api_key = credentials['api_key']
api_secret = credentials['api_secret']
callback_url = credentials['callback_url']
userid = credentials['userid']
password = credentials['password']

global client, referer_url
client =  APIClient(app_key=api_key, app_secret=api_secret, redirect_uri=callback_url)
referer_url = client.get_authorize_url()
print 'referer_url: %s' % referer_url

def post_weibo(text,pic_path):
 	# get access token & expire
	# token = client.request_access_token(code)
	#access_token = token.access_token
	access_token = credentials['access_token']
	print(access_token)
	#expires_in = token.expires_in
	expires_in = credentials['expires_in']
	print(expires_in)
	client.set_access_token(access_token, expires_in)

	# use .upload to post w/ pic
	# use .update to post w/o pic

	if pic_path == "":
		client.statuses.update.post(status=text)
	else:
		pic = open(pic_path,'rb')
		client.statuses.upload.post(status=text,pic=pic)
		pic.close()

	print('weibo posted')

if __name__ == '__main__':
	print "running..."
	#schedule.every(1).minutes.do(weibo_text)
	#while 1:
	#	schedule.run_pending()
	#	time.sleep(1)
	# weibo_text()
