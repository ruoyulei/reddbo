import demo
import urllib
import json
import httplib
import requests

q = "To be or not to be, that is the question."
result = demo.baidu_tranlate(q)

dct = json.loads(result)

print dct['trans_result']
