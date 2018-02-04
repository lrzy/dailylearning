# -*- coding=utf-8 -*-
"""
    测试map函数
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

def map1(x1):
    return x1*x1+1

def test_map():
    """
        测试map 函数的功能
    """
    a=map(map1,[1,2,3,4,5,6])
    for d in a:
        print d

if __name__ == '__main__':
    test_map()
