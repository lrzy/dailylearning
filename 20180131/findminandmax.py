# -*- coding=utf-8 -*-
"""
    使用迭代的方式查询最大值和最小值
"""
from collections import Iterable

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

def findMinAndMax(L):
    """
        使用迭代的方式查询最大值和最小值
        
        :param L:输入的可迭代类型的对象
        
        :return :(最小值,最大值)
    """
    if not isinstance(L,Iterable):
        return False,u"非可迭代类型"
    if not  bool(L):
        return (None,None)
    #实际使用
    #return (min(L),max(L))
    nmax=L[0]
    nmin=L[0]
    for d in L:
        if nmax<d:
            nmax=d
        if nmin>d:
            nmin=d
    return (nmin,nmax)
        

if __name__ == '__main__':
    if findMinAndMax([]) != (None, None):
        print 1
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print 2
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print 3
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
