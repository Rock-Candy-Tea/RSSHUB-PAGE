
---
title: '前端必知必会 _ 学SVG看这篇就够了（八）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0ec97defa0e43b9ab881e2aac2c725a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 08:29:49 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0ec97defa0e43b9ab881e2aac2c725a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">这是SVG系列目录：</h3>
<ul>
<li><a href="https://juejin.cn/post/6993211337509699620" target="_blank" title="https://juejin.cn/post/6993211337509699620">前端必知必会 | 学SVG看这篇就够了（一）</a></li>
<li><a href="https://juejin.cn/post/6993607549576544270" target="_blank" title="https://juejin.cn/post/6993607549576544270">前端必知必会 | 学SVG看这篇就够了（二）</a></li>
<li><a href="https://juejin.cn/post/6994024417001111560" target="_blank" title="https://juejin.cn/post/6994024417001111560">前端必知必会 | 学SVG看这篇就够了（三）</a></li>
<li><a href="https://juejin.cn/post/6994432253484859406" target="_blank" title="https://juejin.cn/post/6994432253484859406">前端必知必会 | 学SVG看这篇就够了（四）</a></li>
<li><a href="https://juejin.cn/post/6994790295439327269" target="_blank" title="https://juejin.cn/post/6994790295439327269">前端必知必会 | 学SVG看这篇就够了（五）</a></li>
<li><a href="https://juejin.cn/post/6995081482851057671" target="_blank" title="https://juejin.cn/post/6995081482851057671">前端必知必会 | 学SVG看这篇就够了（六）</a></li>
<li><a href="https://juejin.cn/post/6995479935666094094" target="_blank" title="https://juejin.cn/post/6995479935666094094">前端必知必会 | 学SVG看这篇就够了（七）</a></li>
</ul>
<h4 data-id="heading-1">前言</h4>
<p>在SVG中有两种截然不同的文本模式. 一种是写在图像中的文本，另一种是SVG字体。关于后者我们将在教程的后面进行讲解，现在我们主要集中前者：写在图像中的文本。</p>
<h4 data-id="heading-2">text</h4>
<p>text标签用于在画布中，放置任何的文字。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文字的内容写在text标签体中，x和y分别代表文本在画布中显示的位置。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0ec97defa0e43b9ab881e2aac2c725a~tplv-k3u1fbpfcp-watermark.image" alt="38.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">text-anchor</h5>
<p>该属性用于设置文本从坐标点中的文本流方向，值分别是start、end、middle、inherit。从下面图中可以看到四种值的不同。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">text-anchor</span>=<span class="hljs-string">"start"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">text-anchor</span>=<span class="hljs-string">"end"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"80"</span> <span class="hljs-attr">text-anchor</span>=<span class="hljs-string">"middle"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"110"</span> <span class="hljs-attr">text-anchor</span>=<span class="hljs-string">"inherit"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5fd8246cf3143ad92b50cd302d92178~tplv-k3u1fbpfcp-watermark.image" alt="39.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">fill</h5>
<p>和其他图形一样，text也可以使用fill属性对主题进行颜色填充。也用引用渐变、图案进行填充。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">linearGradient</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"fillTest"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"5%"</span> <span class="hljs-attr">stop-color</span>=<span class="hljs-string">"#fc5c7d"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"85%"</span> <span class="hljs-attr">stop-color</span>=<span class="hljs-string">"#6a82fb"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">linearGradient</span>></span>
<span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"red"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"green"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"60"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#ee2"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"80"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"rgb(255,0,0)"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"url(#fillTest)"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63a3afa74be3430b962c3f01f582d572~tplv-k3u1fbpfcp-watermark.image" alt="40.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-5">stroke</h5>
<p>同样，我们也可以给字体设置描边。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">linearGradient</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"strTest"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"5%"</span> <span class="hljs-attr">stop-color</span>=<span class="hljs-string">"#00f260"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"85%"</span> <span class="hljs-attr">stop-color</span>=<span class="hljs-string">"#0575e6"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">linearGradient</span>></span>
<span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"red"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"green"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"60"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#ee2"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"80"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"rgb(255,0,0)"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"url(#strTest)"</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9518eb02a2048b888fd3cb02a29e243~tplv-k3u1fbpfcp-watermark.image" alt="41.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">tspan</h5>
<p>该元素用来标记大块文本的子部分，它必须是一个<code>text</code>元素或别的<code>tspan</code>元素的子元素。一个典型的用法是把句子中的一个词变成粗体，突出重点。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span>></span>
    坐标：
    <span class="hljs-tag"><<span class="hljs-name">tspan</span> <span class="hljs-attr">font-weight</span>=<span class="hljs-string">"bold"</span>></span>
        广州
    <span class="hljs-tag"></<span class="hljs-name">tspan</span>></span>
<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcc2c91ccb0c47b7a05b0fc60d848e92~tplv-k3u1fbpfcp-watermark.image" alt="42.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>tspan</code>标签还有以下几种属性：</p>

























<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>x</td><td>为容器设置一个新绝对<code>x</code>坐标。它覆盖了默认的当前的文本位置。这个属性可以包含一个数列，它们将一个一个地应用到<code>tspan</code>元素内的每一个字符上。</td></tr><tr><td>y</td><td>为容器设置一个新绝对<code>y</code>坐标。它覆盖了默认的当前的文本位置。这个属性可以包含一个数列，它们将一个一个地应用到<code>tspan</code>元素内的每一个字符上。</td></tr><tr><td>dx</td><td>从当前位置，用一个水平偏移开始绘制文本。这里，你可以提供一个值数列，可以应用到连续的字体，因此每次累积一个偏移。</td></tr><tr><td>dy</td><td>从当前位置，用一个垂直偏移开始绘制文本。这里，你可以提供一个值数列，可以应用到连续的字体，因此每次累积一个偏移。</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span>></span>
    坐标：
    <span class="hljs-tag"><<span class="hljs-name">tspan</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">font-weight</span>=<span class="hljs-string">"bold"</span>></span>
        广州
    <span class="hljs-tag"></<span class="hljs-name">tspan</span>></span>
<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d18b64705ed4cb4a8c656f10d6f5529~tplv-k3u1fbpfcp-watermark.image" alt="43.png" loading="lazy" referrerpolicy="no-referrer"></p>













<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>rotate</td><td>把所有的字符旋转一个角度。如果是一个数列，则使每个字符旋转分别旋转到那个值，剩下的字符根据最后一个值旋转。</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">tspan</span> <span class="hljs-attr">rotate</span>=<span class="hljs-string">"18"</span>></span>
        hello world
    <span class="hljs-tag"></<span class="hljs-name">tspan</span>></span>
<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70fa627823ee4f5999957132c10960a7~tplv-k3u1fbpfcp-watermark.image" alt="44.png" loading="lazy" referrerpolicy="no-referrer"></p>













<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>textLength</td><td>这是一个很模糊的属性，给出字符串的计算长度。它意味着如果它自己的度量文字和长度不满足这个提供的值，则允许渲染引擎精细调整字型的位置。</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">tspan</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">textLength</span>=<span class="hljs-string">"80"</span>></span>
        hello world
    <span class="hljs-tag"></<span class="hljs-name">tspan</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">tspan</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">textLength</span>=<span class="hljs-string">"110"</span>></span>
        hello world
    <span class="hljs-tag"></<span class="hljs-name">tspan</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">tspan</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"60"</span> <span class="hljs-attr">textLength</span>=<span class="hljs-string">"140"</span>></span>
        hello world
    <span class="hljs-tag"></<span class="hljs-name">tspan</span>></span>
<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6e5decc62584d54a30c287d8f3f5208~tplv-k3u1fbpfcp-watermark.image" alt="45.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-7">其他字体相关属性</h5>
<p>下面这些属性可以在<code>text</code>标签中直接设置成一个属性，或是在<code>CSS</code>中声明。</p>





















































<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>font-family</td><td>设置文本的字体系列</td></tr><tr><td>font-style</td><td>设置斜体文字的字体样式属性</td></tr><tr><td>font-weight</td><td>设置字体的粗细</td></tr><tr><td>font-variant</td><td>在小型大写字母和普通文本选项之间切换</td></tr><tr><td>font-stretch</td><td>在给定字体的可选拉伸版本中切换</td></tr><tr><td>font-size</td><td>设置文本的大小</td></tr><tr><td>font-size-adjust</td><td>独立于字体的实际大小尺寸，调整其可视大小尺寸</td></tr><tr><td>kerning</td><td>开启或关闭字体间距选项</td></tr><tr><td>letter-spacing</td><td>设置你的文本中的字母与字母之间的间距</td></tr><tr><td>word-spacing</td><td>设置你的文本中的单词与单词之间的间距</td></tr><tr><td>text-decoration</td><td>设置/取消字体上的文本装饰</td></tr></tbody></table>
<h4 data-id="heading-8">最后</h4>
<p>本篇文章讲述了在<code>SVG</code>中的关于文本标签的使用方法，及它的一些属性。</p>
<p>感谢你的阅读！</p>
<p>😀😀 <strong>关注我，不迷路！</strong> 😀😀</p></div>  
</div>
            