
---
title: '测试开发之前端篇-Web前端简介'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9019'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 23:37:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=9019'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>自从九十年代初，人类创造出网页和浏览器后，Web取得了长足的发展，如今越来越多的企业级应用也选择使用Web技术来构建。</p>
<p>前面给大家介绍<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.easycorp.cn%2Fthread%2F291506.html" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.easycorp.cn/thread/291506.html" ref="nofollow noopener noreferrer">网络协议</a>时讲到，您在阅读这篇文章时，浏览器是通过HTTP/HTTPS协议向服务器发送请求、并显示了其响应内容的。本文给大家简要介绍下，网页在浏览器中展现和互动时，主要涉及到的以下几个方面的技术。希望此系列文章，对大家工作中的Web测试用例设计、自动化测试，以及网站问题定位有所帮助。</p>
<h3 data-id="heading-0">HTML（HyperText Markup Language，超文本标记语言）</h3>
<p>用于描述网页的结构和内容，包涵了很多标签（tag）组成的元素(element)。如使用段落标签p，可以定义一个形如*</p><p>hello world</p>*的段落元素。<p></p>
<p>在浏览器窗口中，按F12键打开”开发人员工具“，在名为Elements的标签中，您可以查看到整个页面的HTML代码。</p>
<pre><code class="copyable"><html>
  <head>
    <title>网页标题</title>
    <meta name="keywords" content="测试开发,自动化测试,软件测试">
    <style type="text/css">
     h3 &#123;color: blue&#125;
    </style>
  </head>
  </head>
  <body>
    <div>
      <h3>这是一个标题</h3>
      <p>这是一个段落。</p>
    </div>
  </body>
  <script type="text/javascript">
    console.log('hello world')
  </script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，各元素的解释如下：<br>
- head： 文档头部，包含网页的信息元素；<br>
- title： 文档标题；<br>
- meta： 元数据，这里的keywords设置了一些可供搜索引擎检索的关键字；<br>
- style： CSS样式表，详见后续章节；<br>
- body： 文档主体，包含页面所要展示的内容；<br>
- script：JavaScript脚本，详见后续章节。</p>
<h3 data-id="heading-1">CSS（Cascading Style Sheets，层叠式样式表）</h3>
<p>定义如何显示 HTML里的元素，包括其布局、大小、风格、色彩等，从而实现网页的内容和显示方式相分离。</p>
<pre><code class="copyable"><style type="text/css">
  h3 &#123;color: blue&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的样式针对h3元素设置了color属性，效果为h3标签中的文字显示为蓝色。</p>
<h3 data-id="heading-2">JavaScript（动态脚本语言）</h3>
<p>运行于浏览器中的一种动态解析脚本语言，用于客户端和服务器的数据交换，并实现网页同用户的交互等。</p>
<pre><code class="copyable"><script type="text/javascript">
  alert('hello world')
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上JavaScript代码，在页面加载结束后，会在弹出一个内容为”hello world“警告窗口。</p>
<h3 data-id="heading-3">Web服务器</h3>
<p>主要用于解析HTML、图片、CSS、JS等静态资源，如Nginx服务器。有些Web服务器可以通过配置相应的程序模块，实现动态内容的解析，如Apache使用模块解析PHP语言编写的脚本。</p>
<h3 data-id="heading-4">应用服务器</h3>
<p>完成业务逻辑处理，同更持久层（如数据库）交换数据，装载数据到模板生成静态网页等功能。通常应用服务器也会内嵌一个Web服务器，以实现将处理好的静态网页以HTML流的形式返回给浏览器。</p>
<h3 data-id="heading-5">前后端分离</h3>
<p>传统的Web应用是在服务器端生成静态HTML响应的，比如PHP、ASP、JSP等。前后端分离的架构下，网页的静态部分更接近于一个HTML模板，浏览器从服务器获取模板后，再通过执行JavaScript来请求服务器、获取数据、装载到模板，最终在用户自己的设备上完成网页的渲染。</p></div>  
</div>
            