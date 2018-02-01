# -*- coding=utf-8 -*-
"""
    算法练习，二维数组中的查找
    二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import click

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

def find_integer_by_mat(mat,num):
    """
        判断一个值是否在二维数组中
        :param mat: [[]]
        :param num: int
        :return: bool
    """
    if not bool(mat):
        return False
    rows,cols = len(mat),len(mat[0])
    row,col = 0,cols-1
    while row<rows and cols>=0:
        if mat[row][col]==num:
            return True
        elif mat[row][col]<num:
            row+=1
        else:
            col-=1
    return False

def find_integer_by_fuc(mat,num):
    """
        判断一个值是否在二维数组中
        使用python语法
        :param mat: [[]]
        :param num: int
        :return: bool
    """
    for row in mat:
        if num in row:
            return True
    return False


def find_integer_by_comper(mat,num):
    """
        判断一个值是否在二维数组中
        使用python语法
        :param mat: [[]]
        :param num: int
        :return: bool
    """
    return bool([num for row in mat if num in row])

if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [2, 3, 6],
              [4, 6, 7]]
    num = 11
    print find_integer_by_mat(matrix, num)
    print find_integer_by_fuc(matrix, num)
    print find_integer_by_comper(matrix, num)
