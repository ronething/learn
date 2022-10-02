# python 操作 redis

## [`redis-py`](https://github.com/andymccurdy/redis-py)

```python
# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: redis_1.py 
@time: 2019/01/10
@github: github.com/ronething 

Less is more.
"""

import redis

# 连接redis，加上decode_responses=True，写入的键值对中的value为str类型，
# 不加这个参数写入的则为字节类型。
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)

r.set("name", "redis")
print(r.get("name"))
```

## 使用 [`Flask-Redis`](https://github.com/underyx/flask-redis) 模块在 flask 中操作 redis 

```python
# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: flask-redis_1.py 
@time: 2019/01/10
@github: github.com/ronething 

Less is more.
"""

from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)

app.config["REDIS_URL"] = "redis://127.0.0.1:6379/0"

redis_store = FlaskRedis(app)


@app.route('/')
def index():
    return redis_store.get('name')


if __name__ == '__main__':
    app.run()
```
