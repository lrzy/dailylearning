# -*- coding=utf-8 -*-
"""
测试列表生成器
"""
__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

if __name__ == '__main__':
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [d.lower() for d in L1 if isinstance(d,str)]
    # 测试:
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')
