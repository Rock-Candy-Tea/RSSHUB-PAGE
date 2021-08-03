
---
title: 'Instance Methods _Events'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11b945eb1f524d0cb068f33f9d600a7e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 01:52:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11b945eb1f524d0cb068f33f9d600a7e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11b945eb1f524d0cb068f33f9d600a7e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当handle后面的括号去掉时，就会出现上面的情况。</p>
<pre><code class="copyable">  <title>Instance Methods Events</title>
</head>
<body>
    <div id="app">
        点击次数：&#123;&#123;count&#125;&#125;
        <button @click="handle()">点击我每次加1</button>
        <button @click="handle(8)">点击我每次加8</button>
    </div>
    <script src="https://cdn.bootcdn.net/ajax/libs/vue/2.6.14/vue.min.js"></script>
 <script>
        var app = new Vue(&#123;
            el:"#app",
            data:&#123;
                count:0
            &#125;,
            methods:&#123;
                handle:function(count)&#123;
                    count = count || 1;//如果传count就是count，没有就默认是1
                    this.count += count;

                &#125;
            &#125;
        &#125;)
    </
    script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果方法中有参数，但是没有加括号，默认传原生事件对象</p>
<h3 data-id="heading-0">修饰符</h3>
<p>阻止向上冒泡</p>
<pre><code class="copyable"><body>
    <div id="app">
    <div @click="divClick" style="height:100px;width:100px; background-color:brown;">
        <button @click.stop="btnClick">点击我</button>

    </div>
        
    </div>
    <script src="https://cdn.bootcdn.net/ajax/libs/vue/2.6.14/vue.min.js"></script>
    <script>
        var app = new Vue(&#123;
            el:"#app",
            data:&#123;
                
            &#125;,
            methods:&#123;
               divClick:function()&#123;
                   alert('div被点击了')
               &#125;,
               btnClick:function()&#123;
                   alert('BUTTON被点击了')
               &#125;

                &#125;
            
        &#125;)
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47c098ceec4845ae9cc60c21cc78453b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
点击button时，div也是那块区域，是向上冒泡了，一块都有反应；
加上一个stop，则点击button和div就会分开了。</p>
<h3 data-id="heading-1">prevent的用法</h3>
<p>每次提交整个页面都会重新加载，则反应速度会变慢</p>

提交表单

现在不让她刷新整个页面，只刷新提交的部分：
<div>
        <hr>
        
            提交表单
            
        </div>
        hangle:function()&#123;
                   alert('不刷新了')
               &#125;
   ### self:只作用在元素本身，而非子元素；
   once：店家按钮只执行一次的方法：
   执行无数次
   加了once只执行一次
   ### 监听键盘事件
   <input type="checkbox" disabled>
   submitMe:function()&#123;
   alert('您按下了enter键盘')&#125;</div>  
</div>
            