#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# 'A-01:'

# import functools
# int2 = functools.partial(int,base=2)

# print('1000000=',int2('1000000'))
# print('1010101=',int2('1010101'))






# 'A-02:'
'a test module'

__author__='wuzhen'
# import sys

# def test():
	# args=sys.argv
	# if len(args)==1:
		# print('Hello,world!')
	# elif len(args)==2:
		# print('Hello,%s'%args[1])
	# else:
		# print('Too many arguments!')

# if __name__=='__main__':
	# test()
	
	
	
# def _private_1(name):
	# return 'hello,%s'%name
	
# def _priveate_2(name):
	# return 'hi,%s'%name
	
# def greeting(name):
	# if len(name)>3:
		# return _private_1(name)
	# else:
		# return _priveate_2(name)
		



		
# 'A-03:'


# std1={'name':'Michael','score':98}
# std2={'name':'Bob','score':81}
		
# class Student(object):
	# def __init__(self,name,score):
		# self.name=name
		# self.score=score
	# def print_score(self):
		# print('%s：%s'%(self.name,self.score))
		
		
# bart=Student('Bart Simpson',59)
# lisa=Student('lisa Simpson',87)
# bat.print_score()
# lisa.print_score()


# 'A-04:'
# class Student(object):
# 	def __init__(self,name,score):
# 		self.name=name
# 		self.score=score
# 	def print_score(self):
# 		print('%s:%s'%(self.name,self.score))

# bart=Student('Bart Simpson',59)
# bart.print_score()

class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
	 	print('%s:%s'%(self.__name,self.__score))
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score=score
		else:
			raise ValueError('bad score')
	def get_grade(self):
		if self.__score>=90:
			return 'A'
		elif  self.__score>=60:
			return 'B'
		else:
			return 'C'


lisa=Student('Lisa',99)
bart=Student('Bart',59)

bart.set_score(123)
print(bart.get_name(),bart.get_score())

# bart.age=8
# print(bart.age)

# bart.score=78
# print(bart.score)

# print(lisa.print_score(),lisa.get_grade())
# print(bart.print_score(),bart.get_grade())
