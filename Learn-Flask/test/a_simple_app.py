# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: a_simple_app.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
