# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: URL Building.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


# 这里我们使用 test_request_context() 方法来尝试使用 url_for() 。
# test_request_context() 告诉 Flask 正在处理一个请求，而实际上也许我们正处在交互 Python shell 之中， 并没有真正的请求。
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
