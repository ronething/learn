# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: Variable Rules.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import Flask

app = Flask(__name__)

"""
Converter types:

string	(default) accepts any text without a slash
int	    accepts positive integers
float	accepts positive floating point values
path	like string but also accepts slashes
uuid	accepts UUID strings
"""


@app.route('/v/<float:number>/')
def float_view(number):
    return 'float number is {}'.format(number)


@app.route('/v/<uuid:number>/')
def uuid_view(number):
    return 'uuid number is {}'.format(number)


@app.route('/v/<path:subpath>/')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath is {}'.format(subpath)


if __name__ == '__main__':
    app.run(debug=True)
