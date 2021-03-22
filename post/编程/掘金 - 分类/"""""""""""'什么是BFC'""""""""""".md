
---
title: """""""""""'什么是BFC'"""""""""""
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 18:33:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73936ce436c34cf1b7cc3badf63ac0f7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是BFC（Block Formatting Context ）</h2>
<p>BFC（Block formatting context ）“块级格式上下文”。 是用于布局块级盒子的一块渲染区域。并且与这个区域的外部毫无关系。
可以理解为BFC是一个块独立的作用域，它有些自己的特性。具有 BFC 特性的元素可以看作是隔离了的独立容器，容器里面的元素不会在布局上影响到外面的元素，并且 BFC 具有普通容器所没有的一些特性。</p>
<h2 data-id="heading-1">如何产生BFC</h2>
<p>满足下列条件之一就可以触发BFC</p>
<p>1.<code>float</code> 的值不是<code> none</code>
2.<code>position</code> 的值不是<code>static</code>或者<code>relative</code>。
3.<code>display</code>的值是<code>inline-block</code>、<code>table-cell</code>、<code>flex</code>、<code>table-caption</code>或者<code>inline-flex</code>
4.<code>overflow</code> 的值不是 <code>visible</code></p>
<h2 data-id="heading-2">BFC的作用</h2>
<p><strong>1.解决margin塌陷问题</strong>
属于同一个BFC的两个相邻的box的margin会重叠，以大的为主。要想解决这个问题，可以将两个盒子分为不同的BFC中。
在同一个BFC中：</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73936ce436c34cf1b7cc3badf63ac0f7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>成为两个BFC，给其中一个盒子外面再包裹一层，并加上<code> overflow: hidden;</code></p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdbd63c46c7c4c608245e1af191afd3c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <style>
        .red &#123;
            <span class="hljs-attr">width</span>: 100px;
            height: 100px;
            background-color: red;
            margin: 20px;
        &#125;
        .box &#123;
            <span class="hljs-attr">overflow</span>: hidden;
        &#125;
        .yellow &#123;
            <span class="hljs-attr">width</span>: 100px;
            height: 100px;
            background-color: yellow;
            margin: 20px;
        &#125;
    </style>
</head>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"red"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"yellow"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.解决父元素高度塌陷问题</strong></p>
<p>当子元素设置为浮动，父元素没有设置高度时，父元素无法撑开子元素的高度
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24892436e11e4f8281a6f32e10699550~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>给父元素设置<code> overflow: hidden;</code>，触发BFC，就可以撑开高度</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68ee8b6114c946b4ba46b2a5f78eebb5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><style>
        .box1 &#123;
            <span class="hljs-attr">width</span>: 200px;
            border: 2px solid #ccc;
            overflow: hidden;
        &#125;
        .box2 &#123;
            <span class="hljs-attr">width</span>: 100px;
            height: 100px;
            background-color: green;
            float: left;
        &#125;
    </style>
</head>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box1"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.解决相邻div遮盖问题（可用作两栏布局）</strong>
两个相邻的div，其中一个浮动，另一个就会被覆盖</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ff96558fe934f338f127a82754bbf2d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>给被覆盖的元素加上<code> overflow: hidden;</code>，触发BFC，就可以防止被红色盒子遮挡</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b0f5ce68e84e40b3ab836d9c6be1f3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-bash copyable" lang="bash"> <style>
        .box1 &#123;
            height: 100px;
            width: 100px;
            <span class="hljs-built_in">float</span>: left;
            background: red
        &#125;
        .box2 &#123;
            width: 200px;
            height: 200px;
            background: <span class="hljs-comment">#eee;</span>
            overflow: hidden;
        &#125;
    </style>
</head>
<body>
    <div class=<span class="hljs-string">"box1"</span>>我是一个左浮动的元素</div>
    <div class=<span class="hljs-string">"box2"</span>>我是一个没有设置浮动,也没有触发 BFC 的元素</div>
</body>

<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            