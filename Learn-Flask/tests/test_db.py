# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: test_db.py 
@time: 2019/01/14
@github: github.com/ronething 

Less is more.
"""


def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
