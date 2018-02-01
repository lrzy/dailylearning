# -*- coding=utf-8 -*-
"""
    使用迭代的方式查询最大值和最小值
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import click

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

"""
default: 设置命令行参数的默认值
help: 参数说明
type: 参数类型，可以是 string, int, float 等
prompt: 当在命令行中没有输入相应的参数时，会根据 prompt 提示用户输入
nargs: 指定命令行参数接收的值的个数
is_flag:当slash(/，斜杠)在参数中的时候，需要打开为True
"""
@click.command()
@click.option('--param1', default=1, help='参数一')
@click.option('--param2', default=2, help='参数2')
@click.option('-p3', help='参数3')
def test_click(**options):
    """
        测试命令行工具类
        
    """
    print options

if __name__ == '__main__':
    test_click()
