#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random

def baidu_tranlate( input_str ): 
  
  #  open file and read appid and secretKey
  with open('app_file.txt', 'r') as f:
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
      print response.read()
      # return json format file
      return response
  except Exception, e:
      print e
  finally:
      if httpClient:
          httpClient.close()
