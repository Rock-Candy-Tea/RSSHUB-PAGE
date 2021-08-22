
---
title: '【动画消消乐】HTML+CSS 白云飘动效果 072'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c63c67c4212845bea968cb659a6f2f2e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 23:53:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c63c67c4212845bea968cb659a6f2f2e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第22天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
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
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c63c67c4212845bea968cb659a6f2f2e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
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
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#93b5cf</span>;
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
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">animation</span>: cloud <span class="hljs-number">5s</span> ease-in-out infinite;
  <span class="hljs-attribute">background</span>: white;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">box-shadow</span>: white <span class="hljs-number">65px</span> -<span class="hljs-number">15px</span> <span class="hljs-number">0</span> -<span class="hljs-number">4px</span>, white <span class="hljs-number">25px</span> -<span class="hljs-number">25px</span>, white <span class="hljs-number">30px</span> <span class="hljs-number">10px</span>, white <span class="hljs-number">60px</span> <span class="hljs-number">15px</span> <span class="hljs-number">0</span> -<span class="hljs-number">10px</span>, white <span class="hljs-number">85px</span> <span class="hljs-number">5px</span> <span class="hljs-number">0</span> -<span class="hljs-number">5px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">60px</span>;
&#125;

<span class="hljs-selector-tag">span</span>:after &#123;
  animation: cloud_shadow <span class="hljs-number">5s</span> ease-in-out infinite;
  <span class="hljs-attribute">background</span>: black;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">15px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">120px</span>;
  <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.2</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">5px</span>;
  <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">60px</span>;
&#125;

<span class="hljs-keyword">@keyframes</span> cloud &#123;
  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">20px</span>);
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> cloud_shadow &#123;
  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(<span class="hljs-number">0px</span>) <span class="hljs-built_in">scale</span>(.<span class="hljs-number">7</span>);
    <span class="hljs-attribute">opacity</span>: .<span class="hljs-number">05</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">原理详解</h1>
<h3 data-id="heading-4">步骤1</h3>
<p>使用span标签，设置为</p>
<ul>
<li>相对定位</li>
<li>宽度、高度均为50px</li>
<li>背景色：白色</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">span</span> &#123;
  <span class="hljs-attribute">background</span>: white;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">position</span>: relative;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47febcd3decd49858395ffda30ebe793~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">步骤2</h3>
<p>利用box-shadow属性，为span添加5个阴影</p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-attribute">box-shadow</span>:  red <span class="hljs-number">65px</span> -<span class="hljs-number">15px</span> <span class="hljs-number">0</span> -<span class="hljs-number">4px</span>,   /*阴影<span class="hljs-number">1</span>*/
              orange <span class="hljs-number">25px</span> -<span class="hljs-number">25px</span>,       /*阴影<span class="hljs-number">2</span>*/
              yellow <span class="hljs-number">30px</span> <span class="hljs-number">10px</span>,        /*阴影<span class="hljs-number">3</span>*/
              green <span class="hljs-number">60px</span> <span class="hljs-number">15px</span> <span class="hljs-number">0</span> -<span class="hljs-number">10px</span>, /*阴影<span class="hljs-number">4</span>*/
              blue <span class="hljs-number">85px</span> <span class="hljs-number">5px</span> <span class="hljs-number">0</span> -<span class="hljs-number">5px</span>;    <span class="hljs-comment">/*阴影5*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/390376cff5da4c49a5de33bda81a78a7~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">步骤3</h3>
<p>span圆角化</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">span</span> &#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44d45ea2c53045b6adfbe0fd90d7c9e8~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">步骤4</h3>
<p>将5个阴影的颜色都修改为白色</p>
<pre><code class="hljs language-css copyable" lang="css">  <span class="hljs-attribute">box-shadow</span>: white <span class="hljs-number">65px</span> -<span class="hljs-number">15px</span> <span class="hljs-number">0</span> -<span class="hljs-number">4px</span>,   /*阴影<span class="hljs-number">1</span>*/
              white <span class="hljs-number">25px</span> -<span class="hljs-number">25px</span>,          /*阴影<span class="hljs-number">2</span>*/
              white <span class="hljs-number">30px</span> <span class="hljs-number">10px</span>,           /*阴影<span class="hljs-number">3</span>*/
              white <span class="hljs-number">60px</span> <span class="hljs-number">15px</span> <span class="hljs-number">0</span> -<span class="hljs-number">10px</span>,   /*阴影<span class="hljs-number">4</span>*/
              white <span class="hljs-number">85px</span> <span class="hljs-number">5px</span> <span class="hljs-number">0</span> -<span class="hljs-number">5px</span>;     <span class="hljs-comment">/*阴影5*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1d29a4fc76647ce8c5c17b117422800~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">步骤5</h3>
<p>将span左移60px</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">span</span> &#123;
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">60px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到一朵小白云</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93f56db0b7524672af12f37ac177231d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">步骤6</h3>
<p>为span添加动画</p>
<p>动画效果描述为：白云上下移动</p>
<p>使用translateY属性对span进行y轴（竖直方向）的上下移动</p>
<ul>
<li>初始（0%）：原位置</li>
<li>中间（50%）：向上移动20px</li>
<li>末尾（100%）：原位置</li>
</ul>
<p>animation动画代码为：</p>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">animation: cloud 5s ease-in-out infinite;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@keyframes</span> cloud &#123;
<span class="hljs-comment">/*忽略0% 100% 因为span需要回到原位置*/</span>
  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">20px</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96efedaffb7c4e28b3c2e9ba678c8eef~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">步骤7</h3>
<p>使用span::after伪元素充当白云的阴影，设置为</p>
<ul>
<li>绝对定位（  left: 5px  bottom: -60px）</li>
<li>高度15px 宽度120px</li>
<li>背景色：黑色</li>
<li>颜色透明度：0.2</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">span:after &#123;
  background: black;
  content: '';
  height: 15px;
  width: 120px;
  opacity: 0.2;
  position: absolute;
  left: 5px;
  bottom: -60px;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9164f90d3a0448ea3341d3af65ba3f8~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">步骤8</h3>
<p>span::after圆角化</p>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">span:after &#123;
  border-radius: 50%;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69fa7ec21fa6404d93caa16167e74a1b~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">步骤9</h3>
<p>为span::after添加动画</p>
<p>效果</p>
<ul>
<li>当白云向上移动，阴影变小，颜色变浅；</li>
<li>向下移动，阴影变大，颜色变深</li>
</ul>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">span:after &#123;
  animation: cloud_shadow 5s ease-in-out infinite;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-handlebars copyable" lang="handlebars"><span class="xml">@keyframes cloud_shadow &#123;
  50% &#123;
    transform: translateY(20px) scale(.7);
    opacity: .05;
  &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/494d74b7dcff4d7ab5dcfec3a7408871~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：从效果图中可以发现，其实阴影部分只是大小、颜色深度在发生变化，其位置是没有发生变化的。这是因为span动画中50%时刻，span执行translateY(-20px)，倘若span::after没有执行translateY(20px)，那么span::after将一起移动20px。（这里本质就是两个效果相抵消；了，所以span::after的位置没有发生变化）</p>
</blockquote>
<p>如果span::after没有设置translateY(20px)</p>
<p>那么就会出现下面的效果：阴影上下也在移动</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd06b893e7e74ad3a1cda27ec2f9a9bf~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-13">结语</h1>
<p>文章仅作为学习笔记，记录从0到1的一个过程</p>
<p>希望对您有所帮助，如有错误欢迎小伙伴指正～</p>
<p>我是<strong>海轰ଘ(੭ˊᵕˋ)੭</strong>，如果您觉得写得可以的话，请点个赞吧</p>
<p>谢谢支持❤️
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78959848d89b46b18f035ea43578d6b4~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            