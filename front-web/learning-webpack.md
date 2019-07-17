# Learning Webpack

## Concepts

配置文件 `webpack.config.js`

- 入口(entry), 默认值为 `./src`

    ```js
    module.exports = {
        entry: './path/to/my/entry/file.js'
    };
    ```

- 出口(output), 默认值为 `./dist`

    ```js
    const path = require('path');

    module.exports = {
        entry: './path/to/my/entry/file.js',
        output: {
            path: path.resolve(__dirname, 'dist'),
            filename: 'my-first-webpack.bundle.js'
        }
    };
    ```

- loader

    处理非javascript文件，转换为webpack可以处理的有效模块

    ```js
    const path = require('path');

    const config = {
    output: {
        filename: 'my-first-webpack.bundle.js'
    },
    module: {
        rules: [
        { test: /\.txt$/, use: 'raw-loader' }
        ]
    }
    };
    ```

- 插件(plugins)

    loader 被用于转换某些类型的模块，而插件则可以用于执行范围更广的任务。插件的范围包括，从打包优化和压缩，一直到重新定义环境中的变量。插件接口功能极其强大，可以用来处理各种各样的任务。

    ```js
    const HtmlWebpackPlugin = require('html-webpack-plugin'); // 通过 npm 安装
    const webpack = require('webpack'); // 用于访问内置插件

    const config = {
    module: {
        rules: [
        { test: /\.txt$/, use: 'raw-loader' }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({template: './src/index.html'})
    ]
    };

    module.exports = config;
    ```

- 模式, `development`, `production`

    ```js
    module.exports = {
    mode: 'production'
    };
    ```


## Install

`npm install webpack`