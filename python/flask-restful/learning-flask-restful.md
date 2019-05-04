# Learning Flask Restful

## Pre

```shell
# 安装
pip install flask-restful
```

A simple example

```python
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
```

## Route

- 一个 `Resource` 可以设置多个路径

    `api.add_resource(HelloWorld, '/', '/hello')`

- endpoint

    `api.add_resource(Todo, '/todo/<int:todo_id>', endpoint='todo_ep')`

    endpint 的用处： `url_for(endpoint)`， 路由Map是 {url: endpoint}， 再由endpoint找对对应的视力了函数。

## Views

- Argument Parsing

    get, post的参数都可以如下得到； 参数不符合时，返回 `{'status': 400, 'message': 'foo cannot be converted to int'}`

    ```python
    parser = reqparse.RequestParser()
    parser.add_argument('rate', type=int, help='Rate to charge for this resource')
    args = parser.parse_args()  # strict=True， 有多余的参数时，返回失败
    ```

    By default, the RequestParser tries to parse values from `flask.Request.values`, and `flask.Request.json`.

    ```python
    # Look only in the POST body
    parser.add_argument('name', type=int, location='form')

    # Look only in the querystring
    parser.add_argument('PageSize', type=int, location='args')

    # From the request headers
    parser.add_argument('User-Agent', location='headers')

    # From http cookies
    parser.add_argument('session_id', location='cookies')

    # From file uploads
    parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')
    ```

    `{error_msg}`, that will be replaced with the string representation of the type error. `help='Bad choice: {error_msg}'`

- data, http_code, headers

    ```python
    class Todo1(Resource):
        def get(self):
            # Default to 200 OK
            return {'task': 'Hello world'}

    class Todo2(Resource):
        def get(self):
            # Set the response code to 201
            return {'task': 'Hello world'}, 201

    class Todo3(Resource):
        def get(self):
            # Set the response code to 201 and return custom headers
            return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}
    ```