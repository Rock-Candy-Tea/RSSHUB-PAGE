
---
title: '你可能对position和z-index有一些误解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d8c5dd9eb3a4b2186a079f2a31aaf67~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 15:59:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d8c5dd9eb3a4b2186a079f2a31aaf67~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">🧃序言</h1>
<p>最近在整理一些很偏的面经题，想起来很久以前被问到的一道题，就是 <code>position</code> 和 <code>z-index</code> 。短短 <code>10min</code> 问了这两个属性，大概直接把周一问懵了。那个时候的心情可能是这样的……</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d8c5dd9eb3a4b2186a079f2a31aaf67~tplv-k3u1fbpfcp-watermark.image" alt="丢脸" loading="lazy" referrerpolicy="no-referrer"></p>
<p>于是，一鼓作气，不懂的知识咱还是得补呀，万一下回又直接被问懵了，那就是死不知悔改了不是。</p>
<p>最后，通过各种资料的查询和理解，整理了下文。内容主要涵盖 <code>position</code> 各个取值的解析以及关于 <code>z-index</code> 的使用。</p>
<p>下面开始进入本文的讲解~🧐</p>
<h1 data-id="heading-1">🍷一、文章结构抢先知</h1>
<p>在文章开始讲解之前，我们先用一张思维导图来了解本文所要讲解的知识。<strong>详情见下图👇</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b22fa6442364ea5a61c48d4d97ba93c~tplv-k3u1fbpfcp-watermark.image" alt="思维导图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>了解完思维导图之后，现在开始进入本文的讲解。</p>
<h1 data-id="heading-2">🍸二、position</h1>
<h2 data-id="heading-3">1. position的取值</h2>
<p>通常情况下， <code>position</code> 有以下几个取值。<strong>具体如下：</strong></p>



































<table><thead><tr><th align="center">取值</th><th align="center">含义</th><th align="center">说明</th></tr></thead><tbody><tr><td align="center"><strong>static</strong></td><td align="center">静态定位</td><td align="center">对象<strong>遵循</strong>标准文档流，<strong>top</strong>，<strong>right</strong>，<strong>bottom</strong>，<strong>left</strong> 等属性失效。</td></tr><tr><td align="center"><strong>relative</strong></td><td align="center">相对定位</td><td align="center">对象<strong>遵循</strong>标准文档流中，依赖<strong>top</strong>，<strong>right</strong>，<strong>bottom</strong>，<strong>left</strong> 等属性相对于该对象在标准文档流中的位置进行偏移，同时可通过 <strong>z-index</strong> 定义层叠关系。</td></tr><tr><td align="center"><strong>absolute</strong></td><td align="center">绝对定位</td><td align="center">对象<strong>脱离</strong>标准文档流，使用 <strong>top</strong>，<strong>right</strong>，<strong>bottom</strong>，<strong>left</strong> 等属性进行绝对定位（相对于 <strong>static</strong> 定位以外的第一个父元素进行绝对定位） ，以及可通过 <strong>z-index</strong> 定义层叠关系。</td></tr><tr><td align="center"><strong>fixed</strong></td><td align="center">固定定位</td><td align="center">对象<strong>脱离</strong>标准文档流，使用 <strong>top</strong>，<strong>right</strong>，<strong>bottom</strong>，<strong>left</strong> 等属性进行绝对定位（相对于浏览器窗口进行绝对定位）同时可通过 <strong>z-index</strong> 定义层叠关系。</td></tr><tr><td align="center"><strong>sticky</strong></td><td align="center">粘性定位</td><td align="center">可以说是相对定位 <strong>relative</strong> 和固定定位 <strong>fixed</strong> 的结合。元素固定的相对偏移是相对于<strong>离它最近的具有滚动框的祖先元素</strong>，如果祖先元素都不可以滚动，那么是相对于 <strong>viewport</strong> 来计算元素的偏移量。</td></tr></tbody></table>
<h2 data-id="heading-4">2. 标准文档流</h2>
<p>我们先来看下<strong>标准文档流的定义：</strong></p>
<p>所谓标准文档流，指的是在不使用其他<strong>与排列和定位相关的</strong>特殊 <code>CSS</code> 规则时，元素的默认排列规则。</p>
<p>理解完定义之后，我们来看看各个取值的使用效果。</p>
<h2 data-id="heading-5">3. 各取值解析</h2>
<h3 data-id="heading-6">（1）static</h3>
<p><code>static</code> ，是默认的 <code>position</code> 值。它没有特殊的定位，且遵循标准文档流。我们用例子来展示一下。</p>
<p><strong>先附上代码：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>static<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">div</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">40px</span> auto;
    &#125;

    <span class="hljs-selector-class">.one</span>&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#99d98c</span>;
    &#125;
    
    <span class="hljs-selector-class">.two</span>&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#76c893</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"one"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"two"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在来看<strong>演示效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3328171ede44d0a14defbd34b4b3f2~tplv-k3u1fbpfcp-watermark.image" alt="static" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，正如我们所想的，规规矩矩的出现在我们面前，跟我们平常实现其他内容所遵循的规则也基本一样。所以这里不做过多解释。</p>
<h3 data-id="heading-7">（2）relative</h3>
<p><code>relative</code> ，对象遵循标准文档流，依赖 <code>top</code>，<code>right</code>，<code>bottom</code>，<code>left</code> 等属性相对于该对象在标准文档流中的位置进行偏移，同时可通过 <code>z-index</code> 定义层叠关系。我们现在用一个例子来展示一下。</p>
<p><strong>先附上代码：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>relative<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">300px</span>;
    &#125;
    
    <span class="hljs-selector-tag">div</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
    &#125;

    <span class="hljs-selector-class">.one</span>&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#99d98c</span>;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">40px</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">60px</span>;
    &#125;
    
    <span class="hljs-selector-class">.two</span>&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#76c893</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"one"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"two"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在来看<strong>演示效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4929c1e6a4ea4445b0a5ce19d68efa68~tplv-k3u1fbpfcp-watermark.image" alt="relative" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到， <code>relative</code> 是相对于该对象<strong>所处的标准文档流</strong>中的位置，依据 <code>left</code> 和 <code>top</code> 进行定位（当然也可以使用 <code>right</code> 和 <code>bottom</code> ，本例仅用以上两个属性做说明）。同时， <code>left</code> 和 <code>top</code> 并不会改变该对象原本在文档流中的占位空间。</p>
<hr>
<p>值得注意的是，如果设置为 <code>margin</code> 和 <code>padding</code> 属性时，该对象在标准文档流中的占位空间也将会随之改变。</p>
<p><strong>附上代码：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>relative<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">300px</span>;
    &#125;
    
    <span class="hljs-selector-tag">div</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
    &#125;

    <span class="hljs-selector-class">.one</span>&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#99d98c</span>;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">40px</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">60px</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">60px</span> <span class="hljs-number">40px</span>;
    &#125;
    
    <span class="hljs-selector-class">.two</span>&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#76c893</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"one"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"two"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们来看下浏览器的<strong>演示效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fbf6817f0234ac9a3775169f0b55be5~tplv-k3u1fbpfcp-watermark.image" alt="relative" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，当设置了 <code>margin</code> 属性时，该对象仍然跟随着其<strong>所处的标准文档流</strong>中的占位空间的变化而变化。</p>
<h3 data-id="heading-8">（3）absolute</h3>
<p><code>absolute</code> ，对象脱离标准文档流，使用 <code>top</code> ， <code>right</code> ， <code>bottom</code> ， <code>left</code> 等属性进行绝对定位（相对于 <code>static</code> 定位以外的第一个父元素进行绝对定位） ，以及可通过 <code>z-index</code> 定义层叠关系。</p>
<p>先来看个例子，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span> <span class="hljs-number">300px</span>;
    &#125;
    
    <span class="hljs-selector-class">.father-ele</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#168aad</span>;
        <span class="hljs-attribute">position</span>: relative;
    &#125;

    <span class="hljs-selector-class">.son-ele</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">position</span>: static;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#76c893</span>;
        <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">20px</span>;
    &#125;

    <span class="hljs-selector-class">.three</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#99d98c</span>;
    &#125;
    
    <span class="hljs-selector-class">.four</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#b5e48c</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father-ele"</span>></span>
        1
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"son-ele"</span>></span>
            2
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"three"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"four"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>具体效果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf0064d068a449b0ac6dca29ea1ff40a~tplv-k3u1fbpfcp-watermark.image" alt="absolute" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的定义中我们了解到，绝对定位 <code>absolute</code> 是脱离标准文档流的，且是相对于 <code>static</code> 定位以外第一个父元素，并且使用 <code>left和top</code> 或 <code>right和bottom</code> 进行绝对定位。所以大家可以看到上图，设置了 <code>absolute</code> 的 <code>four</code> 相对于 <code>father-ele</code> 进行定位。</p>
<p>值得一提的是，在使用 <code>absolute</code> 绝对定位时，必须指定 <code>left</code> 、 <code>top</code> 、 <code>right</code> 和 <code>bottom</code> 中的至少一个，否则 <code>left/right/top/bottom</code> 属性将会使用默认值 <code>auto</code> 。这将导致对象遵从标准文档流，在前一个对象之后立即被呈递，简单讲就是都变成 <code>relative</code> ，并且会占用文档空间。</p>
<p>还有就是，如果同时设置了 <code>left/right</code> 属性，那么 <code>left</code> 生效。同理如果 <code>top/bottom</code> 同时存在时， <code>top</code> 生效。</p>
<h3 data-id="heading-9">（4）fixed</h3>
<p><code>fixed</code> ，对象脱离标准文档流，使用 <code>top</code> ， <code>right</code> ， <code>bottom</code> ， <code>left</code> 等属性进行绝对定位（相对于<strong>浏览器窗口</strong>进行绝对定位）同时可通过 <code>z-index</code> 定义层叠关系。</p>
<p>先来看个例子，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>fixed<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span> <span class="hljs-number">300px</span>;
    &#125;
    
    <span class="hljs-selector-class">.father-ele</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#168aad</span>;
        <span class="hljs-attribute">position</span>: relative;
    &#125;

    <span class="hljs-selector-class">.son-ele</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">position</span>: static;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#76c893</span>;
        <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">200px</span>;
    &#125;

    <span class="hljs-selector-class">.three</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">position</span>: fixed;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#99d98c</span>;
    &#125;
    
    <span class="hljs-selector-class">.four</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#b5e48c</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father-ele"</span>></span>
        1
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"son-ele"</span>></span>
            2
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"three"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"four"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>具体效果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47886f8ed4f74e51ab719192a612c72c~tplv-k3u1fbpfcp-watermark.image" alt="fixed" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，<code>fixed</code> 是相对于<strong>浏览器窗口</strong>进行固定定位的。</p>
<h3 data-id="heading-10">（5）sticky</h3>
<p>对于 <code>sticky</code> 来说，就是粘性定位，主要用来做导航栏滑动到一定程度时让导航栏固定到顶部。不过这个属性有它一定的利弊存在，要了解清楚其中存在的各种问题后，谨慎使用！！</p>
<p>这里不再过多介绍，感兴趣的小伙伴可以<a href="https://juejin.cn/post/6844904087486464007" target="_blank" title="https://juejin.cn/post/6844904087486464007">戳此链接</a>查看该属性的内容~</p>
<p>讲到这里，关于 <code>position</code> 的各种取值解析基本就结束啦！但是细心的小伙伴可能已经发现，上面一直提到的 <code>z-index</code> ，好像都没有讲到。不着急，接下来我们就来讲讲 <code>z-index</code> 这个属性的纸短情长。</p>
<h1 data-id="heading-11">🍹三、z-index</h1>
<h2 data-id="heading-12">1. 一个片面的理解</h2>
<p>在我的认知里，一直认为 <code>z-index</code> 是用来描述页面的层叠顺序。一旦 <code>z-index</code> 的值越大，页面就可以叠放的越高。但事实证明，是我孤陋寡闻了。所谓 <code>z-index</code> ，只有在以下场景适用。<strong>分别为：</strong></p>
<ul>
<li>首先， <code>z-index</code> 这个属性并不是在所有的元素上都有效果。它仅仅只在定位元素（定义了 <code>position</code> 属性，且属性的值为非 <code>static</code> 值的元素）上有效果。</li>
<li>要判断元素在 <code>z轴</code> 上的<strong>堆叠顺序</strong>，并不仅仅是直接比较两个元素的 <code>z-index</code> 值的大小，同时，这个堆叠顺序还由元素的<strong>层叠上下文</strong>和<strong>层叠等级</strong>共同决定。</li>
</ul>
<p><strong>先来看一张图👇</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87000103020e44b494ed3f03244f296e~tplv-k3u1fbpfcp-watermark.image" alt="z-index" loading="lazy" referrerpolicy="no-referrer"></p>
<p>相信大家对三维坐标空间一定很熟悉。通常地，我们用 <code>x轴</code> 来表示<strong>水平位置</strong>，用 <code>y轴</code> 来表示<strong>垂直位置</strong>，然后用 <code>z轴</code> 来表示在<strong>纸面内外方向上的位置</strong>。但是呢，由于屏幕是一个二维平面，所以我们并不是真正地看到 <code>z轴</code> 。我们经常说的看到 <code>z轴</code> ，实际上是通过<strong>透视</strong>，将元素展现在其二维空间的前面或者后面才看到的。</p>
<p>对 <code>z-index</code> 有了一个基础的认识之后，我们来看看它的取值。</p>
<h2 data-id="heading-13">2. z-index的取值</h2>
<p>要确定沿着这 <code>z轴</code> 元素是如何分布的，<code>css</code> 允许我们对 <code>z-index</code> 属性设置3种类型的值。<strong>分别是：</strong></p>
<ul>
<li>auto（自动，默认值）；</li>
<li>整数（正整数/负整数/0）；</li>
<li>inherit（继承）。</li>
</ul>
<p>目前，让我们先关注在<strong>整数值</strong>上。 整数值可以是正值，负值，或0。通常来说，<strong>数值越大</strong>，元素也就越靠近观察者；而<strong>数值越小</strong>，元素看起来也就越远。</p>
<p>所以，如果有两个元素放在了一起，占据了二维平面上一块共同的区域，那么有着较大 <code>z-index</code> 值的元素就会掩盖或者阻隔有着较低 <code>z-index</code> 值的元素在共同区域的那一部分。</p>
<p>尽管如此，现在还是有一些问题悬而未决、等待我们的解答。<strong>具体问题如下：</strong></p>
<ul>
<li>当一个设置了 <code>z-index</code> 值的定位元素与常规文档流中的元素相互重叠的时候，谁会被置于上方？</li>
<li>当定位元素与浮动元素相互重叠的时候，谁会被置于上方？</li>
<li>当定位元素被嵌套在其他定位元素中时，又会发生什么呢？</li>
</ul>
<p>带着这些问题，我们继续深入了解神奇的 <code>z-index</code> 是怎么工作的，又会抛出哪些新的内容呢？</p>
<p>接下来我们来了解一下上述中提到的<strong>层叠上下文</strong>、<strong>层叠等级</strong>和<strong>层叠顺序</strong>。</p>
<h2 data-id="heading-14">3. 层叠上下文</h2>
<h3 data-id="heading-15">（1）举个例子</h3>
<p>我们来做一个<strong>具象的比喻：</strong></p>
<p>假设现在有一张桌子，桌子上面呢，放了好多水果，那么这张桌子就代表着一个层叠上下文。</p>
<p>再来，我们还有一张桌子，桌子上面，放了很多本书，那么新的这张桌子，又代表着一个新的层叠上下文。</p>
<p>而水果和书这两样东西，就可以理解为他们<strong>所处的层叠上下文</strong>中的<strong>层叠上下文元素</strong>。</p>
<p>这样理解，会不会就明白了许多呢。现在，我们来抛出它的定义。</p>
<h3 data-id="heading-16">（2）定义</h3>
<p>层叠上下文(stacking context)，是HTML中一个三维的概念。在 <code>CSS2.1</code> 规范中，每个盒模型的位置是三维的，分别是平面画布上的<code>X轴</code>，<code>Y轴</code>以及表示层叠的<code>Z轴</code>。一般情况下，元素在页面上沿 <code>X轴</code> 和 <code>Y轴</code> 平铺，我们是察觉不到它们在<code>Z轴</code>上的层叠关系。而一旦元素发生堆叠，这时就能发现某个元素可能覆盖了另一个元素或者被另一个元素覆盖。</p>
<p>如果一个元素含有<strong>层叠上下文</strong>，(也就是说它是层叠上下文元素)，我们可以理解为这个元素在<code>Z轴</code>上就“高人一等”，最终表现就是它离屏幕观察者更近。</p>
<h2 data-id="heading-17">4. 层叠等级</h2>
<h3 data-id="heading-18">（1）定义</h3>
<p>讲完层叠上下文，我们再来看看层叠等级又是什么呢？</p>
<p>所谓层叠等级(stacking level)，也叫 <code>层叠级别</code> 或 <code>层叠水平</code> 。<strong>它有两层含义：</strong></p>
<ul>
<li>在同一个层叠上下文中，它描述的是该层叠上下文中的层叠上下文元素在 <code>Z轴</code> 上的上下顺序。</li>
<li>在其他普通元素中，它描述的是这些普通元素在 <code>Z轴</code> 上的上下顺序。</li>
</ul>
<h3 data-id="heading-19">（2）举个例子</h3>
<p>同样，我们用刚刚那个例子来继续举例。假设桌子上面的苹果和书，是一层一层叠上去的。</p>
<p>现在，我们先看第一张桌子，第一张桌子的所有苹果，是在同一个层叠上下文中，那么苹果的堆叠顺序，就是在这个层叠上下文中 <code>z轴</code> 上的上下顺序，这是<strong>第一层含义</strong>。</p>
<p>然后呢，第一张桌子和第二张桌子，他们是两个不同的层叠上下文，我们把它们视为两个普通的元素。那这两个普通的元素，它们也有在 <code>z轴</code> 上的上下顺序。所以呢，这个上下的堆叠顺序，就是我们所说的<strong>第二层含义</strong>。</p>
<h2 data-id="heading-20">5. 形成的条件</h2>
<p>看完层叠上下文和层叠等级，我们现在需要来了解一下，要怎么样，才能让元素形成层叠上下文。<strong>具体有以下几种情况：</strong></p>
<ul>
<li>根元素<code>html</code> ；</li>
<li>绝对定位 <code>ansolute</code> 或相对定位 <code>relative</code> 且 <code>z-index</code> 值不为 <code>auto</code> ；</li>
<li>一个 <code>flex</code> 项目，且 <code>z-index</code> 值不为 <code>auto</code> ，也就是父元素 <code>display: flex|inline-flex</code> ；</li>
<li>元素的 <code>opacity</code> 属性值小于 <code>1</code> ；</li>
<li>元素的 <code>transform</code> 属性值不为 <code>none</code> ；</li>
<li>元素的 <code>mix-blend-mode</code> 属性值不为 <code>normal</code> ；</li>
<li>元素的 <code>isolation</code> 属性被设置为 <code>isolate</code> ；</li>
<li>在 <code>mobile WebKit</code> 和 <code>Chrome 22+</code> 内核的浏览器中，<code>position: fixed</code> 时总是会创建一个新的层叠上下文, 即使 <code>z-index</code> 的值是 <code>auto</code> ；</li>
<li>元素的 <code>-webkit-overflow-scrolling</code> 属性被设置 <code>touch</code> 。</li>
</ul>
<h2 data-id="heading-21">6. 层叠顺序</h2>
<p>在第 <code>4</code> 点中，尽管上面所说的只包含一个两级的层叠，但事实上在一个层叠上下文中，一共可以有<strong>7种层叠等级</strong>。<strong>具体如下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/731ab2d1cdaf4215963b81b083fa3c03~tplv-k3u1fbpfcp-watermark.image" alt="7种层叠层级" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面我们来一一对上面的7种层叠顺序进行阐述。<strong>说明如下：</strong></p>
<ul>
<li><strong>背景和边框</strong> —— 形成层叠上下文的元素的背景和边框，也是层叠上下文中的<strong>最低等级</strong>。</li>
<li><strong>负z-index值</strong> —— 层叠上下文内有着 <code>负z-index值</code> 的子元素。</li>
<li><strong>块级盒</strong> —— 文档流中非行内非定位子元素。</li>
<li><strong>浮动盒</strong> —— 非定位浮动元素。</li>
<li><strong>行内盒</strong> —— 文档流中行内级别非定位子元素。</li>
<li><strong>z-index: 0</strong> —— 定位元素，这些元素将形成了新的层叠上下文。</li>
<li><strong>正z-index值</strong> —— 定位元素。 层叠上下文中的最高等级。</li>
</ul>
<p><strong>注：</strong> 字体颜色对应框内颜色</p>
<p>以上这七个层叠等级构成了层叠次序的规则。比如， 在<strong>层叠等级七</strong>上的元素会比在<strong>等级一至六</strong>上的元素显示得更上方（更靠近观察者）。 在层叠等级四上的元素会显示在<strong>等级一至三</strong>上的元素之上。</p>
<p>看到上面这张图的时候，我想到了一些坑。</p>
<p>如果你只看层叠等级 <code>2</code> ,  <code>6</code> ,  <code>7</code> （也就是那些提到了 <code>z-index</code> 的等级），那么有很大的可能你会发现这跟你理解的 <code>z-index</code> 可能是一样的。 正 <code>z-index</code> 值比  <code>z-index:0</code> 值更高一层， <code>z-index:0</code> 值又比负 <code>z-index</code> 值高一层。 往往我们很多时候都只理解到了这里，也就觉得 <code>z-index</code> 只有这些内容，往后的事也不了了之了。</p>
<p>但事实上，事实与现实总是不相符的。一般来说，大多数的元素都比 <code>z-index:0</code> 和 <code>z-index > 0</code> 时的层叠等级要低。</p>
<p>另外同样有趣的是非定位元素分散在四个不同的层叠等级上，为什么是这样子的呢？其实，你可以想象以下，如果所有的非定位元素都在<strong>同一层叠等级</strong>上，那么我们也就不会看到文字（行内盒）在 <code>div</code> 盒子上了（块级盒）。</p>
<h2 data-id="heading-22">7. 例子展示</h2>
<p>讲到这里，相信大家对 <code>z-index</code> 已经有了一定的认知。接下来呢，我们就就来用一个例子巩固一下上面所学到的知识🌈</p>
<p><strong>先附上代码：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"09.scss"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
&#125;
 
<span class="hljs-selector-class">.ele1</span>, <span class="hljs-selector-class">.ele2</span>, <span class="hljs-selector-class">.ele3</span>, <span class="hljs-selector-class">.ele4</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
&#125;
  
<span class="hljs-selector-class">.ele1</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#38a3a5</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">z-index</span>: <span class="hljs-number">10</span>;
&#125;
  
<span class="hljs-selector-class">.ele2</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#99d98c</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">75px</span>;
  <span class="hljs-attribute">z-index</span>: <span class="hljs-number">100</span>;
&#125;
 
<span class="hljs-selector-class">.ele3</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#57cc99</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">125px</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">25px</span>;
  <span class="hljs-attribute">z-index</span>: <span class="hljs-number">150</span>;
&#125;
 
<span class="hljs-selector-class">.ele4</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#80ed99</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">350px</span>;
  <span class="hljs-attribute">z-index</span>: <span class="hljs-number">50</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ele1"</span>></span>
        1
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ele2"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ele3"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ele4"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家可以先想象一下具体的层叠顺序，然后再来看结果。<strong>接下来看一下演示效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0da6b2a47b424a2bba9442ec7b6dd6c4~tplv-k3u1fbpfcp-watermark.image" alt="演示图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不知道最终的结果是都跟小伙伴们心里的预期是一样的呢。很多小伙伴可能想着， <code>ele4</code> 的 <code>z-index</code> 值不是 <code>50</code> 吗，而 <code>ele2</code> 和 <code>ele3</code> 的 <code>z-index</code> 值是 <code>100</code> 和 <code>200</code> ，为什么反而是 <code>ele4</code> 在最上面呢。我们来解决这个疑惑。</p>
<p>其实， <code>ele1</code> 和 <code>ele4</code> 是两个不同的层叠上下文，而 <code>ele2</code> 和 <code>ele3</code> 是 <code>ele1</code> 的层叠上下文元素。所以， <code>ele1</code> 的值是 <code>10</code> ，而 <code>ele2</code> 和 <code>ele3</code> 可以理解为是 <code>10.100</code> 和 <code>10.150</code> ，这样，自然地，<code>ele4</code> 肯定就是在最上方了。</p>
<p>还有另外一种特殊情况就是， <code>ele4</code> 的 <code>z-index</code> 的值跟 <code>ele1</code> 的值是一样的，都是 <code>10</code> 。在这种情况下，如果遇到在同一个层叠上下文的元素，他们的 <code>z-index</code> 值如果一样的话，那得遵循个<strong>先来后到</strong>原则。 <code>ele1</code> 先出现了，所以它在里面；而 <code>ele4</code> 后出现，它在外面。</p>
<p>那如果遇到 <code>ele4</code> 的 <code>z-index</code> 的值是 <code>9</code> 呢？我们改一下 <code>ele4</code> 的 <code>css</code> 样式，然后来观察一下效果。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.ele4</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#80ed99</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>具体效果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d6dcd88efb42f6a6227a41b8503ae5~tplv-k3u1fbpfcp-watermark.image" alt="演示效果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上图，大家可以发现，<code>ele4</code> 的 <code>z-index</code> 值比 <code>ele1</code> 小，所以自然地， <code>ele4</code> 在里面， <code>ele1</code> 在外面。</p>
<h1 data-id="heading-23">🥂四、结束语</h1>
<p>当你初次遇到 <code>z-index</code> 时，它就像一个非常简单、易于理解的属性。 它的值代表着在朝向屏幕内外面轴上的位置。而深入探究 <code>z-index</code> 以后我们还发现了很多 <code>z-index</code> 背后的事情， 包括层叠上下文、层叠等级和层叠次序规则等等。</p>
<p>所以说呀，万宗不变其一，万事万物还是得追溯到源头上才能更好的解决问题本身。</p>
<p>相信通过上文的了解，大家对 <code>position</code> 和 <code>z-index</code> 又有了一个全新的认识~</p>
<h1 data-id="heading-24">🐣彩蛋 One More Thing</h1>
<h2 data-id="heading-25">（：参考资料</h2>
<p>长安曹公子👉<a href="https://juejin.cn/post/6844903667175260174" target="_blank" title="https://juejin.cn/post/6844903667175260174">彻底搞懂CSS层叠上下文、层叠等级、层叠顺序、z-index</a></p>
<p>Steven Bradley👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebdesign.tutsplus.com%2Fzh-hans%2Farticles%2Fwhat-you-may-not-know-about-the-z-index-property--webdesign-16892" target="_blank" rel="nofollow noopener noreferrer" title="https://webdesign.tutsplus.com/zh-hans/articles/what-you-may-not-know-about-the-z-index-property--webdesign-16892" ref="nofollow noopener noreferrer">关于z-index 那些你不知道的事</a></p>
<p>猫儿不熊👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Ffe_flyfish%2Farticle%2Fdetails%2F74279163" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/fe_flyfish/article/details/74279163" ref="nofollow noopener noreferrer">CSS-position:static/relative/absolute/fixed定位</a></p>
<p>书籍👉<a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">张鑫旭老师的CSS世界</a></p>
<h2 data-id="heading-26">（：番外篇</h2>
<blockquote>
<ul>
<li>
<p>关注公众号<strong>星期一研究室</strong>，第一时间关注优质文章，<strong>更多精选专栏待你解锁</strong>~</p>
</li>
<li>
<p>如果这篇文章对你有用，记得<strong>留个脚印jio</strong>再走哦~</p>
</li>
<li>
<p>以上就是本文的全部内容！我们下期见！👋👋👋</p>
</li>
</ul>
</blockquote></div>  
</div>
            