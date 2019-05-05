# Tmp

## 使用devapi作为缓存代理服务器

```plain
$ pip install devpi-server

$ devpi-server --host=0.0.0.0 --start    # 启动
...
starting background devpi-server at http://0.0.0.0:3141
...

$ devpi-server --host=0.0.0.0 stop       # 关闭
```

使用代理来安装
$ pip install -i http://localhost:3141/root/pypi tornado

## 偏函数 partical

```
from functools import partial
>>> basetwo = partial(int, base=2)
>>> basetwo('10010')
18
```

```
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```

## no mudule queue

python2.7 安装了__future__的，queue和Queue都可以用，没有安装的，只能用Queue

python3 是queue

## str

### str.rpartition

```
>>> filepath = 'ab.c.txt'
>>> filepath.rpartition('.')
('ab.c', '.', 'txt')
```

## Code

`# noqa` 代码检查该行时，忽略掉任何警告

```pythton
App = Celery  # noqa: E305 XXX compat
```