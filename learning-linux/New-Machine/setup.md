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

#### Foxit Reader

[Ubuntu pdf阅读器](https://linux.cn/article-7245-1.html)

安装 Fixit Reader, [下载地址](https://www.foxitsoftware.com/downloads/thanks.php?page=reader_test_b&product=Foxit-Reader&platform=Linux-64-bit&version=2.4.1.0609&package_type=run&language=English)

```
cd /tmp 
gzip -d FoxitReader_version_Setup.run.tar.gz 
tar -xvf FoxitReader_version_Setup.run.tar 
./FoxitReader_version_Setup.run 
```


## Ubuntu桌面环境配置

`$ sudo apt install dconf-editor`

#### 窗口按钮放左边

命令行:

```shell
gsettings set org.gnome.desktop.wm.preferences button-layout ‘close,maximize,minimize:’

右侧冒号放左侧 :close,maximize,minimize
```

#### 单击任务栏图标最小化

`gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'`

#### Rename Terminal -- Set title

```
vim  ~/.bashrc

set-title(){
  ORIG=$PS1
  TITLE="\e]2;$@\a"
  PS1=${ORIG}${TITLE}
}

source ~/.bashrc
```


## Bugs

#### Ubuntu18.04蓝牙连接问题

[Ubuntu 18.04上的蓝牙连接问题](https://sunflower.keda.io/bluetooth-connection-issue-on-ubuntu-18-04)
```
sudo add-apt-repository ppa:bluetooth/bluez
sudo apt-get update
sudo apt-get upgrade
```