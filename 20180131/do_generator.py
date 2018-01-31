# -*- coding=utf-8 -*-
"""
    生成器：generator 测试
"""

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

def simple_generator():
    """
        测试创建一个generator
    """
    #range 和xrange:range返回一个list,xrange 返回的就是一个对象数值是使用时生成的类似一个生成器
    return (x for x in range(11) if x%2==0)

def fib(nmax):
    """
        斐波拉契数列
    """
    n, a, b = 0, 0, 1
    while n < nmax:
        yield b
        a, b = b, a + b
        n = n + 1
    yield 'done'

def triangles(NMAX=10):
    """
        杨辉三角
    """
    n=[1]
    lastn=[1]
    while len(n)<=NMAX:
        yield n
        n=[1]
        for index in xrange(len(lastn)-1):
            n.append(lastn[index]+lastn[index+1])
        n.append(1)
        lastn=n
        
    
    

if __name__ == '__main__':
    g1 = simple_generator()
    print g1
    print next(g1)
    for d in g1:
        print d
    for d in fib(6):
        print d
    for d in triangles():
        print d
    n = 0
    results = []
    for t in triangles():
        print(t)
        results.append(t)
        n = n + 1
        if n == 10:
            break
    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')
