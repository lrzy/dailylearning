# -*- coding=utf-8 -*-
"""
    了解collections模块
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import namedtuple,deque,defaultdict,Counter

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"


def test_namedtuple():
    """
        测试namedtuple
    """
    # namedtuple('名称', [属性list]):
    People=namedtuple('People',['name','age','sex'])
    p=People(u"zy",'18',u'男')
    print p
    print p.name
    for a in p:
        print a
    print isinstance(p,tuple)
    print isinstance(p,People)


def test_deque():
    """
        测试deque
    """
    l = deque(['a','b','c'])
    print l
    l.append('d')
    l.appendleft('e')
    print l
    print l.pop()
    print l.popleft()
    

def test_defalutdict():
    """
        测试defaultdict
    """
    d = defaultdict(dict)
    print d['q']
    d = defaultdict(lambda:0)
    print d['q']

def test_Counter():
    """
        测试Counter
    """
    c = Counter('programming')
    print c
    b = Counter([1,2,3,4,5,4,2,5,6,2,6,2])
    print b
    
if __name__ == '__main__':
    #test_namedtuple()
    #test_deque()
    #test_defalutdict()
    test_Counter()
