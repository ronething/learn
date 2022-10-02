# -*- coding:utf-8 _*-
""" 
@author: ronething 
@file: Redirects and Errors.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import abort, redirect, url_for, Flask

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login')), 200


@app.route('/login')
def login():
    abort(401)
    print("this_is_never_executed")


@app.errorhandler(401)
def error(error):
    return "401 error", 401


if __name__ == '__main__':
    app.run(debug=True)
