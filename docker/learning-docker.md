# Learning Docker

## Install

- install in ubuntu
  
    [ubuntu install](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

- 避免每次命令输入sudo

    ```shell
    sudo usermod -aG docker $USER
    ```

    [Manage Docker as a non-root user](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user)

- 更改仓库镜像地址

    `sudo vim /etc/default/docker` 在最后一行添加

    ```text
    DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
    ```

## 程序环境

Docker程序环境

环境配置文件:

- `/etc/sysconfig/docker-network`
- `/etc/sysconfig/docker-storage`
- `/etc/sysconfig/docker`

Unit File

- `/usr/lib/systemd/system/docker.service`

Docker Registry配置文件

- `/etc/containers/registries.conf`

Docker 镜像加速

```shell
$ vim /etc/docker/daemon.json

{
    "registry-mirrors": ["https://registery.docker-cn.com"]
}

$ systemctl start docker.service
```

## Command

- 容器
  
    docker attach <?>    //重新连回容器

## Tmp

- 允许特定特定容器间的连接

    --icc=false --iptables=true --link

- 覆写entrypoint
    docker run --entrypoint=/bin/bash -it {imageid}
