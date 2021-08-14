
---
title: 'CSS控制html元素、文字的各种居中'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fd3f9c569514cc68b713fedd97dfecf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 23:55:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fd3f9c569514cc68b713fedd97dfecf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">前言</h3>
<p>在前端开发中，常常遇要水平或垂直居中文字、元素等情况，在这里做了一下常见解决办法的总结，居中的其它办法还有待探索和总结。</p>
<h4 data-id="heading-1">CSS水平居中</h4>
<h5 data-id="heading-2">1. 居中行内元素或者行内块元素（水平居中文字）。</h5>
<p>可以对其<strong>父元素</strong>添加text-align属性：center。也可以将text-align的属性值设置为left和right进行左右对齐。</p>
<p>CSS样式</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.align-center</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background-color</span>: lightcoral;
    
    <span class="hljs-comment">/* 水平居中 */</span>
    <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>html元素</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"align-center"</span>></span>水平居中<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fd3f9c569514cc68b713fedd97dfecf~tplv-k3u1fbpfcp-watermark.image" alt="水平居中.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">2. 元素（盒子、容器）本身居中（利用margin实现）</h5>
<p>如果是居中一个元素（盒子、容器），而不是元素里面的文字可以用如下方式实现。</p>
<p><strong>方法前提：</strong></p>
<ul>
<li>盒子必须制定了宽度width。</li>
<li>盒子的左右外边距设置为auto。</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.align-center</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background-color</span>: lightcoral;

    <span class="hljs-comment">/* 方法1
    水平居中 */</span>
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
    
    <span class="hljs-comment">/*
    方法2
    margin:auto;
    */</span>
    
    <span class="hljs-comment">/*
    方法3
    margin-left:auto;
    margin-right:auto;
    */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"align-center"</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e2671c1eabe479d954ef48b6eae13a1~tplv-k3u1fbpfcp-watermark.image" alt="水平居中2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">CSS垂直居中</h4>
<h5 data-id="heading-5">1. 单行文字垂直居中</h5>
<p>利用line-height，将其属性值设置为容器相同高度，实现<strong>单行文字</strong>的垂直居中。</p>
<p>css代码</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.heigt-center</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background-color</span>: lightgreen;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>html代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"heigt-center"</span>></span>
    垂直居中
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58511857628a49c5842d30fb21f86261~tplv-k3u1fbpfcp-watermark.image" alt="单行文字垂直居中.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">2.图片和文字垂直对齐（多用于头像姓名）</h5>
<p>使用场景：一般做网页时需要让头像和姓名水平居中可以使用如下方法实现。</p>
<p><strong>注意</strong>：</p>
<ul>
<li>
<p>是给图片元素设置CSS属性：vertical-align: middle;</p>
</li>
<li>
<p>此属性需要设置给<strong>行内块元素</strong>，后面的文字才有效。</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adac9c994e764fd7944dda2940e26e33~tplv-k3u1fbpfcp-watermark.image" alt="头像姓名水平居中.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">25px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
    
    <span class="hljs-attribute">vertical-align</span>: middle;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"head"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">""</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"img/head.jpg"</span> /></span>
        子非鱼
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">CSS水平垂直居中</h4>
<p>水平垂直居中常用下面.content中的三行代码实现，不过可以用.content2中比较简单的两行代码实现。</p>
<p><strong>CSS样式</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background-color</span>: skyblue;

    <span class="hljs-comment">/* 水平垂直居中 */</span>
    <span class="hljs-attribute">display</span>: grid;
    <span class="hljs-attribute">align-items</span>: center;
    justify-items: center;
&#125;

<span class="hljs-selector-class">.content2</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background-color</span>: lawngreen;

    <span class="hljs-comment">/*水平垂直居中*/</span>
    <span class="hljs-attribute">display</span>: grid;
    place-items: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>html元素</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>水平垂直居中文字<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content2"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>水平垂直居中文字<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4352cbf441b408fbcce8e42d5bba378~tplv-k3u1fbpfcp-watermark.image" alt="水平垂直居中.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            