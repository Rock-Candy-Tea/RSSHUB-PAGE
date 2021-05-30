
---
title: 'dom1-3个例子'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f8bff02a9a44c5085bb4d650daf0171~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 07:44:45 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f8bff02a9a44c5085bb4d650daf0171~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>dom定义了表示和修改文档所需的方法。dom对象即为宿主对象，由浏览器厂商定义，用来操作html和xml功能的一类对象的集合。dom是对html和xml的标准变成接口</strong></p>
<p><strong><strong>dom对象只能让js操作html</strong>，<strong>xml是html的脚本，里面的标签可以自定义，现在不用了</strong>
<strong>onclick一旦被点击就被执行，js里面不能写-，所以用大驼峰解决如backColor</strong></strong></p>
<h1 data-id="heading-0">例1,点击后的效果</h1>
<pre><code class="copyable"><!-- 例一 -->
    <div></div>
<script type="text/javascript">
// dom对象只能让js操作html，xml是html的脚本，里面的标签可以自定义，现在不用了
// onclick一旦被点击就被执行，js里面不能写-，所以用大驼峰解决backColor,

例1
var div = document.getElementsByTagName('div')[0];//div被选到js里面操作
div.style.width = "100px";
div.style.height = "100px";
div.style.backgroundColor = "red";
// 1
div.onclick = function()&#123;
    this.style.backgroundColor = "green";
    this.style.width = "200px";
    this.style.height = "50px";
    this.style.borderRadius ="10%";
&#125;
// 2计数器。点击一次变一次颜色
var count = 0;
div.onclick = function() &#123;
    count ++;
    if(count % 2 == 1)&#123;
        this.style.backgroundColor = "purple";
    &#125;else&#123;
        this.style.backgroundColor = "yellow";
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有点击的效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2624843477eb43edbb7e9035127a9c50~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-05-27 214322.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击第一次</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe8cc4e7c043423da7745d88cada2513~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-05-27 214437.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击第二次</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b5f606c452c421a93f30a4c6c2164a1~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-05-27 214454.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">**例2，函数实现按钮点击效果 **</h1>
<pre><code class="copyable"><html>
    <head>
        <meta charset="utf-8">
        <title>dom初探</title>
        <style type="text/css">

        .content&#123;
            display:none;
            width:200px;
            height:200px;
            border:2px solid red;
        &#125;
        .active&#123;
            background-color:blue;
        &#125;
        </style>
    </head>
    <body>
        <div class="wrapper">
            <button class="active">111</button>
            <button>222</button>
            <button>333</button>
            <div class="content" style="display:block">banana</div>
            <div class="content">appleapple</div>
            <div class="content">grape</div>
        </div>

        <script type="text/javascript">
            var btn = document.getElementsByTagName("button");
            var div = document.getElementsByClassName("content");
            // 给每一个btn加事件，点击onclick就执行函数，让当前被点击的btn实现效果，并清楚其余btn的效果
            for(var i = 0; i<btn.length; i++)&#123;
                (function(n)&#123;//产生了闭包，用立即执行函数

                    btn[n].onclick = function()&#123;
                    for(var j = 0; j<btn.length; j++)&#123;
                        btn[j].className ="";//清除所有button的效果
                        div[j].style.display = "none";//清除所有div的效果
                    &#125;
                    this.className = "active";
                    div[n].style.display = "block";
                &#125;
                &#125;(i))
                
            &#125;
</script>
 </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f8bff02a9a44c5085bb4d650daf0171~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-05-27 212008.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">例三方块移动</h1>
<pre><code class="copyable"><script type="text/javascript">
        var div = document.createElement("div")//在js创建div
        document.body.appendChild(div); //在body里面插入标签div,后续可以操作div了
        div.style.width="100px";
        div.style.height = "100px";
        div.style.backgroundColor = "red";
        div.style.position ="absolute";
        div.style.left="0";
        div.style.top="0";

        var speed = 1;

        例div.style.left="100px";//向右移动100px
# **例一**
        setInterval(function ()&#123;
### //例1每100毫秒向右下移动一次----
            //  div.style.left = parseInt(div.style.left) + 1 +"px";//parseInt把里面的元素转为数字类型
            // div.style.top = parseInt(div.style.top) + 1 +"px";

### //例2-----------加速运动
            speed += speed/20;
            div.style.left = parseInt(div.style.left) + speed +"px";
            div.style.left = parseInt(div.style.left) + speed +"px";
        &#125;, 100);//每隔数毫秒执行一次函数

# 例二加速运动到一定距离就停止运动
        var timer = setInterval(function ()&#123;
            speed += speed/11;
            div.style.left = parseInt(div.style.left) + speed +"px";
            div.style.top = parseInt(div.style.top) + speed +"px";
            if(parseInt(div.style.top)> 200 && parseInt(div.style.left)>200)&#123;
                clearInterval(timer);//清除定时器
            &#125;
        &#125;,100);
</script>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            