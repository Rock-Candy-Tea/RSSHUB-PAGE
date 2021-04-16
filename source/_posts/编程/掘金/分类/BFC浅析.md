
---
title: 'BFC浅析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a69ad08de54b43d4a7681a86e3f8584b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 18:21:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a69ad08de54b43d4a7681a86e3f8584b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">BFC定义</h3>
<p>  Formatting context(格式化上下文) 是 W3C CSS2.1 规范中的一个概念。它是页面中的一块渲染区域，并且有一套渲染规则，它决定了其子元素将如何定位，以及和其他元素的关系和相互作用。</p>
<p>  BFC(Block formatting context)，直译为“块级格式化上下文”，是一个独立渲染区域，内部的元素布局不受外界的影响，并且在一个BFC中，块盒与行盒（行盒由一行中所有的内联元素所组成）都会垂直的沿着其父元素的边框排列。</p>
<h3 data-id="heading-1">BFC特性</h3>
<ul>
<li>属于同一个BFC的两个相邻容器的上下margin会重叠（重点）</li>
<li>计算BFC高度时浮动元素也参于计算（重点）</li>
<li>BFC的区域不会与浮动容器发生重叠（重点）</li>
<li>BFC内的容器在垂直方向依次排列</li>
<li>元素的margin-left与其包含块的border-left相接触</li>
<li>BFC是独立容器，容器内部元素不会影响容器外部元素</li>
</ul>
<h3 data-id="heading-2">BFC创建</h3>
<ul>
<li>float属性不为none</li>
<li>position属性为absolute或者fixed</li>
<li>display为inline-block，table-cell，flex，inline-flex</li>
<li>overflow为hidden，auto，scroll</li>
<li>html根元素</li>
</ul>
<h3 data-id="heading-3">BFC作用</h3>
<ul>
<li>解决相邻盒子之间垂直边距重叠问题</li>
<li>清除浮动，解决盒子塌陷问题</li>
<li>解决父子元素外边距合并（外边距塌陷）</li>
<li>解决浮动环绕文字问题</li>
</ul>
<p>（1）解决相邻盒子之间垂直边距重叠问题<br>
边距重叠问题：</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .marginBottom, .marginTop &#123;
            width: 100px;
            height: 100px;
            background: red;
        &#125;
        .marginBottom &#123;
            margin-bottom: 20px;
        &#125;
        .marginTop &#123;
            margin-top: 20px;
        &#125;
    </style>
</head>
<body>
    <div class="marginBottom"></div>
    <div class="marginTop"></div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<img width="250" align="bottom" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a69ad08de54b43d4a7681a86e3f8584b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">  
<p>  样式类名分别为 .marginBottom和 .marginTop的盒子处于同一个BFC内部，相邻margin会重叠，导致两个盒子之间的margin实际为20px</p>
<p>  给 .marginBottom类样式的盒子添加一个.container的壳子，设置.container的overflow为hidden，使得两个原有的两个盒子处于不同的BFC之内，达到去除margin重叠的效果</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .marginBottom, .marginTop &#123;
            width: 100px;
            height: 100px;
            background: red;
        &#125;
        .marginBottom &#123;
            margin-bottom: 20px;
        &#125;
        .marginTop &#123;
            margin-top: 20px;
        &#125;
        .container &#123;
            overflow: hidden;
        &#125;
    </style>
</head>
<body>
    <div class="container">
        <div class="marginBottom"></div>
    </div>
    <div class="marginTop"></div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<img width="250" align="bottom" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/743c3310be73446ba33e9b37467dff1f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">  
<p>（2）清除浮动，解决盒子塌陷问题<br>
当一个标准流盒子中所有的子元素都进行了浮动，并且没有给盒子设置高度时，那么这个盒子的整个高度就会塌陷，浮动的子元素高度不计算在父元素内，父元素高度就为0。</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .child &#123;
            width: 100px;
            height: 100px;
            background: red;
            float: left;
        &#125;
        .container &#123;
            background: yellow;
        &#125;
    </style>
</head>
<body>
    <div class="container">
        <div class="child"></div>
    </div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<img width="250" align="bottom" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb32d623de7340c389ae9569b78b4f77~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>.container的高度为0，给.container的盒子添加overflow:hidden以后触发BFC，可以看到.container有了高度。</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .child &#123;
            width: 100px;
            height: 100px;
            background: red;
            float: left;
        &#125;
        .container &#123;
            background: yellow;
            overflow: hidden;
        &#125;
    </style>
</head>
<body>
    <div class="container">
        <div class="child"></div>
    </div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<img width="250" align="bottom" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9637bf102325462297f66919a80614bb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>（3）解决父子元素外边距合并（外边距塌陷）<br>
外边距合并指的是，当两个垂直外边距相遇时，它们将形成一个外边距。合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者。 (<a href="https://www.w3cschool.cn/css_margin_collapsing.html" target="_blank" rel="nofollow noopener noreferrer">CSS 外边距合并</a>)</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .child &#123;
            width: 100px;
            height: 100px;
            background: red;
            margin-top: 20px;
        &#125;
        .container &#123;
            background: yellow;
            width: 200px;
            height: 200px;
        &#125;
    </style>
</head>
<body>
    <div class="container">
        <div class="child"></div>
    </div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<img width="250" align="bottom" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/975049055515498fab265a8dc021026b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">  
<p>  child设置margin-top为20px以后，container和child都一起向上边距增加了20px，而不是child相对container增加20px的间距</p>
<p>  给container元素增加overflow触发BFC：</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .child &#123;
            width: 100px;
            height: 100px;
            background: red;
            margin-top: 20px;
        &#125;
        .container &#123;
            background: yellow;
            width: 200px;
            height: 200px;
            overflow: hidden;
        &#125;
    </style>
</head>
<body>
    <div class="container">
        <div class="child"></div>
    </div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<img width="250" align="bottom" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ef3f2318c9948c8987d4d0568d63180~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">  
<p>（4）解决浮动环绕文字问题</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .box &#123;
            width: 100px;
            height: 100px;
            background: red;
            float: left;
        &#125;
    </style>
</head>
<body>
    <div class="box"></div>
    <div>文字文字文字文字文字文字文字文字文字文文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字</div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<img width="250" align="bottom" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/984884508df24074b57f6539623c4ddc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">   
<p>文字环绕box块，第二个元素有部分被浮动元素所覆盖，(但是文本信息不会被浮动元素所覆盖) 如果想避免元素被覆盖，可触发第二个元素的 BFC 特性，在第二个元素中加入 overflow: hidden</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .box &#123;
            width: 100px;
            height: 100px;
            background: red;
            float: left;
        &#125;
        .text &#123;
            overflow: hidden;
        &#125;
    </style>
</head>
<body>
    <div class="box"></div>
    <div class="text">文字文字文字文字文字文字文字文字文字文文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字</div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<img width="250" align="bottom" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94ecdbb81ec747e68a399bdc10fcdb38~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">   
<h3 data-id="heading-4">总结</h3>
<p>  BFC与其定义一致，创建一个独立渲染区域，内部的元素布局不受外界的影响；通过这种方式与其他元素进行独立，来达成一些样式效果。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            