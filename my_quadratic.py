#! /usr/bin/env python3
# -*- coding:utf-8 -*-


import math

def quadratic(a, b, c) :
    if not 	isinstance(a, (int, float)):    
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    '''
    对输入的数据类型进行检查，三个数不能同时检查，否则程序会报错！（血泪史。。。）
    '''
    if b**2 - 4 * a * c < 0:
        return '此方程无解'    # 返回值
    else:
        x1 =( - b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
        x2 =( - b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
        return x1, x2    # 返回值
