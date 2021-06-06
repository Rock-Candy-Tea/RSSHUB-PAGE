
---
title: 'css：如何实现左右定宽，中间自适应布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73db0144f16748f088d4def302d4d0b1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 02:13:01 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73db0144f16748f088d4def302d4d0b1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">前述</h3>
<p>今天看到一个css题目，说<strong>你能用几种方式来实现css左右定宽，中间自适应布局</strong>？恰好好久没写布局了，今天通过几种布局方式巩固一下，加深印象。</p>
<p>我下面分别使用<strong>圣杯布局</strong>、<strong>双飞翼布局</strong>、<strong>Flex布局</strong>和<strong>绝对定位布局</strong>实现</p>
<h3 data-id="heading-1">圣杯布局</h3>
<p>圣杯布局是一种<strong>三列</strong>，<strong>左右栏固定</strong>，<strong>中间栏边框自适应</strong>的网页布局</p>
<p>特点：<br>
采用float浮动<br>
三列布局，中间宽度自适应，两边定宽；<br>
中间元素要在html结构中处于开头；</p>
<p>html代码如下:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-comment"><!-- mian要放开头 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>main<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>left<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>right<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.container</span> &#123;
      <span class="hljs-attribute">min-width</span>: <span class="hljs-number">600px</span>;
      <span class="hljs-attribute">overflow</span>: hidden;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">box-sizing</span>: border-box;
    &#125;

    <span class="hljs-selector-class">.left</span>,
    <span class="hljs-selector-class">.main</span>,
    <span class="hljs-selector-class">.right</span> &#123;
      <span class="hljs-attribute">float</span>: left;
      <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100px</span>;
    &#125;

    <span class="hljs-selector-class">.left</span> &#123;
      <span class="hljs-attribute">position</span>: relative;
      <span class="hljs-attribute">left</span>: -<span class="hljs-number">200px</span>;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100%</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: green;
    &#125;

    <span class="hljs-selector-class">.main</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">background</span>: blue;
    &#125;

    <span class="hljs-selector-class">.right</span> &#123;
      <span class="hljs-attribute">position</span>: relative;
      <span class="hljs-attribute">right</span>: -<span class="hljs-number">200px</span>;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">200px</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: red;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73db0144f16748f088d4def302d4d0b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解析：</p>
<ul>
<li>这里的<code>.main</code>使用了<code>width:100%</code>，会导致<code>.left</code>和<code>.right</code>会换行，所以<code>.left</code>的<code>margin-left:100%</code>（<strong>margin-left百分比相对的是父元素</strong>），<code>.right</code>的<code>margin-left: -200px</code>（<strong>200px刚好是自身的宽度</strong>）实现在同一行</li>
<li><code>.container</code>的<code>padding</code>刚好与<code>.left</code>和<code>.right</code>的长度一样，方便<code>.left</code>向左方向，<code>.right</code>向右方向，相对定位移动自身宽度的长度,避免遮挡到<code>.main</code></li>
<li>然后<code>.container</code>需要设置<code>min-width</code>，因为<code>.left</code>的<code>margin-left</code>是<code>100%</code>，相对的是<strong>父元素</strong>，如果<code>.container</code>宽度变小，则<code>.main</code>宽度也会变小，如果小于<code>.left</code>的宽度，则不足以和<code>.main</code>在一行，<code>.left</code>则会换行</li>
</ul>
<blockquote>
<p>这里是讲自己的理解，话糙了一点，如果看不懂，自己可以复制代码，自己去看看，会了解的更深。</p>
</blockquote>
<h3 data-id="heading-2">双飞翼布局</h3>
<p>双飞翼布局也是一种<strong>三列</strong>，<strong>左右栏固定</strong>，<strong>中间栏边框自适应</strong>的网页布局<br>
解决问题也和圣杯布局类似，也是采用<strong>三栏全部float浮动</strong>，<strong>左右两栏加上负margin</strong>，<strong>跟中间栏div并排</strong>，形成三栏布局。<strong>主要不同是在解决 “中间栏div内容不被遮挡”方式不一样</strong>。</p>
<p>html代码如下（注意⚠：HTML结构发生改变, 多了<strong>div.content</strong>）</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>main<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>left<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>right<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.main</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">background</span>: blue;
    &#125;

    <span class="hljs-selector-class">.content</span> &#123;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">200px</span>;
    &#125;

    <span class="hljs-selector-class">.left</span>,
    <span class="hljs-selector-class">.main</span>,
    <span class="hljs-selector-class">.right</span> &#123;
      <span class="hljs-attribute">float</span>: left;
      <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100px</span>;
    &#125;

    <span class="hljs-selector-class">.left</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100%</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: green;
    &#125;

    <span class="hljs-selector-class">.right</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">200px</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: red;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和圣杯布局主要区别：</p>
<ul>
<li><code>.main</code>内部多了子元素<code>div.content</code></li>
<li>子元素<code>div.content</code>里用<code>margin-left</code>和<code>margin-right</code>，去保证不被<code>.left</code>和<code>.right</code>遮挡</li>
<li><code>.left</code>,<code>.right</code>不需要使用定位去避免遮挡<code>.main</code></li>
</ul>
<h3 data-id="heading-3">Flex布局</h3>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-comment"><!-- 注意是left main right --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>left<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>main<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>right<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.container</span> &#123;
      <span class="hljs-attribute">display</span>: flex;
      <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100px</span>;
    &#125;

    <span class="hljs-selector-class">.left</span> &#123;
      <span class="hljs-attribute">flex-basis</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: green;
    &#125;

    <span class="hljs-selector-class">.main</span> &#123;
      <span class="hljs-attribute">flex</span>: auto;
      <span class="hljs-attribute">background</span>: blue;
    &#125;

    <span class="hljs-selector-class">.right</span> &#123;
      <span class="hljs-attribute">flex-basis</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: red;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析：</p>
<ul>
<li><strong>flex布局</strong>，弹性布局，可以简便、完整、响应式地实现各种页面布局，未来的布局的首选方案（当然如果你要考虑ie,另说）</li>
<li><code>.main</code>使用<code>flex</code>属性，<code>.left</code> 和<code>.right</code>使用<code>flex-basis</code> 属性</li>
<li><code>flex</code>属性是<code>flex-grow</code>（如果有剩余空间，是否扩大）, <code>flex-shrink</code>（如果空间不够，是否压缩） 和 <code>flex-basis</code>（本身的空间大小）的简写，默认值为<code>0 1 auto</code>。后两个属性可选</li>
<li><code>flex属性</code>有两个快捷值：<code>auto (1 1 auto)</code> 和 <code>none (0 0 auto)</code>,这里使用的是<code>auto</code>，如果有剩余空间，则扩大，如果空间不够,则压缩</li>
</ul>
<h3 data-id="heading-4">absolute 布局</h3>
<p><code>absolute</code>绝对定位的元素的位置与文档流无关，因此不占据空间。<br>
这一点与相对定位不同，相对定位实际上被看作普通流定位模型的一部分。</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
  <span class="hljs-comment"><!-- 注意是left main right --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>left<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>main<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>right<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.container</span> &#123;
      <span class="hljs-attribute">position</span>: relative;
    &#125;

    <span class="hljs-selector-class">.left</span>,
    <span class="hljs-selector-class">.main</span>,
    <span class="hljs-selector-class">.right</span> &#123;
      <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100px</span>;
    &#125;

    <span class="hljs-selector-class">.left</span> &#123;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: green;
    &#125;

    <span class="hljs-selector-class">.main</span> &#123;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">200px</span> <span class="hljs-number">0</span> <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: blue;
    &#125;

    <span class="hljs-selector-class">.right</span> &#123;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background</span>: red;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析：</p>
<ul>
<li><code>.main</code>使用<code>margin</code>避免被<code>.left</code>和<code>.right</code>遮挡</li>
<li><code>.left</code>和<code>.right</code>使用<code>absolute</code>定位，不占据文档流</li>
</ul>
<h3 data-id="heading-5">总结：</h3>
<p>推荐使用：<strong>flex布局 > absolute布局 = 双飞翼布局 > 圣杯布局</strong><br>
首选flex布局，因为这是未来的布局方式的首选方案，属性方便设置，实用，好理解；<br>
absolute布局和双飞翼布局适中，圣杯布局不好理解（对我来说）；<br>
大家都可以了解下，正所谓技多不压身嘛。</p></div>  
</div>
            