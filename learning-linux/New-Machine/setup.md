# Setup

#### net-tools 查看ip

```
sudo apt-get install net-tools
ifconfig
```

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
1. 首先编译安装 libQtShadowsocks

    依赖
    ```
    sudo apt-get install g++ cmake qt5-default qtcreator pkg-config
    ```
    编辑安装 Botan2
    ```
    wget https://botan.randombit.net/releases/Botan-2.3.0.tgz
    tar xvf Botan-2.3.0.tgz
    cd Botan-2.3.0
    ./configure.py
    make -j4
    sudo make install
    sudo ldconfig
    ```


    ```
    git clone git@github.com:shadowsocks/libQtShadowsocks.git

    mkdir build && cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr
    make -j4
    sudo make install
    ```
2. 编译安装shadowsocks-qt5
    ```
    sudo apt-get install libqrencode-dev libzbar-dev libappindicator-dev

    git clone git@github.com:shadowsocks/shadowsocks-qt5.git

    mkdir build && cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr
    make -j4
    sudo make install
    ```


#### vpn软件 openfortigui
[github-openfortigui](https://github.com/theinvisible/openfortigui)

[docs-openfortigui](https://hadler.me/linux/openfortigui/)

#### Postman

报错./electron: error while loading shared libraries: libgconf-2.so.4: cannot open shared object file: No such file or directory
```
apt-get install libgconf-2-4
```

Gtk-Message: Failed to load module "canberra-gtk-module"
```
sudo apt-get install libcanberra-gtk-module
```