# jimoky.cn Database Tester
# jimoky.cn不法盗号网站数据库请求压力测试
# Author:lwd-temp@Github
# Python 3,Requests
import requests
import random
import time
# 请求头
headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043128 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D PA QQ/7.0.0.3135 NetType/4G WebP/0.3.0 Pixel/1080','cookie': 'PHPSESSID=5cegv2n30s4nmlv8alcgiqqkj0'}
# 不法网站URL
url = 'http://jimoky.cn/action/qq_kj/2019.php'
# POST数据示例
# data = {'u':'qqnumber','p':'password','bianhao':'1'}
# POST
# postit = requests.post(url, headers=headers,data=data)
while True:
    qqnumber=random.randint(1000000000,9999999999)
    qqpw=random.randint(111111111111,999999999999999)
    data = {'u':str(qqnumber),'p':str(qqpw),'bianhao':'1'}
    print("POST数据:"+str(data))
    try:
        postit = requests.post(url, headers=headers, data=data)
    except (requests.exceptions.ConnectionError):
        print("ConnectionError")
        pass
    print(str(postit))
    time.sleep(1)