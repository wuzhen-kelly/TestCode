# -*- coding:utf-8 -*-
import urllib
from urllib.parse  import urlencode
from urllib.request import Request,urlopen
url= "http://xapi.kybyun.com/usr/login"
data={}
data["appchg"]="AppStore"
data["apptype"]="21"
data["appver"]="2.1.3.1"
data["email"]="mushishi01"
data["isbind"]="0"
data["password"]="111111"
data["sysdev"]="iPhone 6 Plus"
data["sysver"]="9.3"
data["uuid"]="6ff7563dbd47c8077905c3920bc0d8b3"
#数据编码以及赋值
data=urllib.parse.urlencode(data).encode(encoding='UTF8')
req = urllib.request.Request(url,data)
#打开地址并且赋值给变量
ResponseStr = urllib.request.urlopen(req)
#读取获得的值
ResponseStr = ResponseStr.read()
#打印
print(ResponseStr )