
---
title: 'javascript 基础- 获取屏幕高度'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2089'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 04:01:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=2089'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">是什么</h2>
<p>在日常开发中，我们会写 回到顶部、滚动条加载数据 等常用功能，这时候，我们不得不提到用 js 获取页面高度的问题。</p>
<p>如获取当前元素到页面底部的距离， 如获取文档网页底部到可视区窗口距离等，我们需要了解以下 API</p>
<h2 data-id="heading-1">讲什么</h2>
<ol>
<li>文档高度与宽度</li>
<li>可视区域高度与宽度</li>
<li>当前元素高度与宽度</li>
<li>带滚动条：获取纵向滚动条高度</li>
<li>带滚动条：获取横向滚动条长度</li>
<li>获取元素到视口的距离</li>
<li>event 对象中的值</li>
<li>常用公式</li>
<li>实用案例</li>
<li>总结</li>
</ol>
<h2 data-id="heading-2">文档高度与宽度</h2>
<p>即是 document 的高度/宽度, 它通常和滚动条相互关联判断操作</p>
<ol>
<li>document.documentElement 获取文档元素。($(document).height())</li>
<li>当没有滚动条时 scrollHeight 和 clientHeight 相同，事实上各种浏览器有不同的处理，通常兼容性写法是取这俩中最大者。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getPageInfo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-built_in">Math</span>.max(
      <span class="hljs-built_in">document</span>.documentElement.scrollWidth,
      <span class="hljs-built_in">document</span>.documentElement.clientWidth
    ),
    <span class="hljs-attr">height</span>: <span class="hljs-built_in">Math</span>.max(
      <span class="hljs-built_in">document</span>.documentElement.scrollHeight,
      <span class="hljs-built_in">document</span>.documentElement.clientHeight
    ),
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">可视区域高度与宽度</h2>
<p>即是 当前可视区域的高度 和 宽度, 它通常和滚动条相互关联判断操作</p>
<ol>
<li>document.documentElement 获取文档元素。($(window).height())</li>
<li>可视区域高度与宽度 是 文档高度与宽度的子集</li>
<li>jq 写法 <code>$(window).height(); $(window).width();</code></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getViewport</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-built_in">document</span>.documentElement.clientWidth,
    <span class="hljs-attr">height</span>: <span class="hljs-built_in">document</span>.documentElement.clientHeight,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">当前元素高度与宽度</h2>
<p>即是当前元素的真实高度，与滚动条操作无关</p>
<ol>
<li>$(ele).height() 获取元素的真实高度</li>
<li>$(ele).width() 获取元素的真实宽度</li>
<li>当出现滚动条的时候， 我们可以使用 $(ele).offset().top 来获取当前元素距顶部的距离</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getEleTop</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-keyword">let</span> offsetTop = el.offsetTop;
  <span class="hljs-keyword">let</span> current = el.offsetParent;
  <span class="hljs-keyword">while</span> (current !== <span class="hljs-literal">null</span>) &#123;
    offsetTop += current.offsetTop;
    current = current.offsetParent;
  &#125;
  <span class="hljs-keyword">return</span> offsetTop;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">带滚动条：获取纵向滚动条高度</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getScrollTop</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> doc = <span class="hljs-built_in">document</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.max(doc.body.scrollTop, doc.documentElement.scrollTop);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">带滚动条：获取横向滚动条长度</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getScrollLeft</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> doc = <span class="hljs-built_in">document</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.max(doc.body.scrollLeft, doc.documentElement.scrollLeft);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">获取元素到视口的距离</h2>
<p>使用 getBoundingClientRect 方法返回元素的大小及其相对于视口的位置。</p>
<p>如果是标准盒子模型，元素的尺寸等于 width/height + padding + border-width 的总和。如果 box-sizing: border-box，元素的的尺寸等于 width/height。</p>
<ol>
<li>方法返回的一组矩形的集合</li>
<li>left, top, right, bottom, x, y, width, 和 height 这几个以像素为单位的只读属性用于描述整个边框。</li>
<li>width 和 height 以外的属性是相对于视图窗口的左上角来计算的。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> rect = obj.getBoundingClientRect();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">event 对象中的值</h2>
<p>在绑定事件的时候，通常 js 会返回一个 event 对象，这个对象返回了当前元素的相关信息。</p>
<ol>
<li>event.screenY 当前元素的屏幕-滚动距离，它包含可视区域未显示的部分（它最大）</li>
<li>event.pageY 当前元素的 clientY + ScrollY 距离（它第二大）</li>
<li>event.clientY 当前元素的可视区域-滚动距离，它只包含可视区域部分（它第三大）</li>
<li>event.offsetY 当前元素距离父元素的距离（它第四大）</li>
</ol>
<h2 data-id="heading-9">常用公式</h2>
<ol>
<li>文档底部与可视区窗口底部的距离 = 文档总高度(document) - 文档滚动高度(scroll) - 可视区窗口高度(view)</li>
<li>当前元素与底部的距离 = 可视区窗口高度(view) + 文档滚动高度(scroll) - 当前元素与页面顶部距离(offset) - 当前元素高度 (ele.height)</li>
</ol>
<h2 data-id="heading-10">实用案例</h2>
<h3 data-id="heading-11">返回顶部</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">goTop</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> goTop = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".goTop"</span>);
  <span class="hljs-keyword">const</span> rootElement = <span class="hljs-built_in">document</span>.documentElement;
  <span class="hljs-keyword">const</span> scrollTotal = rootElement.scrollHeight - rootElement.clientHeight;
  <span class="hljs-keyword">if</span> (rootElement.scrollTop / scrollTotal > <span class="hljs-number">0.8</span>) &#123;
    goTop.classList.add(<span class="hljs-string">"showBtn"</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    goTop.classList.remove(<span class="hljs-string">"showBtn"</span>);
  &#125;
&#125;

<span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"scroll"</span>, goTop);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">滚动导航</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"scroll"</span>, goTop);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">goTop</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> nav = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"item-nav"</span>);
  <span class="hljs-keyword">var</span> scrollTop = <span class="hljs-built_in">document</span>.body.scrollTop || <span class="hljs-built_in">document</span>.documentElement.scrollTop;
  <span class="hljs-keyword">if</span> (scrollTop > <span class="hljs-number">65</span>) &#123;
    nav.style.top = <span class="hljs-string">"20px"</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    nav.style.top = <span class="hljs-number">80</span> - scrollTop + <span class="hljs-string">"px"</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">上下滚动时判断元素在视口中出现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.onscroll = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> dom = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"box"</span>);
  <span class="hljs-keyword">let</span> top = getElementTop(dom); <span class="hljs-comment">// 元素距页面高度</span>
  <span class="hljs-keyword">let</span> scrollTop = getScrollTop(); <span class="hljs-comment">// 获取滚动条高度</span>
  <span class="hljs-keyword">let</span> viewPortHeight = getViewport().height; <span class="hljs-comment">// 获取视口宽高</span>

  <span class="hljs-keyword">if</span> (top > scrollTop && top <= scrollTop + viewPortHeight) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"元素出现"</span>);
  &#125;
&#125;;

<span class="hljs-built_in">document</span>.onscroll = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> $dom = $(<span class="hljs-string">"#box"</span>);
  <span class="hljs-keyword">let</span> top = $dom.offset().top;
  <span class="hljs-keyword">let</span> scrollTop = $(<span class="hljs-built_in">window</span>).scrollTop();
  <span class="hljs-keyword">let</span> viewPortHeight = $(<span class="hljs-built_in">window</span>).height();

  <span class="hljs-keyword">if</span> (top > scrollTop && top <= scrollTop + viewPort.height) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"元素出现"</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">总结</h2>
<pre><code class="copyable">网页可见区域宽：document.body.clientWidth
网页可见区域高：document.body.clientHeight
网页可见区域宽：document.body.offsetWidth (包括边线的宽)
网页可见区域高：document.body.offsetHeight (包括边线的宽)
网页正文全文宽：document.body.scrollWidth
网页正文全文高：document.body.scrollHeight
网页被卷去的高：document.body.scrollTop
网页被卷去的左：document.body.scrollLeft
网页正文部分上：window.screenTop
网页正文部分左：window.screenLeft
屏幕分辨率的高：window.screen.height
屏幕分辨率的宽：window.screen.width
屏幕可用工作区高度：window.screen.availHeight
屏幕可用工作区宽度：window.screen.availWidth
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            