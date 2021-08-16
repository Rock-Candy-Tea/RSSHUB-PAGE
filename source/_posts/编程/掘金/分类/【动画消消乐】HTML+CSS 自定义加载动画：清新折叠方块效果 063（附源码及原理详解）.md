
---
title: '【动画消消乐】HTML+CSS 自定义加载动画：清新折叠方块效果 063（附源码及原理详解）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ca6599d41104925a20631e70a21cf14~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 21:47:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ca6599d41104925a20631e70a21cf14~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">前言</h1>
<blockquote>
<p>Hello！小伙伴！</p>
<p>非常感谢您阅读海轰的文章，倘若文中有错误的地方，欢迎您指出～</p>
<p>自我介绍<strong>ଘ(੭ˊᵕˋ)੭</strong></p>
<p>昵称：海轰</p>
<p>标签：程序猿｜C++选手｜学生</p>
<p>简介：因C语言结识编程，随后转入计算机专业，有幸拿过国奖、省奖等，已保研。目前正在学习C++/Linux（真的真的太难了～）</p>
<p>学习经验：扎实基础 + 多做笔记 + 多敲代码 + 多思考 + 学好英语！</p>
<p>【动画消消乐】 平时学习生活比较枯燥，无意之间对一些网页、应用程序的过渡/加载动画产生了浓厚的兴趣，想知道具体是如何实现的？ 便在空闲的时候学习下如何使用css实现一些简单的动画效果，文章仅供作为自己的学习笔记，记录学习生活，争取理解动画的原理，多多“消灭”动画！</p>
</blockquote>
<h1 data-id="heading-1">效果展示</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ca6599d41104925a20631e70a21cf14~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">Demo代码</h1>
<p>HTML</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"style.css"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">section</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">html</span>, <span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;

<span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#ed556a</span>;
  <span class="hljs-comment">/* background-color: #82466e; */</span>
  <span class="hljs-attribute">animation</span>: backColor <span class="hljs-number">4s</span> infinite;
&#125;

<span class="hljs-selector-tag">section</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">650px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid white;
&#125;

<span class="hljs-selector-tag">span</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">48px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">48px</span>;
  <span class="hljs-attribute">background-color</span>: goldenrod;
  <span class="hljs-attribute">display</span>: inline-block;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>);
&#125;

<span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::before</span> &#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">top</span>: -<span class="hljs-number">24px</span>;
  <span class="hljs-attribute">animation</span>: loading_1 <span class="hljs-number">4s</span> ease infinite;
&#125;

<span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::after</span> &#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.85</span>);
  <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.15</span>);
  <span class="hljs-attribute">animation</span>: loading_2 <span class="hljs-number">2s</span> ease infinite;
&#125;

<span class="hljs-keyword">@keyframes</span> loading_1 &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>)
  &#125;
  <span class="hljs-number">12%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>)
  &#125;
  <span class="hljs-number">25%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>)
  &#125;
  <span class="hljs-number">37%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>)
  &#125;
  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>)
  &#125;
  <span class="hljs-number">62%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>)
  &#125;
  <span class="hljs-number">75%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>)
  &#125;
  <span class="hljs-number">87%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1</span>)
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">24px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">24px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>), <span class="hljs-number">0px</span> <span class="hljs-number">48px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0</span>)
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> loading_2 &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">0</span>) <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">0</span>)
  &#125;
  <span class="hljs-number">25%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">100%</span>, <span class="hljs-number">0</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">0</span>) <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>)
  &#125;
  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">100%</span>, <span class="hljs-number">100%</span>) <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">180deg</span>) <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>)
  &#125;
  <span class="hljs-number">75%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">100%</span>) <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">180deg</span>) <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">360deg</span>)
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">0</span>) <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">360deg</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">原理详解</h1>
<h3 data-id="heading-4">步骤1</h3>
<p>使用span标签，设置为</p>
<ul>
<li>宽度、高度均为48px</li>
<li>背景色：棕色</li>
<li>相对定位</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">span &#123;
  width: 48px;
  height: 48px;
  background-color: goldenrod;
  position: relative;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7db119100ae34603976b11ba7d4084c3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">步骤2</h3>
<p>使用span::before伪元素，设置为</p>
<ul>
<li>绝对定位（  left: 0   top: -24px）</li>
<li>宽度、高度均为24px</li>
<li>背景色：白色</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">span::before &#123;
  content: '';
  width: 24px;
  height: 24px;
  position: absolute;
  background-color: #fff;
  left: 0;
  top: -24px;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aeefb8b3888b4281865d855b0a9dbcb4~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">步骤3</h3>
<p>使用box-shadow为span::before设置四个阴影</p>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">span::before &#123;
  box-shadow: 0 24px red, /* 阴影1 */
  24px 24px orange, /* 阴影2 */
  24px 48px yellow,/* 阴影3 */
  0px 48px green;/* 阴影4 */
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>四个阴影位置关系如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25deb377910d40e0ad53939aa8eb2e2a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
注：这里为了视觉显示区分四个阴影，每个阴影采用了不同的颜色，在实际中其实每个阴影都设置为白色。</p>
<h3 data-id="heading-7">步骤4</h3>
<p>为span::before的四个阴影添加动画loading_1</p>
<p>每个阴影只有两种状态：<strong>显示</strong> 与 <strong>不显示</strong></p>
<p>显示与否则是通过设置颜色的透明级别为0或1</p>
<p>比如</p>
<ul>
<li>阴影显示：0 24px rgba(255, 255, 255, 1)</li>
<li>阴影不显示：0 24px rgba(255, 255, 255, 0)</li>
</ul>
<p>关键有 <strong>九帧</strong></p>
<p>第一帧</p>
<ul>
<li>阴影1、2、3、4均不显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">box-shadow: 0 24px rgba(255, 255, 255, 0), 
24px 24px rgba(255, 255, 255, 0), 
24px 48px rgba(255, 255, 255, 0), 
0px 48px rgba(255, 255, 255, 0);  
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61079b7e11064cc1964f3ea150503cea~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
第二帧</p>
<ul>
<li>阴影1显示</li>
<li>阴影2、3、4不显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">box-shadow: 0 24px rgba(255, 255, 255, 1), 
24px 24px rgba(255, 255, 255, 0), 
24px 48px rgba(255, 255, 255, 0), 
0px 48px rgba(255, 255, 255, 0);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7a95fa7108c4c53ac84b127e741400c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三帧</p>
<ul>
<li>阴影1、2显示</li>
<li>阴影3、4不显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">box-shadow: 0 24px rgba(255, 255, 255, 1), 
24px 24px rgba(255, 255, 255, 1), 
24px 48px rgba(255, 255, 255, 0),
0px 48px rgba(255, 255, 255, 0);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1336d687ac9e41e88e84d6b9c1529091~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第四帧</p>
<ul>
<li>阴影1、2、3显示</li>
<li>阴影4不显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">box-shadow: 0 24px rgba(255, 255, 255, 1), 
24px 24px rgba(255, 255, 255, 1), 
24px 48px rgba(255, 255, 255, 1), 
0px 48px rgba(255, 255, 255, 0);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69e1a7362f0f4fb2be64786b9c7faf5c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第五帧</p>
<ul>
<li>阴影1、2、3、4都显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">box-shadow: 0 24px rgba(255, 255, 255, 1), 
24px 24px rgba(255, 255, 255, 1), 
24px 48px rgba(255, 255, 255, 1), 
0px 48px rgba(255, 255, 255, 1);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d154913e11f418d97367fc8a992c21e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第六帧</p>
<ul>
<li>阴影2、3、4显示</li>
<li>阴影1不显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml"> box-shadow: 0 24px rgba(255, 255, 255, 0), 
 24px 24px rgba(255, 255, 255, 1), 
 24px 48px rgba(255, 255, 255, 1), 
 0px 48px rgba(255, 255, 255, 1);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21ad7f7ef0b34a618b7de564fc619668~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第七帧</p>
<ul>
<li>阴影3、4显示</li>
<li>阴影1、2不显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml"> box-shadow: 0 24px rgba(255, 255, 255, 0), 
 24px 24px rgba(255, 255, 255, 0), 
 24px 48px rgba(255, 255, 255, 1), 
 0px 48px rgba(255, 255, 255, 1);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df8b290a51dc4570922f1afc50de2f8a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第八帧</p>
<ul>
<li>阴影4显示</li>
<li>阴影1、2、3不显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">box-shadow: 0 24px rgba(255, 255, 255, 0), 
24px 24px rgba(255, 255, 255, 0), 
24px 48px rgba(255, 255, 255, 0), 
0px 48px rgba(255, 255, 255, 1);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ed72e52349c4418a9b1bfe57852d833~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第九帧</p>
<ul>
<li>阴影1、2、3、4均不显示</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">box-shadow: 0 24px rgba(255, 255, 255, 0), 
24px 24px rgba(255, 255, 255, 0), 
24px 48px rgba(255, 255, 255, 0), 
0px 48px rgba(255, 255, 255, 0);  
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a77e56bb3e044b49e66fbc604fff9e3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置动画animation使得从第一帧平稳过渡至第九帧</p>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">animation: loading_1 4s ease infinite;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">
@keyframes loading_1 &#123;
  0% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 0), 24px 24px rgba(255, 255, 255, 0), 24px 48px rgba(255, 255, 255, 0), 0px 48px rgba(255, 255, 255, 0)
  &#125;
  12% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 1), 24px 24px rgba(255, 255, 255, 0), 24px 48px rgba(255, 255, 255, 0), 0px 48px rgba(255, 255, 255, 0)
  &#125;
  25% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 1), 24px 24px rgba(255, 255, 255, 1), 24px 48px rgba(255, 255, 255, 0), 0px 48px rgba(255, 255, 255, 0)
  &#125;
  37% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 1), 24px 24px rgba(255, 255, 255, 1), 24px 48px rgba(255, 255, 255, 1), 0px 48px rgba(255, 255, 255, 0)
  &#125;
  50% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 1), 24px 24px rgba(255, 255, 255, 1), 24px 48px rgba(255, 255, 255, 1), 0px 48px rgba(255, 255, 255, 1)
  &#125;
  62% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 0), 24px 24px rgba(255, 255, 255, 1), 24px 48px rgba(255, 255, 255, 1), 0px 48px rgba(255, 255, 255, 1)
  &#125;
  75% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 0), 24px 24px rgba(255, 255, 255, 0), 24px 48px rgba(255, 255, 255, 1), 0px 48px rgba(255, 255, 255, 1)
  &#125;
  87% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 0), 24px 24px rgba(255, 255, 255, 0), 24px 48px rgba(255, 255, 255, 0), 0px 48px rgba(255, 255, 255, 1)
  &#125;
  100% &#123;
    box-shadow: 0 24px rgba(255, 255, 255, 0), 24px 24px rgba(255, 255, 255, 0), 24px 48px rgba(255, 255, 255, 0), 0px 48px rgba(255, 255, 255, 0)
  &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9cad5c3a7494f388c77df79a0171c29~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">步骤5</h3>
<p>取消span::before的背景色</p>
<p>将此时形成的动画定义为<strong>动画1</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79598fe6954a486db1e54f59d9387983~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">步骤6</h3>
<p>先忽略span::before形成的动画，暂时注释掉</p>
<p>使用span::after伪元素，设置为</p>
<ul>
<li>绝对定位（top：0 left：0）</li>
<li>宽带、高度均为24px</li>
<li>背景色：白色，透明级别：0.85</li>
<li>阴影：0 0 10px rgba(0, 0, 0, 0.15);</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">span::after &#123;
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 24px;
  height: 24px;
  background: rgba(255, 255, 255, 0.85);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52126db9a90c421582fb0d84b2a59be3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">步骤7</h3>
<p>为span::after添加动画</p>
<p>有<strong>5个关键帧</strong></p>
<p>第一帧（初始状态）</p>
<ul>
<li>二维空间：右移：0 下移：0</li>
<li>三维空间：绕x轴旋转0度 绕y轴旋转0度</li>
</ul>
<pre><code class="hljs language-clike copyable" lang="clike"> transform: translate(0, 0) rotateX(0) rotateY(0)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二帧（相对于初始状态）</p>
<ul>
<li>二维空间：右移：100% 下移：0 （100%是指相对于自身的大小，若自身宽100px 那就移动100px）</li>
<li>三维空间：绕x轴旋转0度 绕y轴旋转180度</li>
</ul>
<pre><code class="hljs language-clike copyable" lang="clike">transform: translate(100%, 0) rotateX(0) rotateY(180deg)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一帧 过渡至 第二帧 效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51898746828d4bb196007c73e66b2020~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三帧 <strong>（相对于初始状态）</strong></p>
<ul>
<li>二维空间：右移：100% 下移：100%</li>
<li>三维空间：绕x轴旋转-180度 绕y轴旋转180度</li>
</ul>
<pre><code class="hljs language-clike copyable" lang="clike">  transform: translate(100%, 100%) rotateX(-180deg) rotateY(180deg)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二帧 过渡至  第三帧 效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3603754afc3488cb5cc55597c9d73ed~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第四帧（相对于初始状态）</p>
<ul>
<li>二维空间：右移：0 下移：100%</li>
<li>三维空间：绕x轴旋转-180度 绕y轴旋转360度</li>
</ul>
<pre><code class="hljs language-clike copyable" lang="clike">transform: translate(0, 100%) rotateX(-180deg) rotateY(360deg)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三帧 过渡至 第四帧 效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef07c7fe2e5b4645aafbd79b7e0d227f~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
第五帧（相对于初始状态）</p>
<ul>
<li>二维空间：右移：0 下移：0</li>
<li>三维空间：绕x轴旋转0度 绕y轴旋转360度</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">transform: translate(0, 0) rotateX(0) rotateY(360deg)；
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>第四帧 过渡至 第五帧 效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d23804b005f44b7b5f558e1eae01889~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置动画从第一帧过渡至第五帧</p>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml"> animation: loading_2 2s ease infinite;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">@keyframes loading_2 &#123;
  0% &#123;
    transform: translate(0, 0) rotateX(0) rotateY(0)
  &#125;
  25% &#123;
    transform: translate(100%, 0) rotateX(0) rotateY(180deg)
  &#125;
  50% &#123;
    transform: translate(100%, 100%) rotateX(-180deg) rotateY(180deg)
  &#125;
  75% &#123;
    transform: translate(0, 100%) rotateX(-180deg) rotateY(360deg)
  &#125;
  100% &#123;
    transform: translate(0, 0) rotateX(0) rotateY(360deg)
  &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>将此动画定义为动画2</strong></p>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4d381ed49a84106b61c75fff88d04ce~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">步骤8</h3>
<p>动画1为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5db59b652ebd44b9a3e3576f5f97f92c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
动画2为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b13484d628a04fdca21cde26b31311ce~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>将动画1与动画2叠加</strong></p>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94457f3650f34be3a9afeb4928a877ad~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">步骤9</h3>
<p>将span旋转45度</p>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">span &#123;
  transform: rotate(45deg);
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6abdc9f3fc9b47feb490f1778e4e9e14~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">步骤10</h3>
<p>取消span背景色</p>
<p>得到最终效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeb663de1d954376bb11ab0117422ba8~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">结语</h1>
<p>文章仅作为学习笔记，记录从0到1的一个过程</p>
<p>希望对您有所帮助，如有错误欢迎小伙伴指正～</p>
<p>我是<strong>海轰ଘ(੭ˊᵕˋ)੭</strong>，如果您觉得写得可以的话，请点个赞吧</p>
<p>谢谢支持❤️
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30324a8ed2b94d10bc01ea2cf97dd5db~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            