# learn-flask

## Static Files

Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, but during development Flask can do that as well. Just create a folder called static in your package or next to your module and it will be available at /static on the application.

To generate URLs for static files, use the special 'static' endpoint name:

`url_for('static', filename='style.css')`

The file has to be stored on the filesystem as static/style.css.

## 渲染模板

自动转义默认开启。因此，如果 name 包含 HTML ，那么会被自动转义。如果你可以 信任某个变量，且知道它是安全的 HTML （例如变量来自一个把 wiki 标记转换为 HTML 的模块），那么可以使用 Markup 类把它标记为安全的，或者在模板 中使用 |safe 过滤器。

## 请求对象

```python
searchword = request.args.get('key', '')
```

用户可能会改变 URL 导致出现一个 400 请求出错页面，这样降低了用户友好度。因此， 我们推荐使用 get 或通过捕捉 KeyError 来访问 URL 参数。

## Error

By default a black and white error page is shown for each error code. If you want to customize the error page, you can use the errorhandler() decorator:

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

Note the 404 after the render_template() call. This tells Flask that the status code of that page should be 404 which means not found. By default 200 is assumed which translates to: all went well.

大概意思是 你懂的。后面的404数字挺重要的。你指定什么 🔙返回的状态码就是什么。记住这一点比较重要。

```python
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
You can also register handlers for arbitrary exceptions:

@app.errorhandler(DatabaseError)
def special_exception_handler(error):
    return 'Database connection failed', 500
```

## Response

If view looked like this and you want to add a new header:

```python
def index():
    return render_template('index.html', foo=42)
```

You can now do something like this:

```python
def index():
    response = make_response(render_template('index.html', foo=42))
    response.headers['X-Parachutes'] = 'parachutes are cool'
    return response
```

> 如何生成一个好的密钥

生成随机数的关键在于一个好的随机种子，因此一个好的密钥应当有足够的随机性。 操作系统可以有多种方式基于密码随机生成器来生成随机数据。使用下面的命令 可以快捷的为 Flask.secret_key （ 或者 SECRET_KEY ）生成值:

```sh
$ python -c 'import os; print(os.urandom(16))'
b'_5#y2L"F4Q8z\n\xec]/'
```

## 必须在服务端做好客户端传过来数据的验证

It’s important to always fully validate the data on the server, even if the client does some validation as well.

## jinja2 for 循环 `loop` 用法

http://jinja.pocoo.org/docs/2.10/templates/#for

## 测试覆盖

好好学📖