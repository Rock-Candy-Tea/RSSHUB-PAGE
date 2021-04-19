
---
title: '前端面试题总结一（HTML和CSS）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2c403dca32e42c1a69f8abdff1c6492~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 22:50:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2c403dca32e42c1a69f8abdff1c6492~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.1你是如和理解HTML语义化的？</h2>
<h3 data-id="heading-1">答：我平时写的代码都是HTML语义化的代码。我理解的HTML语义化简单来说就是使用正确的标签做正确的事情，例如段落要写成p标签，标题要写h1~h6。使用恰当语义的 HTML 标签，让页面具有良好的语义和结构，从而方便人类和机器都能快速理解网页内容。</h3>
<h3 data-id="heading-2">发展路线：后端的table标签–>美工人员使用div+css布局–>讲专业的前端会使用正确的标签进行页面开发</h3>
<h2 data-id="heading-3">1.2为什么要使用HTML语义化标签？</h2>
<ul>
<li>用正确的标签做正确的事情</li>
<li>页面内容结构化</li>
<li>无 CSS 时也能进行网页阅读</li>
<li>方便浏览器，搜索引擎解析，利于 SEO</li>
</ul>
<h2 data-id="heading-4">2.meta viewport 是做什么用的，怎么写？（手机上让页面不能缩放，应该怎么写。）</h2>
<p>答：移动端适配，让在PC段端正常显示的页面，到了不同大小的移动端也能根据屏幕的大小正常显示页面。</p>
<pre><code class="copyable"><meta name="viewport" content="width=device-width, user-scalable=no,  initial-scale=1, maximum-scale=1, minimum-scale=1">
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2c403dca32e42c1a69f8abdff1c6492~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">3.H5是什么？</h2>
<h3 data-id="heading-6">答：H5应该是一个前端技术的集合，我们在谈论H5的时候，实际上是一个解决方案。一个看起来酷炫的的移动端网站的解决方案。这个解决方案包括了HTML5新增的audio（音频）标签，canvas,拖曳特性，本地存储，websocket通信，同时也包括盒模型，绝对定位，包括一切前端的基本知识。</h3>
<ul>
<li>websocket通信:最大的特点就是服务端可以主动向客户端推送消息，客户端也可以主动向服务端发送消息.</li>
</ul>
<p><img alt="图片.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c1939813f044d1baf86303b3f8467e9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">4.清除浮动：</h2>
<h3 data-id="heading-8">4.1当父元素不给高度的时候，内部元素不浮动时会撑开，而浮动的时候，父元素变成一条线。</h3>
<h3 data-id="heading-9">4.2解决方法</h3>
<h4 data-id="heading-10">4.2.1.额外标签法（在最后一个浮动标签后，新加一个标签，给其设置clear：both；）</h4>
<pre><code class="copyable">    .clear&#123;
        clear:both;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">4.2.2.父级添加overflow属性（父元素添加overflow:hidden）（不推荐）</h4>
<h4 data-id="heading-12">通过触发BFC方式，实现清除浮动</h4>
<pre><code class="copyable">    .fahter&#123;
        width: 400px;
        border: 1px solid deeppink;
        overflow: hidden;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">优点：代码简洁</h4>
<h4 data-id="heading-14">缺点：内容增多的时候容易造成不会自动换行导致内容被隐藏掉，无法显示要溢出的元素</h4>
<h4 data-id="heading-15">4.2.3.使用after伪元素清除浮动（推荐使用）</h4>
<pre><code class="copyable">    .clearfix:after&#123;/*伪元素是行内元素 正常浏览器清除浮动方法*/
        content: "";
        display: block;
        height: 0;
        clear:both;
        //将元素隐藏，但是在网页中该占的位置还是占着
        visibility: hidden;
    &#125;
    .clearfix&#123;
        *zoom: 1;/*ie6清除浮动的方式 *号只有IE6-IE7执行，其他浏览器不执行*/
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：符合闭合浮动思想，结构语义化正确</p>
<p>缺点：ie6-7不支持伪元素：after，使用zoom:1触发hasLayout.</p>
<p>4.2.4使用before和after双伪元素清除浮动</p>
<pre><code class="copyable">     .clearfix:after,.clearfix:before&#123;
        content: "";
        display: table;
    &#125;
    .clearfix:after&#123;
        clear: both;
    &#125;
    .clearfix&#123;
        *zoom: 1;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：代码更简洁</p>
<p>缺点：用zoom:1触发hasLayout.</p>
<pre><code class="copyable">//背代码
 .clearfix:after&#123;
     content: '';
     display: block; /*或者 table*/
     clear: both;
 &#125;
 .clearfix&#123;
     zoom: 1; /* IE 兼容*/
 &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">5.你用过那些HTML5标签？</h2>
<h3 data-id="heading-17">答：①内容相关：header\main\footer\artticle;</h3>
<h3 data-id="heading-18">②功能相关：canvas\video\audio</h3>
<p>首先获取到canvas，然后获取到canvas的二维上下文，然后设置笔刷的颜色，然后设置笔刷的范围。画出了绿色范围。</p>
<p><img alt="图片.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f36dbbbd4de9469f8c36ed4297efc6ab~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
video</p>
<p><img alt="图片.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/706be26df56b4d1ba6ff0d79a45f2d4e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            