
---
title: 'JavaScript实现鼠标点击拖拽'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/739f3b8c9c2b4cc0ba021b2c9e326ff4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 18:30:43 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/739f3b8c9c2b4cc0ba021b2c9e326ff4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>三个即将要用的事件</strong></p>
<ul>
<li>onmousedown 鼠标按下事件</li>
<li>onmouseup 鼠标抬起事件</li>
<li>onmousemove 鼠标拖动事件</li>
</ul>
<p><strong>三组浏览器常用属性</strong></p>
<ul>
<li>clientX 与 clientY （**当前元素点击时 **距离浏览器最边上的距离（left 与 top））</li>
<li>offsetLeft 与 offsetTop （<strong>当前元素</strong> 距离浏览器最边上的距离（left 与 top））</li>
<li>innerWidth 与 innerHeight （浏览器整体 <strong>宽</strong> 和 <strong>高</strong>）</li>
</ul>
<p>定义一个我们即将要拖动的 div。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">background</span>: pink; 程序员爱爱 <span class="hljs-attribute">color</span> you too?
  <span class="hljs-attribute">position</span>: absolute;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"left: 100px; top: 100px; width: 100px; height: 100px;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明一下，需要在拖动时改变 div 的 left 和 top，所以设置定位给 div。</p>
<ul>
<li>为什么要给 div 设置行内样式呢？</li>
<li>：便于更好的 **获取 **和 <strong>修改</strong></li>
</ul>
<h1 data-id="heading-0">JavaScript部分 详细讲解原理</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取到 DOM 元素</span>
<span class="hljs-keyword">const</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.box'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">第一步：注册 onmousedown （鼠标按下事件）事件</h4>
<p>当我们点击元素时需要获取到鼠标点击元素的位置。</p>
<pre><code class="hljs language-js copyable" lang="js">box.addEventlistener(<span class="hljs-string">'mousedown'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
   <span class="hljs-comment">// 元素距离最左边的位置，理解为：你的 left 值是多少</span>
    <span class="hljs-keyword">let</span> offsetLeft = box.offsetLeft
    <span class="hljs-keyword">let</span> offsetTop = box.offsetTop
    
   <span class="hljs-comment">// 元素距离最左边的位置（注意：这个位置是鼠标点下去距离浏览器左边的位置，是包含 div 元素的）</span>
    <span class="hljs-keyword">let</span> x = event.clientX - offsetLeft
    <span class="hljs-keyword">let</span> y = event.clientY - offsetTop
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在根据 <strong>clientX</strong> 与 <strong>clientY</strong>，获取到<strong>鼠标在 div 元素中的位置</strong>。</p>
<p>现在我们点击一下 div 元素，看到 div 中的红点位置，是我们鼠标点击的位置，看到控制台中的输入。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/739f3b8c9c2b4cc0ba021b2c9e326ff4~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们每次点击都是在随机的一个位置，所以需要获取到每次鼠标点击在 div 元素上的位置。</p>
<h4 data-id="heading-2">第二步：监听 onmousemove 事件</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.onmousemove = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
    <span class="hljs-keyword">let</span> left = event.clientX - x
    <span class="hljs-keyword">let</span> top = event.clientY - y
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当鼠标点击在 div元素 上并且不松开的情况下，拖动着元素。</p>
<p>开始计算 div元素 的横纵值（left 和 top）</p>
<h4 data-id="heading-3">第三步：元素是否超出浏览器边界</h4>
<p>东：<strong>右边</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>((box.offsetLeft + box.style.width) > <span class="hljs-built_in">window</span>.innerWidth)&#123;
   box.style.left = <span class="hljs-built_in">window</span>.innerWidth - <span class="hljs-built_in">parseInt</span>(box.style.width) + <span class="hljs-string">"px"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>南：<strong>下边</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>((box.offsetTop + box.style.height) > <span class="hljs-built_in">window</span>.innerHeight)&#123;
    box.style.top = <span class="hljs-built_in">window</span>.innerHeight - <span class="hljs-built_in">parseInt</span>(box.style.height) + <span class="hljs-string">'px'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>西：<strong>左边</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (box.offsetLeft < <span class="hljs-number">0</span>) &#123;    box.style.left = <span class="hljs-number">0</span> + <span class="hljs-string">"px"</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>北：<strong>上边</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (box.offsetTop < <span class="hljs-number">0</span>) &#123;
    box.style.top = <span class="hljs-number">0</span> + <span class="hljs-string">"px"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">完整代码</h2>
<p>HTML</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>AUTHOR:CUMIN<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span> &#123;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
    &#125;

    <span class="hljs-selector-class">.box</span> &#123;
      <span class="hljs-attribute">background</span>: pink; programmer most love love pink
      <span class="hljs-attribute">position</span>: absolute;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"left: 100px; top: 100px; width: 100px; height: 100px;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JavaScript</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.box'</span>)

    <span class="hljs-keyword">const</span> mousedown = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'鼠标点击位置 ———— 距离浏览器最左边的位置：'</span>+event.clientX)
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'元素距离浏览器最左边的位置：'</span> + box.offsetLeft)
      <span class="hljs-keyword">let</span> innerX = event.clientX - box.offsetLeft
      <span class="hljs-keyword">let</span> innerY = event.clientY - box.offsetTop

      box.style.borderWidth = <span class="hljs-string">"1px"</span>;
      box.style.borderStyle = <span class="hljs-string">"solid"</span>;
      box.style.borderColor = <span class="hljs-string">"black"</span>;
      <span class="hljs-comment">// 移动时</span>
      <span class="hljs-built_in">document</span>.onmousemove = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
        box.style.left = event.clientX - innerX + <span class="hljs-string">"px"</span>
        box.style.top = event.clientY - innerY + <span class="hljs-string">"px"</span>
      &#125;

      <span class="hljs-comment">// 抬起时</span>
      <span class="hljs-built_in">document</span>.onmouseup = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">document</span>.onmousemove = <span class="hljs-literal">null</span>
        <span class="hljs-built_in">document</span>.mousedown = <span class="hljs-literal">null</span>
        control()
        box.style.borderWidth = <span class="hljs-string">""</span>;
        box.style.borderStyle = <span class="hljs-string">""</span>;
        box.style.borderColor = <span class="hljs-string">""</span>;
      &#125;
    &#125;

    <span class="hljs-comment">// 超出边界处理</span>
    <span class="hljs-keyword">const</span> control = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (box.offsetLeft < <span class="hljs-number">0</span>) &#123;
        box.style.left = <span class="hljs-number">0</span> + <span class="hljs-string">"px"</span>
      &#125;

      <span class="hljs-keyword">if</span> (box.offsetTop < <span class="hljs-number">0</span>) &#123;
        box.style.top = <span class="hljs-number">0</span> + <span class="hljs-string">"px"</span>
      &#125;

      <span class="hljs-keyword">if</span> ((box.offsetLeft + <span class="hljs-built_in">parseInt</span>(box.style.width)) > <span class="hljs-built_in">window</span>.innerWidth) &#123;
        box.style.left = (<span class="hljs-built_in">window</span>.innerWidth - <span class="hljs-built_in">parseInt</span>(box.style.width)) + <span class="hljs-string">"px"</span>
      &#125;

      <span class="hljs-keyword">if</span> ((box.offsetTop + <span class="hljs-built_in">parseInt</span>(box.style.height)) > <span class="hljs-built_in">window</span>.innerHeight) &#123;
        box.style.top = (<span class="hljs-built_in">window</span>.innerHeight - <span class="hljs-built_in">parseInt</span>(box.style.height)) + <span class="hljs-string">"px"</span>
      &#125;

    &#125;

    <span class="hljs-comment">// 按下时</span>
    box.addEventListener(<span class="hljs-string">'mousedown'</span>, mousedown, <span class="hljs-literal">false</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>结印</strong></p></div>  
</div>
            