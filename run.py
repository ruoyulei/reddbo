#coding=utf8

import demo
import image
import reddit
import urllib
import json
import httplib
import requests

def test_trans():
	q = "To be or not to be, that is the question."
	result = demo.baidu_tranlate(q)

	dct = json.loads(result)

	zn = dct['trans_result'][0]['dst']

	print zn.encode('utf-8')

def test_img():
	link = "https://www.reddit.com/r/funny/comments/6dnvs0/the_correct_way_to_eat_fried_chicken/"
	i = image.get_image_link(link)
	print i

def test_reddit():
	r = reddit.get_reddit()
	print r[3][0]

def integ_test():
	r = reddit.get_reddit()
	for img in r[3]:
		print img

	'''
	url = str(r[3][2])
	print url
	image.get_image_link(url)
	'''

integ_test()