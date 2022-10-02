# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: Rendering Templates.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import Flask, render_template, Markup

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<string:name>/')
def hello(name=None):
    return render_template('hello.html', name=name)


# 在模板内部可以和访问 get_flashed_messages() 函数一样访问 request 、 session 和 g [1] 对象。

@app.route('/markup/')
def markup():
    return Markup("Hello <em>World</em>!")


if __name__ == '__main__':
    app.run(debug=True)
