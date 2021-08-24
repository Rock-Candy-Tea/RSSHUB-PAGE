
---
title: '一篇搞定如何使用JavaScript  操作 DOM 元素'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'images/ldh.jpg'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 01:37:13 GMT
thumbnail: 'images/ldh.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>JavaScript 的 DOM 操作可以改变网页内容、结构和样式，我们可以利用 DOM 操作元素来改变元素里面的内容 、属性等。</p>
<h3 data-id="heading-0">一、改变元素内容</h3>
<p>1、从起始位置到终止位置的内容, 但它去除 html 标签， 同时空格和换行也会去掉</p>
<pre><code class="copyable">element.innerText
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、起始位置到终止位置的全部内容，包括 html 标签，同时保留空格和换行</p>
<pre><code class="copyable">element.innerHTML
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="copyable"><body>
    <div></div>
    <p>
        我是文字
        <span>123</span>
    </p>
    <script>
        var div = document.querySelector('div');
        div.innerText = '<strong>今天是：</strong> 2019';//加粗无效
        div.innerHTML = '<strong>今天是：</strong> 2019';//加粗了
    </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>innerText 和 innerHTML的区别</p>
<pre><code class="copyable">1) innerText 不识别html标签 非标准  去除空格和换行
2) innerHTML 识别html标签 W3C标准 保留空格和换行的
3) 这两个属性是可读写的  可以获取元素里面的内容
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">二、常用元素的属性</h3>
<pre><code class="copyable">src、href、id、alt、title
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="copyable"><body>
    <button id="btn">点击改变图片属性</button>
    <img src="images/ldh.jpg" alt="" title="桂林山水">

    <script>
        // 修改元素属性  src
        // 1. 获取元素
        var btn = document.getElementById('btn');
        var img = document.querySelector('img');
        // 2. 注册事件  处理程序
        btn.onclick = function() &#123;
            img.src = 'images/zxy.jpg';//更改图片src
            img.title = '山清水秀';//更改图片title
        &#125;
    </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">三、表单元素的属性</h3>
<pre><code class="copyable">type、value、checked、selected、disabled
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="copyable"><body>
    <button>按钮</button>
    <input type="text" value="输入内容">
    <script>
        // 1. 获取元素
        var btn = document.querySelector('button');
        var input = document.querySelector('input');

        // 2. 注册事件 处理程序
        btn.onclick = function() &#123;
            // input.innerHTML = '点击了'; //不起作用， 这个是 普通盒子 比如 div 标签里面的内容
            // 表单里面的值 文字内容是通过 value 来修改的
            input.value = '被点击了';

            // 如果想要某个表单被禁用 不能再点击 disabled  我们想要这个按钮 button禁用
            // btn.disabled = true;
            this.disabled = true;  // this 指向的是事件函数的调用者 btn

            //display:none 隐藏元素 display:block 显示元素
            btn.display='none';
        &#125;
    </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">四、样式属性操作</h3>
<p>我们可以通过 JS 修改元素的大小、颜色、位置等样式。</p>
<pre><code class="copyable">1. element.style      行内样式操作
2. element.className  类名样式操作
<span class="copy-code-btn">复制代码</span></code></pre>
<p>style示例：</p>
<pre><code class="copyable"> <style>
      div &#123;
            width: 100px;
            height: 100px;
            background-color: pink;
        &#125;      
  </style>
<body>
    <div></div>
    <script>
        // 1. 获取元素
        var div = document.querySelector('div');

        // 2. 注册事件 处理程序
        div.onclick = function() &#123;
            // div.style里面的属性 采取驼峰命名法 
            this.style.backgroundColor = 'purple';
            this.style.width = '250px';
        &#125;
    </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>className 示例：</p>
<pre><code class="copyable">    <style>
        div &#123;
            width: 100px;
            height: 100px;
            background-color: pink;
        &#125;
        
        .change &#123;
            background-color: purple;
            color: #fff;
            font-size: 25px;
            margin-top: 100px;
        &#125;
    </style>
<body>
    <div class="first">文本</div>
    <script>
        // 1. 使用 element.style 获得修改元素样式  如果样式比较少 或者 功能简单的情况下使用
        var div= document.querySelector('div');
        div.onclick = function() &#123;
            // this.style.backgroundColor = 'purple';
            // this.style.color = '#fff';
            // this.style.fontSize = '25px';
            // this.style.marginTop = '100px';
            // 让我们当前元素的类名改为了 change

            // 2. 我们可以通过 修改元素的className更改元素的样式 适合于样式较多或者功能复杂的情况
            // 3. 如果想要保留原先的类名，我们可以这么做 多类名选择器
            // this.className = 'change';  //这样写就只有change的样式了
            this.className = 'first change';  //这样就保留原来的样式再加入新的样式
        &#125;
    </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意：</code></p>
<pre><code class="copyable">1.JS 里面的样式采取驼峰命名法 比如 fontSize、 backgroundColor
2.JS 修改 style 样式操作，产生的是行内样式，CSS 权重比较高
3. 如果样式修改较多，可以采取操作类名方式更改元素样式。 
4. class因为是个保留字，因此使用className来操作元素类名属性
5. className 会直接更改元素的类名，会覆盖原先的类名。(如果要保留原来的样式可以采用多类名样式)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">小结</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eee8ee59274b4cdbb53af0ba4397b945~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            