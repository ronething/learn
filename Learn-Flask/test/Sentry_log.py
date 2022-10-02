# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: Sentry_log.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import Flask

from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config.from_object('test.setting')
app.secret_key = "别说了"

sentry = Sentry(app, dsn=app.config["DSN"])


@app.route('/ep/')
def ep():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
