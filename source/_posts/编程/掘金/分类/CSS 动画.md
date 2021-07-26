
---
title: 'CSS 动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=936'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 07:10:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=936'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">浏览器渲染原理</h1>
<p>浏览器在渲染一个页面的时候，有以下几个步骤：</p>
<ol>
<li>由 HTML 构建 HTML 树（DOM）</li>
<li>由 CSS 构建 CSS 树（CSSOM）</li>
<li>将以上两棵树合并成一棵渲染树（Render Tree）</li>
<li>进行 Layout 布局（依据文档流、盒模型确定大小、位置）</li>
<li>进行 Paint 绘制（内容、色彩）</li>
<li>进行 Compose 合成（依层叠顺序呈现出来）</li>
</ol>
<p>CSS 实现动画的方法，大体上可概括为 transition 法和 animation 法。</p>
<p>在介绍这两种方法前，先要介绍一个非常重要的属性——<code>transform</code>。</p>
<h1 data-id="heading-1">transform</h1>
<p><code>transform</code> 属性可以实现元素的平移、缩放、旋转、倾斜等效果（对 inline 元素无效）。</p>
<p><code>transform</code> 属性常用的值有</p>
<ol>
<li><code>translate()</code></li>
</ol>
<p>可以对元素进行平移</p>
<pre><code class="hljs language-js copyable" lang="js">transform: translateX(50px)               <span class="hljs-comment">/* 向右平移50px */</span>
<span class="hljs-attr">transform</span>: translateY(<span class="hljs-number">50</span>%)                <span class="hljs-comment">/* 向下平移自身高度的50% */</span>
<span class="hljs-attr">transform</span>: translate(20px, 20px)          <span class="hljs-comment">/* 向右、下分别平移20px */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>scale()</code></li>
</ol>
<p>对元素进行缩放</p>
<pre><code class="hljs language-js copyable" lang="js">transform: sacleX(<span class="hljs-number">1.2</span>)                     <span class="hljs-comment">/* 宽放大为原来的1.2倍 */</span>
<span class="hljs-attr">transform</span>: sacle(<span class="hljs-number">1.2</span>)                      <span class="hljs-comment">/* 宽、高均放大为原来的1.2倍 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>rotate()</code></li>
</ol>
<p>对元素进行旋转</p>
<pre><code class="hljs language-js copyable" lang="js">transform: rotate(60deg)                   <span class="hljs-comment">/* 顺时针旋转60度 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><code>skew()</code></li>
</ol>
<p>使元素发生倾斜</p>
<pre><code class="hljs language-js copyable" lang="js">transform: skew(45deg)                     <span class="hljs-comment">/* 倾斜45度 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解了 transform 的基本用法，就可以为元素添加动画了。</p>
<h1 data-id="heading-2">用 transition 实现动画</h1>
<p>transition 就是过渡的意思，作用指定一个行为结尾，transition 会自动添加一个过渡效果。
例如</p>
<pre><code class="hljs language-js copyable" lang="js">div&#123;
  <span class="hljs-attr">height</span>: 50px;
  width: 50px;
  border: 1px solid red;
  transition: transform 1s linear;
&#125;
<span class="hljs-attr">div</span>:hover&#123;
  <span class="hljs-attr">transform</span>: rotate(45deg);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当鼠标 hover 的时候，div 由原来的默认样式变为顺时针旋转45度，transition 使得这两种状态的转变用1s的时间去完成，期间自动补充了过渡动画。</p>
<p>transition 的值包括属性名、持续时间、过渡方式、延迟时间，通常来说属性名和持续时间是必须的。</p>
<ul>
<li>属性名用以指定需要过渡的属性，all 表示所有属性</li>
<li>过渡方式是指，完成这一过渡所遵从的【进度-时间】函数关系模型，诸如匀速变化、先快后慢、先慢后快等等，CSS 提供了多种函数模型，如 linear、ease、ease-in、ease-out 等。</li>
</ul>
<p>需要注意的是，并非所有的属性都支持过渡，像<code>display: none</code>--><code>display: block</code>的变化就不支持，类似的需求可以用<code>visibility: hidden</code>--><code>visibility: visible</code>代替。</p>
<h1 data-id="heading-3">用 animation 实现动画</h1>
<p>transition 动画只能指定两种变化状态，即开始和结束，其中间的过程都由数学函数控制，而 animation 可以指定多个关键帧，相较而言更加灵活。</p>
<p>animation 的核心就是定义关键帧， 这里用的是 <code>@keyframes</code> 语法，写法如下</p>
<pre><code class="hljs language-js copyable" lang="js">@keyframes xxx&#123;
    <span class="hljs-number">0</span>% &#123;样式一&#125;
    <span class="hljs-number">10</span>% &#123;样式二&#125;
    <span class="hljs-number">40</span>% &#123;样式三&#125;
    ...
    <span class="hljs-number">100</span>%&#123;样式四&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="hljs language-js copyable" lang="js">@keyframes xxx&#123;
    <span class="hljs-keyword">from</span> &#123;样式一&#125;
    to &#123;样式二&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 xxx 为动画名字。</p>
<p>声明好关键帧之后，就可以使用 animation 属性为元素应用这个动画了</p>
<pre><code class="hljs language-js copyable" lang="js">div&#123;
    <span class="hljs-attr">animation</span>: xxx 1s infinite alternate-reverse; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>animation 的值包括动画名、时长、过渡方式、延迟、次数、方向等，具体用法参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fanimation" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation" ref="nofollow noopener noreferrer">animation</a></p></div>  
</div>
            