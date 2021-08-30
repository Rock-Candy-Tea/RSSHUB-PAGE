
---
title: '【动画消消乐｜CSS】080.单span标签实现自定义简易过渡动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cb21452431a43d4b0aac8dd06532dee~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 22:21:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cb21452431a43d4b0aac8dd06532dee~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第30天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">前言</h1>
<blockquote>
<p>Hello！小伙伴！</p>
<p>非常感谢您阅读海轰的文章，倘若文中有错误的地方，欢迎您指出～</p>
<p> </p>
<p>自我介绍 <strong>ଘ(੭ˊᵕˋ)੭</strong></p>
<p>昵称：海轰</p>
<p>标签：程序猿｜C++选手｜学生</p>
<p>简介：因C语言结识编程，随后转入计算机专业，有幸拿过国奖、省奖等，已保研。目前正在学习C++/Linux（真的真的太难了～）</p>
<p>学习经验：扎实基础 + 多做笔记 + 多敲代码 + 多思考 + 学好英语！</p>
<p> 
【动画消消乐】 平时学习生活比较枯燥，无意之间对一些网页、应用程序的过渡/加载动画产生了浓厚的兴趣，想知道具体是如何实现的？ 便在空闲的时候学习下如何使用css实现一些简单的动画效果，文章仅供作为自己的学习笔记，记录学习生活，争取理解动画的原理，多多“消灭”动画！</p>
</blockquote>
<h1 data-id="heading-1">效果展示</h1>
<p>难度 🌟</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cb21452431a43d4b0aac8dd06532dee~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
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
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#222f3e</span>;
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
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">5px</span>;
  <span class="hljs-attribute">display</span>: inline-block;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.15</span>);
  <span class="hljs-attribute">overflow</span>: hidden;
&#125;

<span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::after</span> &#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">96px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">5px</span>;
  <span class="hljs-attribute">background</span>: white;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">animation</span>: loading <span class="hljs-number">2s</span> linear infinite alternate;
&#125;

<span class="hljs-keyword">@keyframes</span> loading &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">0%</span>)
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">100%</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">原理详解</h1>
<h3 data-id="heading-4">步骤1</h3>
<p>使用一个span标签</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置为</p>
<ul>
<li>相对定位</li>
<li>宽度为100% 高度为5px</li>
<li>背景颜色为 白色，透明级别为0.15</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css">  <span class="hljs-selector-tag">span</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">5px</span>;
<span class="hljs-attribute">position</span>: relative;
<span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.15</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a31ce0ce471c47bd80b633819ec651f1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">步骤2</h3>
<p>利用span::after作为白色条纹部分</p>
<p>设置为</p>
<ul>
<li>绝对定位（top:0 left:0）</li>
<li>宽度为96px 高度为5px（与span高度保持一致）</li>
<li>背景颜色为白色</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::after</span> &#123;
<span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
<span class="hljs-attribute">width</span>: <span class="hljs-number">96px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">5px</span>;
<span class="hljs-attribute">background</span>: white;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
<span class="hljs-comment">/* animation: loading 2s linear infinite alternate; */</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ffd5b62667d417d8b84b297944e0356~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">步骤3</h3>
<p>为span::after添加动画</p>
<p>使得白色条状部分从左到右运动、再从右到左运动</p>
<p>设置两个关键帧：</p>
<ul>
<li>初始位置：最左端</li>
<li>末尾位置：最右端</li>
</ul>
<p>在最左端时<code>left: 0;</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8d2f6c8a6e64fd689278e48717e4608~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
在最右端时 <code>left: 100%;  transform: translateX(-100%)</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36f8e00cbfdb416e9a9d735c1fb8fbfc~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
css代码</p>
<pre><code class="hljs language-css copyable" lang="css">  <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::after</span> &#123;
<span class="hljs-attribute">animation</span>: loading <span class="hljs-number">2s</span> linear infinite alternate;
  &#125;
  
  <span class="hljs-keyword">@keyframes</span> loading &#123;
<span class="hljs-number">0%</span> &#123;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">0%</span>)
&#125;
<span class="hljs-number">100%</span> &#123;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">100%</span>)
&#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后效果图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c3c7c17b4c34126a1687607f1bfdda9~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">疑点难点</h1>
<p>在最右端时为什么这样设置？ <code>left: 100%;  transform: translateX(-100%)</code> 只写 <code>left: 100%;</code>不行吗？</p>
<p>如果只写 <code>left: 100%;</code> 效果为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a742d9835004a189389c53117e3ce03~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
注：白色边框可以忽略不看 这里只是用来模拟页面边界的</p>
<p>而我们需要的效果是在最右端的时候，是白色条纹的最右端与span的最右端重叠，而不是最左端与span的最右端重叠</p>
<p>所以我们还需要使用<code> transform: translateX(-100%)</code></p>
<p>再将span::after向左移动 相对于自身（span::after）100%宽度 的距离</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2eabd09c7560491e9cf1db40e6450a34~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一定要注意，是相对于span::after自身的宽度！（与left不同 left是相对于span宽度的）</p>
<h1 data-id="heading-8">结语</h1>
<p>文章仅作为学习笔记，记录从0到1的一个过程</p>
<p>希望对您有所帮助，如有错误欢迎小伙伴指正～</p>
<p>我是 <strong>海轰ଘ(੭ˊᵕˋ)੭</strong></p>
<p>如果您觉得写得可以的话，请点个赞吧</p>
<p>谢谢支持❤️
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93b1e988941f4b5595656906707efb3a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            