# -*- coding=utf-8 -*-
"""
    使用route() 装饰器把一个函数绑定到对应的 URL 上
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

app = Flask(__name__)
app.debug = True 

#然后，我们使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test2():
    return 'test2'

#测试变量规则
"""
 ——————————————————————————————————
|int 	|接受整数                  |
|float	|同 int ，但是接受浮点数   |
|path	|和默认的相似，但也接受斜线|
 ——————————————————————————————————
"""
@app.route('/age/<int:age>')
def inage(age):
    return str(age)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/name/<name>')
def name(name):
    return name


if __name__ == '__main__':
    app.run()

