# -*- coding=utf-8 -*-
#functools.wraps 则可以将原函数对象的指定属性复制给包装函数对象, 默认有 __module__、__name__、__doc__,或者通过参数选择
#具体还需要验证一下,在类上没有太大的差别，现在
from functools import wraps

def singleton(cls):
    instances = {}
    #print args,kw
    def _singleton(*args,**kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

def singleton_wraps(cls):
    instances = {}
    #print args,kw
    @wraps(cls)
    def _singleton(*args,**kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass(object):
    """普通装饰器"""
    a = 1
    def __init__(self,x):
        self.x = x

    def tt(self):
        print self.x

@singleton_wraps
class MyClass2(object):
    """普通使用wraps"""
    def __init__(self,x):
        self.x = x

    def tt(self):
        print self.x

if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)
    print a is b   # True
    print id(a), id(b)  # 4367665424 4367665424
    # 类型验证
    print type(a)  # <class '__main__.MyClass'>
    print type(b)  # <class '__main__.MyClass'>
    a2 = MyClass2('a2')
    print a2.__module__
    print a.__module__
    print dir(a)
