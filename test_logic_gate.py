# -*- coding: utf-8 -*-
# !/usr/bin/env python
# File : test_logic_gate.py
# Date : 2019/4/19
# Author: leichao
# Email : leichaocn@163.com

"""简述功能.

详细描述.
"""

__filename__ = "test_logic_gate.py"
__date__ = 2019 / 4 / 19
__author__ = "leichao"
__email__ = "leichaocn@163.com"

import os
import sys

import pandas as pd
import numpy as np


class LogicGate:
    """逻辑门的基础类
    
    定义标签名变量、输出值变量、获取标签名的方法、获取输出值的方法
    
    Attributes:
    
    """
    
    def __init__(self, n):
        """"""
        self.label = n
        self.output = None
    
    def get_label(self):
        return self.label
    
    def get_output(self):
        """这是一个尚不存在的方法，被子类集成后会被重写。
        """
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """双引脚类，主要定义双引脚的接口
    
    定义引脚接口包括定义输入方法、定义实例变量。
    
    Attributes:
    
    """
    
    def __init__(self, n):
        """"""
        LogicGate.__init__(self, n)
        self.pin_a = None
        self.pin_b = None
    
    # def get_pin_a(self):
    #     return int(
    #         input('Please enter pin a input for gate '
    #               + self.get_label()
    #               + '-->')
    #     )
    
    #  使用连接器后的升级版本
    def get_pin_a(self):
        if self.pin_a is None:
            return int(
                input('Please enter pin a input for gate '
                      + self.get_label()
                      + ' -->')
            )
        else:
            # 不为空，说明被连接器对象占据了
            # 所以，获得这个逻辑门针脚的前一个逻辑门的输出
            return self.pin_a.get_from().get_output()
    
    # def get_pin_b(self):
    #     return int(
    #         input('Please enter pin b input for gate '
    #               + self.get_label()
    #               + '-->')
    #     )
    
    #  使用连接器后的升级版本
    def get_pin_b(self):
        if self.pin_b is None:
            return int(
                input('Please enter pin b input for gate '
                      + self.get_label()
                      + ' -->')
            )
        else:
            # 不为空，说明被连接器对象占据了
            # 所以，获得这个逻辑门针脚的前一个逻辑门的输出
            return self.pin_b.get_from().get_output()
    
    # 连接器需要的方法
    def set_next_pin(self, source):
        '''连接器需要的方法
        如果针脚为空，就把连接器source实例传给这个针脚
        '''
        if self.pin_a is None:
            # 如果a脚为空，就把连接器的
            self.pin_a = source
        else:
            if self.pin_b is None:
                self.pin_b = source
            else:
                raise RuntimeError('Error:NO EMPTY PINS')


class UnaryGate(LogicGate):
    """单引脚类，主要定义单引脚的接口
    
    定义引脚接口包括定义输入方法、定义实例变量。
    
    Attributes:
    
    """
    
    def __init__(self, n):
        """"""
        LogicGate.__init__(self, n)
        self.pin = None
    
    # def get_pin(self):
    #     return int(
    #         input('Please enter pin input for gate '
    #               + self.get_label()
    #               + '-->')
    #     )
    
    # 用了连接器后的升级版本
    def get_pin(self):
        if self.pin is None:
            return int(
                input('Please enter pin input for gate '
                      + self.get_label()
                      + ' -->')
            )
        else:
            # 不为空，说明被连接器对象占据了
            # 所以，获得这个逻辑门针脚的前一个逻辑门的输出
            return self.pin.get_from().get_output()
    
    # 连接器必须
    def set_next_pin(self, source):
        '''连接器需要的方法
        如果针脚为空，就把连接器source实例传给这个针脚
        '''
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError('Error:NO EMPTY PINS')


# 父亲是BinaryGate，爷爷是LogicGate。
class AndGate(BinaryGate):
    """这个类实现与门
    
    与门的核心逻辑
    
    Attributes:
    
    """
    
    def __init__(self, n):
        """"""
        BinaryGate.__init__(self, n)
    
    # 用于重写父类中的方法
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


# 父亲是BinaryGate，爷爷是LogicGate。
class OrGate(BinaryGate):
    """这个类实现或门

    详细描述

    Attributes:

    """
    
    def __init__(self, n):
        """"""
        BinaryGate.__init__(self, n)
    
    # 用于重写父类中的方法
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


# 父亲是BinaryGate，爷爷是LogicGate。
class NotGate(UnaryGate):
    """这个类实现非门

    详细描述

    Attributes:

    """
    
    def __init__(self, n):
        """"""
        UnaryGate.__init__(self, n)
    
    # 用于重写父类中的方法
    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector:
    """这个类是
    
    详细描述
    
    Attributes:
    
    """
    
    def __init__(self, fgate, tgate):
        """"""
        self.from_gate = fgate
        self.to_gate = tgate
        
        # 把本连接器实例送如下游逻辑门的set_next_pin方法中
        tgate.set_next_pin(self)
    
    def get_from(self):
        """获得这个连接器的上游的逻辑门"""
        return self.from_gate
    
    def get_to(self):
        """获得这个连接器的下游的逻辑门"""
        return self.to_gate


def main():
    """仅用于单元测试"""
    
    g1 = AndGate('G1')
    # print(g1.get_label())
    # print(g1.get_output())
    
    g2 = AndGate('G2')
    # print(g2.get_label())
    # print(g2.get_output())
    
    g3 = OrGate('G3')
    # print(g3.get_label())
    # print(g3.get_output())
    
    g4 = NotGate('G4')
    # print(g4.get_label())
    # print(g4.get_output())
    
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    # g4.get_output()
    print(g4.get_output())


if __name__ == '__main__':
    main()
