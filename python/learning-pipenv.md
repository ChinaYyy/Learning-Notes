# pipenv

problem solved

- `pip` and `virtualenv` work together
- upgrade `requirements.txt`
- `pipenv graph`
- loading `.env` files

install

`sudo apt-get install python3-pip`

`$ pip3 install --user pipenv`

有必要， 添加pipenv到环境变量。`python -m site --user-base`的目录后追加`bin`

upgrade

`$ pip install --user --upgrade pipenv`

使用国内镜像

``` bash
$ vim Pipfile
url = "https://mirrors.aliyun.com/pypi/simple/"
```

## Useing

创建虚拟环境（指定版本)

- pipenv --two
- pipenv --three
- pipenv --python 2.7

安装模块

`$ pipenv install requests`

运行命令

`$ pipenv run python main.py`

激活、退出虚拟环境

`$ pipenv shell`

`$ exit`