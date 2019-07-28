# Bash

## bash 的配置文件

- 全局配置文件

  - /etc/profile
  - /etc/profile.d/*.sh
  - /etc/bashrc

- 个人配置

  - ~/.bash_profile
  - ~/.bashrc

profile类文件

- 设定环境变量
- 运行命令或脚本

bashrc类文件

- 设定本地变量
- 定义命令别名

### 登录式shell

/etc/profile  --> /etc/profile.d/*.sh  --> ~/.bash_profile  --> ~/.bashrc  --> /etc/bashrc

### 非登录式shell

~/.bashrc --> /etc/bashrc --> /etc/profile.d/*.sh

## 变量

本地变量 VARNAME=VALUE 作用域为整个bash进程

局部变量 local VARNAME=VALUE 作用域为当前代码段

环境变量 export VARNAME=VALUE 作用域为当前shell进程及其子进程

位置变量 $1, $2, ...

特殊变量

    `$?` 上一条命令的执行状态返回值 0~255：

        - 0: 正确执行
        - 1~255: 错误执行， 1，2，127系统预留

    `$#` 参数的个数

    `$*` 参数列表

    `$@` 参数列表

### 变量替换

`echo "The current work directory is $(pwd)"`

``echo "The current work directory is `pwd`"``

- `反引号` 命令替换
- `""`, 弱引用， 可以实现变量替换
- `''`， 强引用， 不完成变量替换

## 文件名通配符(不包含目录 ) globbing

- `*` 任意长度的任意字符
- `？` 任意单个字符
- `[]` 匹配指定范围内的任意单个字符

  - `[abc]`, `[a-z0-9]`
  - `[:space:]` 空白字符
  - `[:punct:]` 标点符号
  - `[:lower:]`
  - `[:upper:]`
  - `[:alpha:]`
  - `[:digit:]`
  - `[:alnum:]` 数字和大小写字母

匹配所有数字和大小写字母： `[[:alnum:]]*`

## 条件判断

条件测试类型：

- 整数测试
- 字符测试
- 文件测试

条件测试的表达式：

- `[ expression ]`  必须有空格
- `[[ expression ]]`
- `test expression`

整数比较

- `-eq` 两个整数是否相等  [ $A -eq $B ]
- `-ne` 不等
- `-gt` 大于
- `-lt`
- `-ge` 大于等于
- `-le`

字符测试

- `==`
- `！=`
- `>`
- `<`
- `-n string` 测定字符串是否为空， 空则真，不空则假
- `-s string` 不空为真， 空则假

逻辑关系

- `&&`  两边要有空格
- `||`
- `！`

文件测试

- `-e FILE` 文件是否存在
- `-f FILE` 文件是否为普通文件
- `-d FILE` 文件是否为目录
- `-r FILE` 是否有读取权限
- `-w FILE`
- `-x FILE`

[ -e /etc/inittab ]
[ ! -e /etc/inittab ]

### 控制结构

if 判断条件; then
  statement
  statement
elif 判断条件; then
  statement
else
  statement
fi

需要区分判断条件使用的是`命令执行结果` 还是 `命令执行状态`($?)

`if id $NAME; then` 这使用的是执行状态， 只要命令正常执行了($?=0)，就为真

``if [ `id -u $NAME` -eq 0 ]; then`` 这使用的是命令执行结果， 需要使用反引号包起来！

### 循环

- for
- while
- until

如何生成列表：

{1..10}

seq START INCREMENT STOP  `seq 1 2 10`

```shell

for 变量 in 列表; do
    循环体
done

for i in 1 2 3 4; do
    循环体
done
```

Example

```shell

declare -i SUM=0

for I in {1..100}; do
    let SUM=$[$SUM + $I]
done
```

### 算数运算

declare -i SUM=0  声明一个变量为整形

declare -x SUM 声明一个环境变量

1. let 算数运算表达式  `let C=$A+$B`
2. $[算数运算表达式] `C=$($A+$B)`
3. $((算数运算表达式)) `E=$(($A+$B))`
4. expr 算数运算表达式， 表达式中各操作数及运算符之间要有空格， 而且要使用命令引用  C=`expr $A + $B`

## 测试脚本错误

`bash -n 脚本`  检测脚本是否有语法错误

`bash -x 脚本`  单步执行
