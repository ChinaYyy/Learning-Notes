# Image-Mysql

[DockerHub-Mysql](https://hub.docker.com/_/mysql?tab=tags)

```shell
docker pull mysql

docker run -it -p 3308:3306 -v /mnt/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD="111111" mysql:latest

docker run -d -p 127.0.0.1:3308:3306 -v /mnt/mysql/data:/var/lib/mysql mysql:latest
```
