# Tmp

## 使用devapi作为缓存代理服务器

```
$ pip install devpi-server

$ devpi-server --host=0.0.0.0 --start    # 启动
...
starting background devpi-server at http://0.0.0.0:3141
...

$ devpi-server --host=0.0.0.0 stop       # 关闭
```

使用代理来安装
$ pip install -i http://localhost:3141/root/pypi tornado




