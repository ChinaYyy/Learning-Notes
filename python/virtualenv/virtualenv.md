# Virtualenv

## Questions

#### 普通用户安装

没有root权限

```
pip install django --user
```
会安装在 `~/.local` 目录下。

```
pip show django|grep Location
```