# -*- coding=utf-8 -*-
"""
    测试类的生命周期
"""

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

class LifeCycle(object):
    """
    测试类的生命周期
    """
    def __new__(cls, *args, **kwargs):
        print "new"
        return super(LifeCycle, cls).__new__(cls)

    def __init__(self):
        print "init"

    
    def __del__(self):
        
        print "del"


if __name__ == '__main__':
    LifeCycle()
