# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: setup.py 
@time: 2019/01/14
@github: github.com/ronething 

Less is more.
"""

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
