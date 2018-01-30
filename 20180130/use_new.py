# -*- coding=utf-8 -*-
class SingleTon(object):
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        #super  调用父类的方法
        # print cls._instance
        return cls._instance[cls]


class MyClass(SingleTon):
    class_val = 22

    def __init__(self, val):
        self.val = val
    #普通的方法，第一个参数需要是self，它表示一个具体的实例本身。
    def obj_fun(self):
        print self.val, 'obj_fun'

    #如果用了staticmethod，那么就可以无视这个self，而将这个方法当成一个普通的函数使用
    @staticmethod
    def static_fun():
        print 'staticmethod'
    #对于classmethod，它的第一个参数不是self,cls，它表示这个类本身
    @classmethod
    def class_fun(cls):
        print cls.class_val, 'classmethod'


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)
    print a is b   # True
    print id(a), id(b)  # 4367665424 4367665424
    # 类型验证
    print type(a)  # <class '__main__.MyClass'>
    print type(b)  # <class '__main__.MyClass'>
