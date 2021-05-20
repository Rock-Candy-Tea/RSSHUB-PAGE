
---
title: '「just-fe」前端基础指南：03-CSS基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4813'
author: 掘金
comments: false
date: Tue, 18 May 2021 21:42:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=4813'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「just-fe」前端基础指南，收集整理了前端开发需要掌握的基础知识，方便夯实基础，查漏补缺。</p>
</blockquote>
<h1 data-id="heading-0">03-css基础</h1>
<h2 data-id="heading-1">1.盒子模型</h2>
<blockquote>
<p>margin, border, padding, content</p>
</blockquote>
<ul>
<li>标准盒子：width = content-width；box-sizing: content-box</li>
<li>怪异盒子：width = border-width + padding + content-width；box-sizing: border-box</li>
</ul>
<h2 data-id="heading-2">2.flex</h2>
<p>指定 flex 容器：</p>
<blockquote>
<p>display: flex | inline-flex</p>
</blockquote>
<ul>
<li>flex-direction: row | column | row-reverse | column-reverse(顺序反转)</li>
<li>flex-wrap: nowrap | wrap | wrap-reverse(行翻转);</li>
<li>justify-content: flex-start | flex-end | center | space-between | space-around;主轴上的对齐方式</li>
<li>align-items: flex-start | flex-end | center | baseline(基线，以文字底部为主) | stretch(默认，以flex-direction:row 为例，如果未设置高度或者 auto，撑满整个容器高度);交叉轴的对齐方式</li>
<li>align-content: flex-start | flex-end | center | space-between | space-around | stretch;(定义了多根轴线的对齐方式，如果项目只有一根轴线，那么该属性将不起作用，如果 flex-wrap: wrap，则起作用)</li>
</ul>
<p>flex 子项：</p>
<ul>
<li>order: ; 排序</li>
<li>flex-basis:  | auto;(定义了在分配多余空间之前，项目占据的主轴空间，浏览器根据这个属性，计算主轴是否有多余空间)</li>
<li>flex-grow: ; (默认为 0，定义项目的放大比例)</li>
<li>flex-shrink: ; (定义了项目的缩小比例)</li>
<li>flex: ; (flex-grow, flex-shrink 和 flex-basis的简写)</li>
<li>align-self: auto | flex-start | flex-end | center | baseline | stretch;(允许单个项目有与其他项目不一样的对齐方式)</li>
</ul>
<p>flex: 0 1 auto; 放大 0，缩小 1, 自动占用主轴空间。</p>
<h2 data-id="heading-3">3.css 优先级</h2>
<blockquote>
<p>important > 内联 > id选择器 > 类选择器 > 标签选择器</p>
</blockquote>
<h3 data-id="heading-4">3.1 浏览器怎样解析 css 选择器的？</h3>
<blockquote>
<p>从右向左解析。</p>
</blockquote>
<h2 data-id="heading-5">4.避免 css 全局污染</h2>
<ul>
<li>使用 css module (生成唯一的类名)</li>
</ul>
<h2 data-id="heading-6">5.动态设置样式</h2>
<ul>
<li>前缀 or react-context</li>
</ul>
<h2 data-id="heading-7">6.CSS3 有哪些新特性？</h2>
<ul>
<li>RGBA 和透明度</li>
<li>background-image、background-size、background-repeat</li>
<li>文字阴影 text-shadow</li>
<li>圆角 border-radius</li>
<li>边框图片 border-image</li>
<li>盒子阴影 box-shadow</li>
</ul>
<h2 data-id="heading-8">7.display:none 和 visibility:hidden 区别？</h2>
<ul>
<li>display:none 不显示元素，不占空间，会导致重绘和回流</li>
<li>visibility: hidden 隐藏元素，占空间</li>
</ul>
<h2 data-id="heading-9">8.对 BFC 的理解</h2>
<blockquote>
<p>BFC是指一个独立的渲染区域，只有Block-level Box参与。它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干.。</p>
</blockquote>
<p>定义：浮动元素和绝对定位元素，非块级盒子的块级容器（例如 inline-blocks, table-cells, 和 table-captions），以及overflow值不为"visiable"的块级盒子，都会为他们的内容创建新的BFC（Block Fromatting Context， 即块级格式上下文）。</p>
<p>BFC的触发条件：</p>
<ul>
<li>根元素，即 html 元素</li>
<li>浮动元素（float 不为 none）、绝对定位元素（position: fixed/absolute）</li>
<li>行内块元素(display: inline-block)、表格单元格(display: table-cell)、表格标题(display: table-caption)</li>
<li>overflow不为visible的块元素</li>
<li>网格元素(display: grid)</li>
</ul>
<p>应用场景：</p>
<ul>
<li>防止浮动导致父元素高度塌陷；</li>
<li>避免外边距折叠；（margin 重叠的原因就是这个）</li>
<li>两栏布局，防止文字环绕等</li>
</ul>
<h2 data-id="heading-10">9.line-height 的理解？</h2>
<blockquote>
<p>行高是指一行文字的高度，具体说是两行文字间基线的距离。
多行文本垂直居中：需要设置display属性为inline-block。</p>
</blockquote>
<h2 data-id="heading-11">10.怎么让 chrome 支持小于 12px 的文字？</h2>
<ul>
<li>transform: scale(0.8);</li>
</ul>
<h2 data-id="heading-12">11.浏览器刷新频率？</h2>
<ul>
<li>60hz，一秒刷新60次，最小间隔为 16.7ms = 1000 / 60</li>
</ul>
<h2 data-id="heading-13">12.position</h2>
<ul>
<li>absolute</li>
<li>relative</li>
<li>fixed</li>
<li>static</li>
<li>sticky</li>
<li>initial</li>
<li>unset</li>
</ul>
<h2 data-id="heading-14">13.居中</h2>
<ul>
<li>margin: 0 auto;</li>
<li>display: flex; justify-content: center;</li>
<li>display: table; margin: 0 auto;</li>
</ul>
<h2 data-id="heading-15">14.高清问题 1px</h2>
<blockquote>
<p>产生原因：DPR(devicePixelRatio) 设备像素比，window.devicePixelRatio=物理像素 /CSS像素</p>
</blockquote>
<p>目前主流的屏幕DPR=2 （iPhone 8）,或者3 （iPhone 8 Plus）。拿2倍屏来说，设备的物理像素要实现1像素，而DPR=2，所以css 像素只能是 0.5。一般设计稿是按照750来设计的，它上面的1px是以750来参照的，而我们写css样式是以设备375为参照的，所以我们应该写的0.5px就好了啊！ 试过了就知道，iOS 8+系统支持，安卓系统不支持。</p>
<p>解决方案：</p>
<ul>
<li>border: 0.5px; ios8+ 支持，安卓不支持。</li>
<li>边框图片; 颜色不可控，圆角模糊；</li>
<li>伪元素;</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.setOnePx</span>&#123;
  <span class="hljs-attribute">position</span>: relative;
  &<span class="hljs-selector-pseudo">::after</span>&#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#e5e5e5</span>;
    <span class="hljs-attribute">display</span>: block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">1px</span>; <span class="hljs-comment">/*no*/</span>
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>, <span class="hljs-number">0.5</span>);
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  &#125;
&#125;
<span class="hljs-selector-class">.setBorderAll</span>&#123;
  <span class="hljs-attribute">position</span>: relative;
  &:after&#123;
    content:<span class="hljs-string">" "</span>;
    <span class="hljs-attribute">position</span>:absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">200%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.5</span>);
    <span class="hljs-attribute">transform-origin</span>: left top;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#E5E5E5</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>设置 viewport 的 scale 值。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>1px question<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Content-Type"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"text/html;charset=UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"WebViewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no"</span>></span>        
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-tag">html</span> &#123;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1px</span>;
      &#125;
      * &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-selector-class">.top_b</span> &#123;
        <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#E5E5E5</span>;
      &#125;

      <span class="hljs-selector-class">.a</span>,<span class="hljs-selector-class">.b</span> &#123;
        <span class="hljs-attribute">box-sizing</span>: border-box;
        <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">1rem</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">1rem</span>;                
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1.4rem</span>;
      &#125;

      <span class="hljs-selector-class">.a</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      &#125;

      <span class="hljs-selector-class">.b</span> &#123;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#f5f5f5</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">var</span> viewport = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"meta[name=viewport]"</span>);
      <span class="hljs-comment">//下面是根据设备像素设置viewport</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.devicePixelRatio == <span class="hljs-number">1</span>) &#123;
        viewport.setAttribute(<span class="hljs-string">'content'</span>, <span class="hljs-string">'width=device-width,initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no'</span>);
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.devicePixelRatio == <span class="hljs-number">2</span>) &#123;
        viewport.setAttribute(<span class="hljs-string">'content'</span>, <span class="hljs-string">'width=device-width,initial-scale=0.5, maximum-scale=0.5, minimum-scale=0.5, user-scalable=no'</span>);
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.devicePixelRatio == <span class="hljs-number">3</span>) &#123;
        viewport.setAttribute(<span class="hljs-string">'content'</span>, <span class="hljs-string">'width=device-width,initial-scale=0.3333333333333333, maximum-scale=0.3333333333333333, minimum-scale=0.3333333333333333, user-scalable=no'</span>);
      &#125;
      <span class="hljs-keyword">var</span> docEl = <span class="hljs-built_in">document</span>.documentElement;
      <span class="hljs-keyword">var</span> fontsize = <span class="hljs-number">32</span>* (docEl.clientWidth / <span class="hljs-number">750</span>) + <span class="hljs-string">'px'</span>;
      docEl.style.fontSize = fontsize;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"top_b a"</span>></span>下面的底边宽度是虚拟1像素的<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"b"</span>></span>上面的边框宽度是虚拟1像素的<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">15.重绘与回流（重排）</h2>
<blockquote>
<p>回流必将引起重绘，重绘不一定会引起回流。</p>
</blockquote>
<p>当 Render树 中部分或全部元素的尺寸、结构、或某些属性发生改变时，浏览器重新渲染部分或全部文档的过程称为回流。</p>
<ul>
<li>改变窗口大小</li>
<li>改变字体</li>
<li>添加、修改样式</li>
<li>内容变化</li>
<li>伪类</li>
<li>设置style 等</li>
</ul>
<p>当页面中元素样式的改变并不影响它在文档流中的位置时（例如：color、background-color、visibility等），浏览器会将新样式赋予给元素并重新绘制它，这个过程称为重绘。</p>
<h2 data-id="heading-17">16.水平垂直布局</h2>
<ul>
<li>lineheight</li>
<li>flex</li>
<li>grid (和 flex 一样，但是兼容性不好)</li>
</ul>
<h2 data-id="heading-18">17.层叠上下文</h2>
<blockquote>
<p>层叠上下文是HTML元素的三维概念，这些HTML元素在一条假想的相对于面向（电脑屏幕的）视窗或者网页的用户的z轴上延伸，HTML元素依据其自身属性按照优先级顺序占用层叠上下文的空间。</p>
</blockquote>
<p>触发：</p>
<ul>
<li>根元素 (HTML)</li>
<li>opacity 属性值小于 1 的元素</li>
<li>transform 属性值不为 "none"的元素</li>
<li>z-index 值不为 "auto"的 绝对/相对定位，</li>
<li>position: fixed</li>
</ul>
<h2 data-id="heading-19">18.transform</h2>
<ul>
<li>transform 不会触发重绘和回流，元素仍然占据原来的位置</li>
<li>transform 会创建一个 GPU图层，使用 GPU渲染。</li>
</ul>
<p>微信公众号：「皮蛋菌丶」</p>
<p>github：<a href="https://github.com/UncleYee/just-fe" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p>
<p>欢迎来撩~</p></div>  
</div>
            