# -*- coding=utf-8 -*-
"""
    测试reduce函数
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

def reduce1(x,y):
    return x*x+y

def test_reduce():
    """
        测试reduce 函数的功能
    """
    a=reduce(reduce1,[1,2,3,4,5,6])
    print a

if __name__ == '__main__':
    test_reduce()
