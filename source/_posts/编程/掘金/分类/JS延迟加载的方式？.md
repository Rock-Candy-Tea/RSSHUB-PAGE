
---
title: 'JS延迟加载的方式？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7149'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 04:33:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=7149'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在网上找到6种，如果有其他的欢迎补充</p>
<h2 data-id="heading-0"><strong>1.defer属性</strong></h2>
<p>HTML 4.01 为<code> <script></code>标签定义了 defer属性。</p>
<p>用途：表明脚本在执行时不会影响页面的构造。也就是说，脚本会被延迟到整个页面都解析完毕之后再执行。</p>
<p>在<code><script></code> 元素中设置 defer 属性，等于告诉浏览器立即下载，但延迟执行。</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
    <script src="test1.js" defer="defer"></script>
    <script src="test2.js" defer="defer"></script>
</head>
<body>
<!-- 这里放内容 -->
</body>
</html>  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然<code><script></code> 元素放在了<code><head></code>元素中，但包含的脚本将延迟浏览器遇到<code></html></code>标签后再执行。</p>
<p>HTML5规范要求脚本按照它们出现的先后顺序执行。在现实当中，延迟脚本并不一定会按照顺序执行。</p>
<p>defer属性只适用于外部脚本文件。支持 HTML5 的实现会忽略嵌入脚本设置的 defer属性</p>
<h2 data-id="heading-1">2.<strong>async 属性</strong></h2>
<p>HTML5 为 <code><script></code>标签定义了 async属性。与defer属性类似，都用于改变处理脚本的行为。同样，只适用于外部脚本文件。
目的：不让页面等待脚本下载和执行，从而异步加载页面其他内容。</p>
<p>异步脚本一定会在页面 load 事件前执行。
不能保证脚本会按顺序执行。</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
    <script src="test1.js" async></script>
    <script src="test2.js" async></script>
</head>
<body>
<!-- 这里放内容 -->
</body>
</html>  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>async和defer一样，都不会阻塞其他资源下载，所以不会影响页面的加载。</p>
<p><strong>缺点：不能控制加载的顺序</strong></p>
<h2 data-id="heading-2">3.动态创建DOM方式</h2>
<pre><code class="copyable">//这些代码应被放置在</body>标签前(接近HTML文件底部)
<script type="text/javascript">  
   function downloadJSAtOnload() &#123;  
       varelement = document.createElement("script");  
       element.src = "defer.js";  
       document.body.appendChild(element);  
   &#125;  
   if (window.addEventListener)  
      window.addEventListener("load",downloadJSAtOnload, false);  
   else if (window.attachEvent)  
      window.attachEvent("onload",downloadJSAtOnload);  
   else 
      window.onload =downloadJSAtOnload;  
</script>  

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3"><strong>4.使用jQuery的getScript()方法</strong></h2>
<pre><code class="copyable">$.getScript("outer.js",function()&#123;
//回调函数，成功获取文件后执行的函数 console.log("脚本加载完成") 
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4"><strong>5.使用<code>setTimeout</code>延迟方法</strong></h2>
<h2 data-id="heading-5"><strong>6.让JS最后加载</strong></h2>
<p>把js外部引入的文件放到页面底部，来让js最后引入，从而加快页面加载速度</p></div>  
</div>
            