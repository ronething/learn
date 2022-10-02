# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: flash_message.py
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = "你滚啊"


@app.route('/flash/')
def flash_mes():
    flash("别吧")
    return render_template("hello.html")


if __name__ == '__main__':
    app.run(debug=True)
