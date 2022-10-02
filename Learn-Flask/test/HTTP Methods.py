# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: HTTP Methods.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import Flask, request, url_for

app = Flask(__name__)


# HEAD: 用于判断某个资源是否存在
# OPTIONS: 用于获取当前URL所支持的方法。
@app.route('/http', methods=["GET", "POST"])
def get_methods():
    if request.method == "POST":
        return "post method {}".format(url_for('get_methods'))
    elif request.method == "GET":
        return "get method {}".format(url_for('get_methods'))
    else:
        return 'none'


if __name__ == '__main__':
    app.run(debug=True)
