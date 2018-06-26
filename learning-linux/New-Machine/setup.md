# Setup

#### 远程ssh连接ubuntu

Could not connect to '192.168.1.102' (port 22): Connection failed

```
sudo apt-get install openssh-server
```

#### 安装 shadowsocks-qt5
```
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```

编译安装
1. 首先编译安装libQtShadowsocks
    ```
    git clone git@github.com:shadowsocks/libQtShadowsocks.git

    mkdir build && cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr
    make -j4
    sudo make install
    ```
2. 编译安装shadowsocks-qt5
    ```
    sudo apt-get install libqrencode-dev
    sudo apt-get install libzbar-dev
    sudo apt-get install libappindicator-dev

    mkdir build && cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr
    make -j4
    sudo make install
    ```


#### vpn软件 openfortigui
[github-openfortigui](https://github.com/theinvisible/openfortigui)

[docs-openfortigui](https://hadler.me/linux/openfortigui/)