#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import json

def translate( input_str ): 
  #  open file and read appid and secretKey
  with open('baidu_credential.txt', 'r') as f:
    my_appid = f.readline().rstrip()
    my_secretKey= f.readline().rstrip()
  f.close() 

  appid = my_appid 
  secretKey = my_secretKey

 
  httpClient = None
  myurl = '/api/trans/vip/translate'

  # Note: q is the input string
  q = input_str

  fromLang = 'en'
  toLang = 'zh'
  salt = random.randint(32768, 65536)

  sign = appid+q+str(salt)+secretKey
  m1 = md5.new()
  m1.update(sign)
  sign = m1.hexdigest()
  myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

  try:
      httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
      httpClient.request('GET', myurl)

      #response是HTTPResponse对象
      response = httpClient.getresponse()
      # print response.read()
      # return json format file
      dct = json.loads(response.read())
      zn = dct['trans_result'][0]['dst'].encode('utf-8')
      return zn
  except Exception, e:
      print e
  finally:
      if httpClient:
          httpClient.close()
