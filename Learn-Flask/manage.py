# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: manage.py 
@time: 2019/01/11
@github: github.com/ronething 

Less is more.
"""

from flaskr import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)
