# -*- coding: utf-8 -*-
# !/usr/bin/env python
# File : test_fraction.py
# Date : 2019/4/18
# Author: leichao
# Email : leichaocn@163.com

"""一个用于测试oop的入门代码。

通过定义一个分数类，介绍了如何以对象的方式表示加、减、等于。
"""

__filename__ = "test_fraction.py"
__date__ = 2019 / 4 / 18
__author__ = "leichao"
__email__ = "leichaocn@163.com"

import os
import sys

import pandas as pd
import numpy as np


def gcd(m, n):
    """获取两个数的最大公约数"""
    while m % n != 0:
        old_m = m
        old_n = n
        
        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    """这个类是
    
    详细描述
    
    Attributes:
    
    """
    
    def __init__(self, top, bottom):
        """"""
        self.num = top
        self.den = bottom
    
    # 显示功能
    def show(self):
        """显示功能"""
        print(self.num, '/', self.den)
    
    # 实现直接就可用print(x)来输出字符串，而不用show
    def __str__(self):
        """显示功能"""
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, other):
        """ """
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_den, new_num)
        return Fraction(new_num / common, new_den / common)
    
    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num == second_num


def main():
    """仅用于单元测试"""
    x = Fraction(3, 5)
    y = Fraction(1, 10)
    
    print(x)
    x.show()
    
    print(x + y)
    print(x == y)
    print(x == Fraction(60, 100))


if __name__ == '__main__':
    main()
