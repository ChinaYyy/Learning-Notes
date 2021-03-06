# Learning Vue

## vue-cli

```bash
sudo apt-get install npm
npm install -g @vue/cli

vue create example
npm run serve
```

函数可以内置 `setTimeout` 函数

## Basic Prepare

引入：

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>  # 开发环境
<script src="https://cdn.jsdelivr.net/npm/vue"></script>  # 生产环境
```

`v- 指令`： 指令的职责是，当表达式的值改变时，将其产生的连带影响，响应式地作用于 DOM。

v-bind指令 `v-bind:title="message"`将这个节点的title特性和Vue实例的message属性保持一致  

条件判断 v-if
`<span v-if="seen">Now you seee me</span>` `data.seen=true/false`， v-if 指令将根据表达式 seen 的值的真假来插入/移除 <p\> 元素。

使用<template\>元素可以渲染分组

用 key 管理可复用的元素

    ```html
    <h1 v-if="ok">Yes</h1>
    <h1 v-else>No</h1>
    ```

loop v-for

    ```html
    <ul id="example-2">
    <li v-for="(item, index) in items">
        {{ parentMessage }} - {{ index }} - {{ item.message }}
    </li>
    </ul>
    ```

建议尽可能在使用 v-for 时提供 key，除非遍历输出的 DOM 内容非常简单，或者是刻意依赖默认行为以获取性能上的提升。

    ```html
    <div v-for="item in items" :key="item.id">
    <!-- 内容 -->
    </div>
    ```

事件监听器 v-on `v-on:click=reversev-on:click=reverse`， 它用于监听 DOM 事件

input model `<input v-model="message">`, 实现表单输入和应用状态之间的双向绑定。

component `$todo-item`

当Vue实例被创建时，data中存在的属性才会被追踪响应。`Object.freeze(vue)`会阻止修改现有的属性。

vm.$watch('a', function (newValue, oldValue) {
  // 这个回调将在 `vm.a` 改变后调用
})

![实例生命周期钩子](../images/vue-lifecycle.png)

计算属性computed， getter 计算属性与方法不同，在于计算属性会进行缓存。
    计算属性默认只有get方法，也可以添加set方法

侦听器 watch：
    当需要在数据变化时执行异步或开销较大的操作时

class与style：
    `<div v-bind:class="{ active: isActive }"></div>`

绑定内联样式：

    ```html
    <div v-bind:style="styleObject"></div>
    data: {
        styleObject: {
            color: 'red',
            fontSize: '13px'
        }
    }
    # 数组语法
    <div v-bind:style="[baseStyles, overridingStyles]"></div>  
    ```

列表渲染：
    由于js本身的限制，列表渲染有两种情况不能触发响应：
        1. 利用索引直接修改项时，例如 vm.items[indexOfItem] = newValue
        2. 修改数组的长度时，例如: vm.items.length = newLength
    解决办法：

    ```javascript
    Vue.set(vm.items, indexOfItem, newValue)
    vm.items.splice(indexOfItem, 1, newValue)
    ```

对象更改检测注意事项：

    1. Vue不能检测对象属性的添加或删除

    ```javascript
    Vue.set(vm.userProfile, 'age', 27)

    //多个
    vm.userProfile = Object.assign({}, vm.userProfile, {
        age: 27,
        favoriteColor: 'Vue Green'
    })
    ```

事件处理：

    1. 监听事件： `v-on`, demo

        ```html
        <div id="example-2">
        <!-- `greet` 是在下面定义的方法名 -->
        <button v-on:click="greet">Greet</button>
        </div>

        var example2 = new Vue({
        el: '#example-2',
        data: {
                name: 'Vue.js'
            },
        // 在 `methods` 对象中定义方法
        methods: {
            greet: function (event) {
            // `this` 在方法里指向当前 Vue 实例
            alert('Hello ' + this.name + '!')
            // `event` 是原生 DOM 事件
            if (event) {
                alert(event.target.tagName)
            }
            }
        }
        }
        ```
    2. 事件修饰符 `stop, prevent, capture, self, once, passive`
    3. 按键修饰符 `keyup`

组件：

    1. 命名规范 `my-component-name` or `MyComponentName`
    2. 局部注册

        ```javascript
        var ComponentA = { /* ... */ }
        var ComponentB = { /* ... */ }
        var ComponentC = { /* ... */ }

        new Vue({
        el: '#app',
        components: {
            'component-a': ComponentA,
            'component-b': ComponentB
        }
        })
        ```
    3. [基础组件的自动化全局注册](https://cn.vuejs.org/v2/guide/components-registration.html)

自定义事件：

    1. 命名规范 `custom-event`， 全部小写

动态组件：

    1. keep-alive 缓存切换不同的组件

分割线

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <link type="text/css" rel="stylesheet" href="index.css">

</head>
<body>

<div id="app">
    {{message}}
    <span v-if="seen">Now you seee me</span>
</div>

<script src="index.js"></script>
</body>
</html>
```

```javascript
var app=new Vue({
    el: '#app',
    data:{
        message: 'Hello Vue!',
        seen: false
    }
});
```