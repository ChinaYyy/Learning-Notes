# Learning Canvas

```html
<canvas width="800" height="600">对不起，您的浏览器不支持canvas</canvas>

<script type="text/javascript">

    // 得到画布标签
    var myCanvas = document.querySelector("#myCanvas");
    // 上下文， 相当于新建画布
    var ctx = myCanvas.getContext("2d");
    // 后面的操作都是ctx的事情， 和myCanvas没有关系了
    // fillStyle 设置填充颜色
    ctx.fillStyle = "lightseagreen"
    // 绘制填充矩形
    ctx.fillRect(100,100,300,200)
    // 开始绘制路径
    ctx.beginPath();
    ctx.moveTo(100,100);  //移动，但不画线
    ctx.lineTo(300,300);  //移动并画线
    ctx.lineTo(600,300);
    ctx.closePath(); // 自动闭合路径
    // 设置线的宽度和颜色
    ctx.lineWidth = "10";
    ctx.strokeStyle = "red";
    ctx.stroke();
    ctx.fill();  // 填充颜色

    //绘制新图形时，需要再重新beginPath
    ctx.beginPath();
</script>
```

- canvas的文本，是不支持canvas的显示内容
- width， height需要写在canvas标签里面， 写在css里的话，会扭曲变形

## 笔触、填充

笔触也叫描边， Canvs中的任何形状，都是由这两个部分组成的。
笔触在canvas中视为一个`Path`的实例，必须stroke之后才能上屏幕。

填充要用`fill`才能上屏幕
