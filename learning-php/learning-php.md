# Learning Php

## Preparation

install

```shell
apt-get update && apt-get upgrade
apt-get install php
```

## 类型相关

var_dump()

gettype()
settype()

错误抑制符 @()

触发错误： `trigger_error(error_msg, error_type)`

## class and object

访问非静态属性: `$this->property`（其中 property 是该属性名）这种方式来``$b = new B(); $b->bar();`

访问静态属性: `self::$property` `B::bar();`

构造函数 `__construct`

    ```php
    class BaseClass {
        function __construct() {
            print "In BaseClass constructor\n";
        }
    }

    class SubClass extends BaseClass {
        function __construct() {
            parent::__construct();
            print "In SubClass constructor\n";
        }
    }

    ```

继承

    ```php
    class ExtendClass extends SimpleClass
    {
        // Redefine the parent method
        function displayVar()
        {
            echo "Extending class\n";
            parent::displayVar();
        }
    }
    ```

::class 获取一个字符串，包含了类 ClassName 的完全限定名称

    ```php
    namespace NS {
        class ClassName {
        }
        echo ClassName::class;
    }

    // NS\ClassName
    ```

## Yii框架

1. PHP
2. 面向对象编程
3. 命令行和Composer

### Pre

```shell
# 安装composer
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer

# 全局安装 composer-asset-plugin
composer global require "fxp/composer-asset-plugin:~1.3"

# 安装应用程序模板
composer create-project --prefer-dist yiisoft/yii2-app-basic basic

# install dependence   非必要
sudo apt-get install php-xml
sudo apt-get install php-mbstring
&
php.ini 打开extention

# install vender文件
composer install

# 运行服务 
php yii serve --port=8888
```

### Route

`?r=site/say&message=heihei`

被解析至 SiteController控制器中的say操作， `SiteController::actionSay()` 调用处理请求。 在`controllers/SiteController.php`文件中。

say位于`views/site/say.php`文件中。
