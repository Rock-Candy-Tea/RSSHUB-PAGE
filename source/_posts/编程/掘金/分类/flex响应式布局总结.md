
---
title: 'flex响应式布局总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78ea2ac67bdb4278b35890c04ad1b94f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 07:43:40 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78ea2ac67bdb4278b35890c04ad1b94f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>众所周知，弹性布局在前端的开发中有着举足轻重的地位，只要使用得当，可以用其制作出许多复杂的布局，但本人最主要的都是使用在响应式布局方面。</p>
<h2 data-id="heading-0">内容结构</h2>
<ul>
<li>容器属性
<ul>
<li>主轴布局
<ul>
<li>flex-direction</li>
<li>flex-wrap</li>
<li>flex-flow</li>
<li>justify-content</li>
</ul>
</li>
<li>侧轴布局
<ul>
<li>align-items</li>
</ul>
</li>
<li>多轴布局
<ul>
<li>align-content</li>
</ul>
</li>
</ul>
</li>
<li>内容属性
<ul>
<li>order</li>
<li>flex-grow</li>
<li>flex-shrink</li>
<li>flex-basis</li>
<li>flex</li>
<li>align-self</li>
</ul>
</li>
</ul>
<blockquote>
<p>使用flex布局: <strong>display:flex;</strong></p>
</blockquote>
<h2 data-id="heading-1">demo</h2>
<p><code>hmtl</code></p>
<pre><code class="copyable"><div class="warpper">
    <div class="inner">1</div>
    <div class="inner">2</div>
    <div class="inner">3</div>
    <div class="inner">4</div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>css</code></p>
<pre><code class="copyable">.warpper &#123;
    width: 500px;
    height: 500px;
&#125;
.inner &#123;
    font-weight: bold;
    color: white;
    text-align: center;
    line-height: 100px;
    font-size: 40px;
&#125;
.inner:nth-child(even)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
&#125;
.inner:nth-child(odd)&#123;
    width: 100px;
    height: 100px;
    background-color: #000000;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>效果</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78ea2ac67bdb4278b35890c04ad1b94f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">容器属性</h2>
<p><code>css</code></p>
<pre><code class="copyable">.warpper &#123;
    width: 500px;
    height: 500px;
    display: flex;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>效果</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9f6beb51cb14680989cf8d30b42aa91~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">主轴布局</h2>
<h3 data-id="heading-4">主轴侧轴概念</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01ab1fa47f7d48dab03006c93df024e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5"><code>flex-direction</code></h3>
<blockquote>
<p>使用容器样式flex布局下添加： flex-direction: <code>param</code>;</p>
</blockquote>
<pre><code class="copyable">@param: 
       row: 主轴方向向右
       row-reverse: 主轴方向向左
       column: 主轴方向向下
       column-reverse: 主轴方向向上
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><code>flex-wrap</code></h3>
<blockquote>
<p>使用容器样式flex布局下添加： flex-wrap: <code>param</code>;</p>
</blockquote>
<pre><code class="copyable">@param: 
       nowrap: 不换行
       wrap: 换行
       wrap-reverse: 反方向换行
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><code>flex-flow</code></h3>
<blockquote>
<p>使用容器样式flex布局下添加： flex-flow: <code><flex-direction> || <flex-wrap></code>;</p>
</blockquote>
<h3 data-id="heading-8"><code>justify-content</code></h3>
<blockquote>
<p>使用容器样式flex布局下添加： justify-content: <code>param</code>;</p>
</blockquote>
<pre><code class="copyable">@param: 
       flex-start: 主轴起点开始
       flex-end: 主轴终点开始
       center: 居中
       space-between: 两端对齐
       space-around: 平均分布在两边
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">侧轴布局</h2>
<h3 data-id="heading-10"><code>align-items</code></h3>
<blockquote>
<p>使用容器样式flex布局下添加： align-items: <code>param</code>;</p>
</blockquote>
<pre><code class="copyable">@param: 
       flex-start: 侧轴起点开始
       flex-end: 侧轴终点开始
       center: 居中
       baseline: 盒子文字基线对齐
       stretch: 没有高度情况下！默认拉伸充满父元素高度
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">多轴布局</h2>
<h3 data-id="heading-12"><code>align-content</code></h3>
<blockquote>
<p>使用容器样式flex布局下添加： align-content: <code>param</code>;</p>
</blockquote>
<pre><code class="copyable">@param: 
       flex-start: 侧轴起点开始
       flex-end: 侧轴终点开始
       center: 侧轴居中
       space-between: 侧轴两端对齐
       space-around: 在侧轴上平均分布在两边
       stretch: 没有高度情况下！默认拉伸充满父元素空间
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>无高度stretch 效果</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fb1207e5c534c3c8ded52539f847fb7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">内容属性</h2>
<h3 data-id="heading-14">order</h3>
<blockquote>
<p>后面跟着一个整数，数值越大，该元素越往后</p>
</blockquote>
<p><code>css</code></p>
<pre><code class="copyable">.inner:nth-child(1)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    order: 8;
&#125;
.inner:nth-child(2)&#123;
    width: 100px;
    height: 100px;
    background-color: #000000;
    order: -8;
&#125;
.inner:nth-child(3)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    order: 2;
&#125;
.inner:nth-child(4)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    order: 1; // (默认)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>效果</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6084cfaf417f410a85f2296381957d7e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">flex-grow</h3>
<blockquote>
<p>通过该属性后面跟一个整数，根据兄弟属性之间该整数的占比，父元素剩余空间会被平均分配。</p>
</blockquote>
<p><code>css</code></p>
<pre><code class="copyable">.inner:nth-child(1)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    flex-grow: 0;
&#125;
.inner:nth-child(2)&#123;
    width: 100px;
    height: 100px;
    background-color: #000000;
    flex-grow: 1;
&#125;
.inner:nth-child(3)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    flex-grow: 0;
&#125;
.inner:nth-child(4)&#123;
    width: 100px;
    height: 100px;
    background-color: black;
    flex-grow: 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>效果</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4536cdc6c53b4e0b859797b4f9da2e91~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">flex-shrink</h3>
<blockquote>
<ul>
<li>与<code>flex-grow</code>相反，当父元素空间不够的时候他会进行缩小，而<code>flex-shrink</code>就是控制缩小的的属性</li>
<li>他后面也是跟一个整数，不过他的算法比较麻烦，我们只要知道后面跟的数值越大，则缩小的越多</li>
<li>flex-shrink：0; 表示不收缩</li>
</ul>
</blockquote>
<h3 data-id="heading-17">flex-basis</h3>
<blockquote>
<p>初始所占空间的大小
auto则为自定义宽度</p>
</blockquote>
<p><code>css</code></p>
<pre><code class="copyable">.inner:nth-child(1)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    flex-basis: 200px;
&#125;
.inner:nth-child(2)&#123;
    width: 100px;
    height: 100px;
    background-color: #000000;
    flex-basis: 50px;
&#125;
.inner:nth-child(3)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    flex-basis: 50px;
&#125;
.inner:nth-child(4)&#123;
    width: 100px;
    height: 100px;
    background-color: black;
    flex-basis: 150px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>效果</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0d364a791ec4c40b1c24bc42e9218cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">flex</h3>
<blockquote>
<ul>
<li>flex: <code><flex-grow></code> || <code><flex-shrink></code> || <code><flex-basis></code></li>
<li>auto: flex: 1 1 auto;</li>
<li>none: flex: 0 0 auto;</li>
</ul>
</blockquote>
<h3 data-id="heading-19">align-self</h3>
<blockquote>
<ul>
<li>单个内容盒子在侧轴上不同的对齐方式</li>
<li>内容css: align-self: <code>param</code>;</li>
</ul>
</blockquote>
<pre><code class="copyable">@param:
       auto: 继承align-items
       flex-start: 侧轴起点开始
       flex-end: 侧轴终点开始
       center: 居中
       baseline: 盒子文字基线对齐
       stretch: 没有高度情况下！默认拉伸充满父元素高度
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>css</code></p>
<pre><code class="copyable">.inner:nth-child(1)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    align-self: center;
&#125;
.inner:nth-child(2)&#123;
    width: 100px;
    height: 100px;
    background-color: #000000;
    align-self: flex-end;
&#125;
.inner:nth-child(3)&#123;
    width: 100px;
    height: 100px;
    background-color: red;
    align-self: flex-start;
&#125;
.inner:nth-child(4)&#123;
    width: 100px;
    /* height: 100px; */
    background-color: black;
    align-self: stretch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>效果</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad6bb4e5a4f047e3b73ba44c123cabda~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            