#coding=utf8

import demo
import urllib
import json
import httplib
import requests

q = "To be or not to be, that is the question."
result = demo.baidu_tranlate(q)

dct = json.loads(result)

zn = dct['trans_result'][0]['dst']

print zn.encode('utf-8')