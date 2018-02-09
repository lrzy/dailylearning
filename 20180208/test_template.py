# -*- coding=utf-8 -*-
"""
    Jinja2 模板渲染
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask,render_template

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

app = Flask(__name__)
app.debug = True 

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html',name=name)



if __name__ == '__main__':
    app.run()

