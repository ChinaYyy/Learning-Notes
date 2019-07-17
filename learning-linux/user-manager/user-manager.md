# User Manager

- 用户管理

  - useradd
  - userdel
  - usermod
  - passwd
  - chsh
  - id
  - chage

## useradd

- `-u` UID
- `-g` GID 基本组
- `-G` GID,... 附加组
- `-c` "COMMENT"
- `-d` HOME_DIR
- `-s` SHELL
- `-M` NO CREATE HOME_DIR
- `-r` 添加系统用户（不能登录， 没有家目录）

## userdel

`userdeL USERNAME`

## usermod

修改用户信息

- `-u` UID
- `-g` GID 指定基本组
- `-a -G` GID 追加附加组， 不使用`-a`选项，会覆盖此前的附加组！！
- `-m -d` 指定新的家目录， 并将此前家目录的文件移动到新主目录中， 如果不存在， 则创建
- `-s` SHELL
- `-l` USERNAME 更改用户名
- `-L` 锁定账号
- `-U` 解锁账号

## passwd

passwd USERNAME

- `--stdin` echo "redhat" | passwd --stdin USERNAME

## groupadd

- `-g` GID
- `-r` 添加系统组

## 相关配置文件

- `/etc/passwd`
- `/etc/shadow`
- `/etc/group`
- `/etc/group`
- `/etc/default/useradd`
- `/etc/shells`
- `/etc/skel/`
- `/etc/login.defs`
