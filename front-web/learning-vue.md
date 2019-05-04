# Learning Vue

## Basic Prepare

引入：

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>  # 开发环境
<script src="https://cdn.jsdelivr.net/npm/vue"></script>  # 生产环境
```

`v- 指令`： 指令的职责是，当表达式的值改变时，将其产生的连带影响，响应式地作用于 DOM

v-bind指令 `v-bind:title="message"`将这个节点的title特性和Vue实例的message属性保持一致  


条件判断 v-if
`<span v-if="seen">Now you seee me</span>` `data.seen=true/false`， v-if 指令将根据表达式 seen 的值的真假来插入/移除 <p> 元素。

loop v-for

事件监听器 v-on `v-on:click=reversev-on:click=reverse`， 它用于监听 DOM 事件

input model `<input v-model="message">`, 实现表单输入和应用状态之间的双向绑定。

component `$todo-item`

当Vue实例被创建时，data中存在的属性才会被追踪响应。`Object.freeze(vue)`会阻止修改现有的属性。

vm.$watch('a', function (newValue, oldValue) {
  // 这个回调将在 `vm.a` 改变后调用
})

![实例生命周期钩子](../images/vue-lifecycle.png)

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