# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: instance folder_path.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    print(app.instance_path)
    # app.run(debug=True)
