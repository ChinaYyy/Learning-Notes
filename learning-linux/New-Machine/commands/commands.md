# Commands

## Summary

- 目录命令

  - ls
  - cd
  - pwd
  - mkdir
  - rmdir
  - tree

- 文件管理

  - touch
  - stat
  - file
  - rm
  - cp
  - mv
  - nano

- 日期时间

  - date
  - clock
  - hwclock
  - cal

- 查看文本

  - cat
  - tac
  - more
  - less
  - head
  - tail

## Basic Commands

### ls

- `-l` long
- `-d` 只显示目录属性，不显示目录下文件
- `-i` inode索引号
- `-t` 时间排序逆序
- `-r` 逆序
- `-R` 递归显示子目录内容

### cd

- `cd` 不带参数， 进入家目录
- `cd -` 与上个命令来回切换

### man

`man COMMAND`

man 命令分等级章节， 默认显示存在的最小章节

- `1` 用户命令
- `2` 系统调用
- `3` 库命令
- `4` 特殊文件（设备文件）
- `5` 文件格式（配置文件的语法）
- `6` 游戏
- `7` 杂项
- `8` 管理员命令（/sbin， /usr/sbin, /usr/local/sbin）

`whatis COMMAND` 可以查看命令有哪些章节， 再使用 `man NUM COMMAND` 查看指定章节

```shell
$ whatis passwd

passwd (5)           - 密码文件
passwd (1)           - 更改用户密码
passwd (1ssl)        - compute password hashes

$ man 5 passwd
```

- `<>` 必选
- `[]` 可选
- `...` 可出现多次
- `{}` 分组

- `NAME` 命令名称及功能简要说明
- `SYNOPSIS` 用法说明， 包括可用的选项
- `DESCRIPTION` 详尽说明
- `OPTIONS` 每个选项的意义
- `OPTIONS` 每个选项的意义
- `FILES` 相关的配置文件

`info COMMAND` 在线搜索文档， 比man要详尽

`/usr/share/doc` 文档

### date

```shell
$ date +"This year is %Y. %nToday is %d."
This year is 2019.
Today is 08.
```

`date` 是系统时间(软件时间)
`hwclock` 硬件时间

### copy

`cp SRC DEST`

- `-r`
- `-f`
- `-p`
- `-a` 归档复制， 常用于备份
