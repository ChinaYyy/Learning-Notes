# Setup Mysql

## apt-get install
```
$ sudo apt-get install mysql-server
```

查看地初始密码
```
$ sudo cat /etc/mysql/debian.cnf

[client]
host     = localhost
user     = debian-sys-maint
password = NsJxBEBDi8Of5cRs

$ mysql -udebian-default-account -pdefaultpassword
> use mysql

> CREATE USER 'root'@'%' IDENTIFIED BY '111111';
```

用户和管理和权限控制 [click](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)

```
set password for 'root'@'localhost' = password('111111');
> set password for 'root'@'%' = password('111111');
> GRANT ALL PRIVILEGES ON *.* TO 'yourname'@'localhost' IDENTIFIED BY 'yourpass' WITH GRANT OPTION;
> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '111111' WITH GRANT OPTION;

> flush privileges;

> update mysql.user set password = password('111111') where user = 'root' and host = 'localhost';
> flush privileges;

> DROP USER 'root'@'localhost';
> DROP USER 'root'@'%';
```


