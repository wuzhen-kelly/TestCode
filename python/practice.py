#! usr/bin/env python3
#--*-- coding:utf-8 -*-

#递归函数 尾递归
def fact(n):
	return fact_iter(n,1)
	
def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)
	
#汉诺塔游戏
def move(n,a,b,c):
	if n==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
		
#使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable		
#isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator

#斐波拉契数列  -函数
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
	
#斐波拉契数列  -generator
def fib1(max):
	n,a,b=0,0,1
	while n<max:
		yield(b)
		a,b=b,a+b
		n=n+1
	return 'done'

#generator，捕获StopIteration错误
g=fib1(6)
while True:
	try:
		x=next(g)
		print('g：',x)
	except StopIteration as e:
		print('Generator return values:',e.value)
		break

#杨辉三角  -generator
def triangles():
	a=[1]
	while True:
		yield a
		a.append(0)
		a=[a[i-1]+a[i] for i in range(len(a))]
n=0
for t in triangles():
	print(t)
	n=n+1
	if n==10:
		break