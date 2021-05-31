
---
title: '什么是BFC'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c555a0dbe249a2a8126ec16684e5a9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 00:53:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c555a0dbe249a2a8126ec16684e5a9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是BFC？</h2>
<p>再解释之前需要了解下面的一些概念有一个认识：</p>
<p><strong>Box(框)</strong></p>
<p>Box它是组成页面的基本单元，一个界面可以由多个Box元素组成。元素的类型（块级与行级）和display属性决定了这个Box的类型，不同类型的 Box， 会参与不同的 Formatting Context（一个决定如何渲染文档的容器），因此Box内的元素会以不同的方式渲染。
Box目前分为一下几种：</p>
<ul>
<li>
<p><strong>block-level</strong></p>
<pre><code class="copyable">box:display 属性为 block, list-item, table 的元素，会生成 block-level box。并且参与 block Formatting context；
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>inline-level</strong>
box:display 属性为 inline, inline-block, inline-table 的元素，会生成 inline-level box。并且参与 inline formatting context；</p>
</li>
<li>
<p><strong>run-in</strong>
box:display 属性为 run-in的元素，会生成run-in-level box.
run-in框的行为如下：
1、如果run-in框包含一个块框，那么run-in框变为块框。
2、如果run-in框的后继兄弟元素为块框（非浮动，非绝对定位），那么run-in框变为该块框的第一个行内框。run-in不能插入本身为run-in的块中，也不能插入块中已有run-in的块中。
3、否则，run-in框变为块框。</p>
<p>浏览器支持：IE8+，chrome（unsupport）</p>
<p><strong>style</strong>
.run-in-box &#123;display: run-in;&#125;</p>
<p><strong>html:</strong></p>
<pre><code class="copyable"> <h2>case 1</h2>
 <div class="run-in-box">
   <p>some text...</p>
 </div>
 <div>some other text....</div>
 <h2>case 2</h2>
 <h3 class="run-in-box">A run-in heading.</h3>
 <p>And a paragraph of text that follows it.</p>
 <h2>case 3</h2>
 <h3 class="run-in-box">A run-in heading.</h3>
 <span>And a span of text that follows it.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><strong>Formatting context</strong></p>
<p>　　Formatting context 是 W3C CSS2.1 规范中的一个概念。它是页面中的一块渲染区域，并且有一套渲染规则，它决定了其子元素将如何定位，以及和其他元素的关系和相互作用。最常见的 Formatting context 有 Block fomatting context (简称BFC)和 Inline formatting context (简称IFC)。</p>
<p><strong>BFC 定义</strong></p>
<p>　　BFC(Block formatting context)直译为"块级格式化上下文"。它是一个独立的渲染区域，只有Block-level box参与， 它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干。</p>
<p><strong>BFC布局规则：</strong></p>
<ol>
<li>内部的Box会在垂直方向，一个接一个地放置。</li>
<li>Box垂直方向的距离由margin决定。属于同一个BFC的两个相邻Box的margin会发生重叠</li>
<li>每个元素的margin box的左边， 与包含块border box的左边相接触(对于从左往右的格式化，否则相反)。即使存在浮动也是如此。</li>
<li>BFC的区域不会与float box重叠。</li>
<li>BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素。反之也如此。</li>
<li>计算BFC的高度时，浮动元素也参与计算</li>
</ol>
<p><strong>二、哪些元素会生成BFC?</strong></p>
<ul>
<li>根元素</li>
<li>float属性不为none</li>
<li>position为absolute或fixed</li>
<li>display为inline-block, table-cell, table-caption, flex, inline-flex</li>
<li>overflow不为visible</li>
</ul>
<p><strong>三、BFC的作用及原理</strong>
<strong>1. 自适应两栏布局</strong></p>
<p>代码：</p>
<pre><code class="copyable"><style>
    body &#123;
        width: 300px;
        position: relative;
    &#125;
 
    .aside &#123;
        width: 100px;
        height: 150px;
        float: left;
        background: #f66;
    &#125;
 
    .main &#123;
        height: 200px;
        background: #fcc;
    &#125;
</style>
<body>
    <div class="aside"></div>
    <div class="main"></div>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c555a0dbe249a2a8126ec16684e5a9~tplv-k3u1fbpfcp-zoom-1.image" alt="4dca44a927d4c1ffc30e3ae5f53a0b79.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据BFC布局规则第3条：</p>
<blockquote>
<p>每个元素的margin box的左边， 与包含块border box的左边相接触(对于从左往右的格式化，否则相反)。即使存在浮动也是如此。</p>
</blockquote>
<p>因此，虽然存在浮动的元素aslide，但main的左边依然会与包含块的左边相接触。</p>
<p>根据BFC布局规则第四条：</p>
<blockquote>
<p>BFC的区域不会与float box重叠。</p>
</blockquote>
<p>我们可以通过通过触发main生成BFC， 来实现自适应两栏布局。</p>
<pre><code class="copyable">.main &#123;
    overflow: hidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当触发main生成BFC后，这个新的BFC不会与浮动的aside重叠。因此会根据包含块的宽度，和aside的宽度，自动变窄。效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79d0657b5ec048dfade8397c640a32b0~tplv-k3u1fbpfcp-zoom-1.image" alt="t01077886a9706cb26b.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2. 清除内部浮动</strong></p>
<pre><code class="copyable"><style>
    .par &#123;
        border: 5px solid #fcc;
        width: 300px;
    &#125;
 
    .child &#123;
        border: 5px solid #f66;
        width:100px;
        height: 100px;
        float: left;
    &#125;
</style>
<body>
    <div class="par">
        <div class="child"></div>
        <div class="child"></div>
    </div>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d57e9e104844610b8f203d78445a1dd~tplv-k3u1fbpfcp-zoom-1.image" alt="t016035b58195e7909a.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据BFC布局规则第六条：</p>
<blockquote>
<p>计算BFC的高度时，浮动元素也参与计算</p>
</blockquote>
<p>为达到清除内部浮动，我们可以触发par生成BFC，那么par在计算高度时，par内部的浮动元素child也会参与计算。
代码：</p>
<pre><code class="copyable">.par &#123;
    overflow: hidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9764374352074bcb96c4355213f536ae~tplv-k3u1fbpfcp-zoom-1.image" alt="t016bbbe5236ef1ffd5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3. 防止垂直 margin 重叠</strong></p>
<pre><code class="copyable"><style>
    p &#123;
        color: #f55;
        background: #fcc;
        width: 200px;
        line-height: 100px;
        text-align:center;
        margin: 100px;
    &#125;
</style>
<body>
    <p>Haha</p>
    <p>Hehe</p>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4469b363a62048a9b5194af46d7e7595~tplv-k3u1fbpfcp-zoom-1.image" alt="t01b47b8b7d153c07cc.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>两个p之间的距离为100px，发送了margin重叠。
根据BFC布局规则第二条：</p>
<blockquote>
<p>Box垂直方向的距离由margin决定。属于同一个BFC的两个相邻Box的margin会发生重叠</p>
</blockquote>
<p>我们可以在p外面包裹一层容器，并触发该容器生成一个BFC。那么两个P便不属于同一个BFC，就不会发生margin重叠了。</p>
<p>代码</p>
<pre><code class="copyable"><style>
    .wrap &#123;
        overflow: hidden;
    &#125;
    p &#123;
        color: #f55;
        background: #fcc;
        width: 200px;
        line-height: 100px;
        text-align:center;
        margin: 100px;
    &#125;
</style>
<body>
    <p>Haha</p>
    <div class="wrap">
        <p>Hehe</p>
    </div>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60de12a6fa90427287ef3e3acedec7b1~tplv-k3u1fbpfcp-zoom-1.image" alt="t0118d1d2badbb00521.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另一种情况</p>
<pre><code class="copyable"><style>
        .box6&#123;
            background: orange;
            height: 200px;
            width: 600px;
        &#125;
        .box6-c&#123;
            height: 100px;
            width: 100px;
            background: black;
            margin-top: 80px;
        &#125;
</style>

<body>
<div class="box6">
    <div class="box6-c"></div>
</div>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2df4f49a87cc423ca2f648a81fa3a6e2~tplv-k3u1fbpfcp-zoom-1.image" alt="图片描述" loading="lazy" referrerpolicy="no-referrer">
内部的子元素的maring距父级的外边距为0；
根据BFC规则第五条：</p>
<blockquote>
<p>BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素。反之也如此。</p>
</blockquote>
<p>我们可以将父级盒子触发BFC，那么父级则属于独立容器，不受外面元素的影响；
代码：</p>
<pre><code class="copyable">.box6 &#123;
    overflow: hidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f6b7eb3645431ca8936a3c97bc02e2~tplv-k3u1fbpfcp-zoom-1.image" alt="图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">总结</h2>
<p>其实以上的几个例子都体现了BFC布局规则第五条：</p>
<blockquote>
<p>BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素。反之也如此。</p>
</blockquote>
<p>因为BFC内部的元素和外部的元素绝对不会互相影响，因此， 当BFC外部存在浮动时，它不应该影响BFC内部Box的布局，BFC会通过变窄，而不与浮动有重叠（两端布局）。同样的，当BFC内部有浮动时，为了不影响外部元素的布局，BFC计算高度时会包括浮动的高度。避免margin重叠也是这样的一个道理。</p></div>  
</div>
            