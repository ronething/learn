# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: Cookies_1.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import make_response, Flask, render_template

app = Flask(__name__)


# Note that cookies are set on response objects.
# Since you normally just return strings from the view functions Flask will convert them into response objects for you.
# If you explicitly want to do that you can use the make_response() function and then modify it.
@app.route('/')
def index():
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'ronething')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
