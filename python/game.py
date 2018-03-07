#usr/bin/env python3
#-*- coding=utf-8 -*-

def move(n,a,b,c):
	# if not isinstrace(n,(int)):
		# raise TypeError('bad operand type')
	if n<=0:
		print('n<=0该游戏无法玩耍')
	# elif n==1:
		# print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)