# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: test_factory.py 
@time: 2019/01/14
@github: github.com/ronething 

Less is more.
"""

from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello/')
    assert response.data == b'Hello, World!'

