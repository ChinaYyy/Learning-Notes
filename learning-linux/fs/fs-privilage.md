# 文件权限

- chown
- chgrp
- chmod

## r w x

文件：

- `r`： 可读， 可以使用`cat`等命令查看文件内容
- `w`:  可写， 编辑、删除文件
- `x`： 可执行

目录：

- `r`： 执行ls列出内部所有文件
- `w`： 在目录内创建文件
- `x`： 使用`cd`, `ls -l`

## umask

用户创建目录或文件时设定的默认权限

目录权限: 666-umask

文件权限: 777-umask

## chown & chgrp

chown [OPTION]... [OWNER][:[GROUP]] FILE...
chown [OPTION]... --reference=RFILE FILE...

- `-R`
- `--reference=RFILE` 参考文件， 改为参考文件一样

## chmod

u, g, o, a

chmod 755 PATH

chmod [OPTION]... MODE[,MODE]... FILE...

chmod u=rwx PATH  // 某类用户权限

chmod gp=rw PATH  

chmod u-x PATH    // 某类用户某位权限

