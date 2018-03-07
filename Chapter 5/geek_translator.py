#Geek Translator
#演示字典的用法

geek={"404":"clueless. From the web error message 404,meaning page not found.",
      "Googling":"searching the Internet for background information on a person.",
      "Keyboard Plaque":"the collection of debris found in computer keyboards.",
      "Link Rot":"the process by which web page links become obsolete.",
      "Percussive Maintenance":"the act of striking an electronic device to make it work.",
      "Uninstalled":"being fired. Especially popular during the dot-bomb era."}

#获取键值(1.有这个键存在则返回对应的值；2.直接获取一个不存在的键会报错)
print(geek["404"])
print(geek["Link Rot"])


#在获取值之前先用in运算符对键进行测试
if "Dancing Baloney" in geek:
    print("I know what Dancing Baloney is.")
else:
    print("I have no idea what Dancing Baloney is.")

    
#通过get()方法获取值
print(geek.get("Dancing Baloney","I have no idea."))


























