# -*- coding:utf-8 -*-
# name=input('please enter your name:')
# print('hello{}'.format(name))
# print('hello'+name)
# print('hello',name)
# print('1024*768=',1024*768)
# print absolute value of an interger:
# a=int(input('please enter your lucky number:'))
# if a>=0:
	# print(a)
# else:
	# print(-a)
# print('I\'m \"OK\"!')  # 可以用转义字符\来转义
# print('I\'m ok')      #转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# print('I\'m learning\nPython.')
# print('\\\n\\')

# print(r'\\\t\\\n')   #Python还允许用r'表示'内部的字符串默认不转义
# # 用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
# print(''' \n\tline1    
# ...line2''
# ...line3''')
# # 多行字符串'''...'''还可以在前面加上r使用       
# print(r'''\t\n张三     
# \李四
# \\王五''')

# n = 123
# f =456.789
# s1 ='Hello, world'
# s2 ='Hello , \'Adam\''
# s3 =r'Hello,"Bart"'
# s4 =r'''Hello,
# Lisa!'''

# print(n,f,s1,s2,s3,s4,sep="\n")


# print('中文测试正常')
# s1=72
# s2=85
# r=(85-72)/72*100
# print('%2.1f %%'%r)



# L=[
	# ['Apple','Google','Microsoft'],
	# ['Java','Pyhton','Ruby','PHP'],
	# ['Adam','Bart','Lisa']
# ]

# print(L[0][0])
# print(L[1][1])
# print(L[2][2])


# age=3
# if age >=18:
	# print('your age is',age)
	# print('adult')
# elif age >=6:
	# print('teenager')
# else:
	# print('kid')
	
	
	
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
# age=20
# if age >=6:
	# print('teenager')
# elif age >=18:
	# print('adult')
# else:
	# print('kid')
	
	
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# x=0	
# if x:
	# print('True')
# else:
	# print('False')

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:	
# birth =int( input('birth:'))
# if birth < 2000:
	# print('00前')
# else:
	# print('00后')


# height = 1.75 
# weight = 80.5
# bmi=height/(weight**2)
# if bmi < 18.5:
	# print('过轻')
# elif bmi < 25:
	# print('正常')
# elif bmi < 28:
	# print('过重')
# elif bmi <32:
	# print('肥胖')
# else:
	# print('严重肥胖')

#循环:
# names = ['Michael','Bob','Tracy']
# for name in names:
	# print(name)

	
# sum = 0
# for x in range(101):
	# sum = sum + x
# print(sum)


# list(range(5))

# sum = 0
# n = 99
# while n > 0:
	# sum = sum + n
	# n = n - 2
# print(sum)


# L = ['Bart','Lisa','Adam']
# for name in L:
	# print('Hello,%s！'%name)

# break语句可以在循环过程中直接退出循环	
# n = 1
# while n <= 100:
	# if n >10:
		# break
	# print(n)
	# n = n + 1
# print('END')


# continue语句可以提前结束本轮循环，并直接开始下一轮循环。
# n = 1
# while n < 10:
	# n = 1
	# if n % 2 == 0:
		# continue
	# print(n)

	
# d = {'Michael':95, 'Bob':75, 'Tracy':85}
# print(d['Michael'])

# d['Adam'] =67
# print(d['Adam'])

# print(d['Thomas'])




# def my_abs(x):
	# if not isinstance(x,(int,float)):       #对参数类型做检查，只允许整数和浮点数类型的参数
		# raise TypeError('bad operand tyepe')
	# if x >= 0:
		# return x
	# else:
		# return -x
		
		
		
# import math

# def quadratic(a,b,c):
	# x=(b**2)-(4*a*c)
	# if not (isinstance (a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
		# raise TypeError('bad operand type')
	# if a==0:
		# return 'a不能为0'
	# if x>=0:
		# x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
		# x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
		# return x1,x2
	# elif x==0:
		# x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
		# return x1
	# else:
		# return '无解'



# print(quadratic(2,3,1))
# print(quadratic(1,3,-4))
# print(quadratic('a','b','c'))


# def power(x):
	# return x*x

	
# def power(x,n=2):
	# s=1
	# while n>0:
		# n=n-1
		# s=s*x
	# return s

# def enroll(name,gender,age=6,city='Beijing'):
	# print('name',name)
	# print('gender:',gender)
	# print('age:',age)
	# print('city:',city)
	
# def add_end(L=None):
	# if L is None:
		# L=[]
	# L.append('END')
	# return L

# def calc(numbers):
	# sum=0
	# for n in numbers:
		# sum=sum+n*n
	# return sum
	
# def person(name,age,**kw):
	# print('name:',name,'age:',age,'other:',kw)

	
def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)
	
















