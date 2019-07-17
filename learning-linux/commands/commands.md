# Commands

常用命令及bash特性

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

- bash特性

  - history
  - alias

- 查看文本

  - cat
  - tac
  - more
  - less
  - head
  - tail

- 文本处理

  - cut
  - sort
  - uniq
  - wc
  - sed
  - awk
  - grep

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

### history

- `history n` 显示最近使用的n行命令
- `!n` 执行第n行命令
- `！-n` 执行倒数第n行命令, ex. 执行上一条命令 `!-1`
- `!!` 执行上一条命令
- `!string` 执行最近以指定string开头的命令
- `!$` 上一条命令的最后一个参数, 也可以按下Esc键后，再按.键

    ```shell
    cat /etc/fstab /etc/issue

    cat !$
    # 相当于cat /etc/issue
    ```

### alias

- `help alias` alias 文档
- `alias` 显示所有的别名
- `alias alias_name=COMMAND`
- `ualias alias_name` 取消别名

### copy

`cp SRC DEST`

- `-r`
- `-f`
- `-p`
- `-a` 归档复制， 常用于备份

## 文本处理

### cut

- `-d` 指定分隔符，默认为`Tab`
- `-f` 选择第一列的字段值

`cut -d ',' -f 1,3 SOMEFILE`
`cut -d ',' -f 1-3 SOMEFILE`

### sort

默认按首字符ASCII的顺序排序

- `-n` 按照数字真实大小排序
- `-t` 分隔符
- `-k` 指定key进行排序， 配合`-t`
- `-r` 逆序
- `-f` 忽略大小写

`sort -t : -k 3 -n /etc/passwd`

### uniq

`相邻`并且`完全一样`的行

- `-d` 只显示重复的行
- `-c` 重复次数

### tr

- `-d` 删除出现在字符集中的所有字符, `tr -d 'ab'`

`tr 'a-z' 'A-Z'` 将所有小写字段转换为大写

### grep

支持正则表达式

加`\`转义是因为有些字符在bash中有特殊函数，需要进行转义，比如 `\{\}`, `\?`, `\+`, `\|`, `\(`, `\)`

- `\?` 1次或0次
- `\{m, n\}`匹配前面的字符至少m次，至多n次
- `^` `$` 特定行首， 行尾， `^$`表示空白行
- `[]` 匹配范围内的任意字符， 支持字符集

  - `[abc]`, `[a-z0-9]`
  - `[:space:]` 空白字符
  - `[:punct:]` 标点符号
  - `[:lower:]`
  - `[:upper:]`
  - `[:alpha:]`
  - `[:digit:]`
  - `[:alnum:]` 数字和大小写字母

- `\<`或`\b` 锚定词首， 后面的任意字符必须作为单词首部出现
- `\>`或`\b` 锚定词尾， 后面的任意字符必须作为单词尾部出现
- `\(\)` 组

  反向引用

  - `\1`
  - `\2`

- `-E` 使用扩展正则表达式(相当于`egrep`), 扩展正则表达式一般不用`\`进行转义， 推荐！
- `-F` `fgrep`, 不支持正则表达式， 但速度更快

```shell
# 匹配以数字结尾
grep '[[:digit:]]$' /etc/inittab

# 匹配单词以root开头的行
grep '\<root' /etc/passwd
```

#### Context line control

- `-A` after， 后面的几行
- `-B` before， 前面的几行
- `-C` 上下几行

### sed

steam editor 默认不编辑原文件， 仅对模式空间中的数据做处理
sed "AddressCommand" file ...
