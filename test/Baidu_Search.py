#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
#from selenium.common.exceptions import
from selenium.webdriver.support.ui import WebDriverWait   #available since
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import  Options

from time import sleep

import os,time

driver=webdriver.Chrome()
print("加载驱动完成..")
driver.get("http://www.baidu.com") #加载页面
print("加载页面完成..")

time.sleep(1)

#方法一
try:
    assert("百度一下") in driver.title
    print("Assert baidu title pass.")
except Exception as e:
    print("Assert baidu title fail.",format(e))

#driver.maximize_window() #浏览器全屏显示
 
print("最大化页面窗口完成..")
driver.find_element_by_name("wd").send_keys("今日头条")   #Find the query box并输入内容
time.sleep(3)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("pyse自动化测试")
#driver.type("//*[@id='kw']","pyse自动化测试")
driver.find_element_by_id("su").send_keys(Keys.ENTER)
#driver.click("//*[@id='su']")
#elem.send_keys(u"今日头条" + Keys.RETURN)中的Keys.return是什么？？
#Keys.Return是什么？？？用firefox驱动实现不了为什么？google为什么不需要按百度一下就跳转到新的页面了？？
#elem.submit()  提交表单方法

print("输入搜索关键字...")
#driver.quit()  #关闭打开的浏览器
#print("关闭浏览器成功")
time.sleep(1)  #Let the page load,will be added to the API



#也可定位登录按钮，通过enter（回车）代替click()
#driver.find_element_by_id("su").send_keys(Keys.ENTER)






