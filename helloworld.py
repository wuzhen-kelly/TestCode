#！/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
age = int(input('Input your age: '))
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

print ('中文测试正常')

#range(101)就可以生成0-100的整数序列，计算0-100的整数之和
sum=0
for x in range(101):
	sum = sum + x
print('0-100的整数之和:',sum)


#计算1~100以内的所有偶数计算之和
sum=0 
n=100
while n>0:
	sum=sum+n
	n=n-2
print('1~100以内的所有偶数计算之和:',sum)

name=input('''please enter your name:''')   
print("你'好",name)
print('你\'好',name)
print("小'朋\"友s\\dfajd",name)
print(r'\\\t\n\\\\')
print('''你'好,你好\"你好
今天星期三，
明天星期四
''',name)
print(r'''line1
line2\t\t\n\tt\\\
line3''')

