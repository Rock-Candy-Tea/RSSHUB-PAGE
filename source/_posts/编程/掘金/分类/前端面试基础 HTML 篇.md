
---
title: '前端面试基础 HTML 篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5029'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:12:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=5029'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>写本文的目的是巩固一下前端的一些基础，互相交流一下，做一个综合的归纳</p>
</blockquote>
<p><a href="https://juejin.cn/post/6985047299466461192" target="_blank" title="https://juejin.cn/post/6985047299466461192">前端面试基础HTML篇</a></p>
<p><a href="https://juejin.cn/post/6985001275796488228" target="_blank" title="https://juejin.cn/post/6985001275796488228">前端面试基础CSS篇</a></p>
<h1 data-id="heading-0">HTML</h1>
<blockquote>
<p>面试HTML方面的一些问题，或者介绍，持续更新</p>
</blockquote>
<h2 data-id="heading-1">1. 语义化标签</h2>
<p>header、main、 footer、 nav、 section、 article、aside</p>
<p>details、 figcaption、 figure、 mark、 summary、 time、</p>
<p>前几个用的比较多，作用就不一一列出来</p>
<h2 data-id="heading-2">2. HTML、XML、XHTML</h2>
<p>1.XHTML可扩展超文本标记性语言，是由html到xml语言的一种过渡性语言，是一种在HTML 4.0基础上优化和改进的新语言，目的是基于XML应用。XHTML是一种增强了的HTML,XHTML 是更严谨更纯净的 HTML 版本。它的可扩展性和灵活性将适应未来网络应用更多的需求。</p>
<p>2.xml可扩展标记语言，是标准通用标记语言的子集，是一种标记电子文件使其具有结构性的标记语言，被设计用来传输和存储数据，是对超文本标记语言的补充。</p>
<p>3.html超文本标记语言，超文本是指网页中可以包括图片，链接，甚至音乐、程序等非文字元素，标记是用特定的符号来标记要显示的内容的各个部分。</p>
<h2 data-id="heading-3">3.<code><!Doctype html></code></h2>
<p><code><!doctype html></code> 的作用就是让浏览器进入标准模式，使用最新的 HTML5标准来解析渲染页面；如果不写，浏览器就会进入混杂模式，我们需要避免此类情况发生。</p>
<h2 data-id="heading-4">4.一个网页从开始请求道最终显示的完整过程</h2>
<pre><code class="copyable">一个网页从请求到最终显示的完整过程一般可以分为如下7个步骤：
（1）在浏览器中输入网址；
（2）发送至DNS服务器并获得域名对应的WEB服务器IP地址；
（3）与WEB服务器建立TCP连接；
（4）浏览器向WEB服务器的IP地址发送相应的HTTP请求；
（5）WEB服务器响应请求并返回指定URL的数据，或错误信息，如果设定重定向，则重定向到新的URL地址；
（6）浏览器下载数据后解析HTML源文件，解析的过程中实现对页面的排版，解析完成后在浏览器中显示基础页面；
（7）分析页面中的超链接并显示在当前页面，重复以上过程直至无超链接需要发送，完成全部数据显示
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://juejin.cn/post/6928677404332425223" target="_blank" title="https://juejin.cn/post/6928677404332425223">阿里面试官的”说一下从url输入到返回请求的过程“问的难度就是不一样！</a> 详细点的就看这位大佬写的</p>
<h2 data-id="heading-5">5.HTML中的Meta标签</h2>
<p>1.name属性</p>
<p><code>name 属性可以用来定义网页的关键字、描述、作者以及版权信息等等。</code></p>

























<table><thead><tr><th>常用属性值</th><th>说明</th></tr></thead><tbody><tr><td>keywords</td><td>用来定义网页的关键字。关键字可以是多个，之间需要用英文逗号,隔开。</td></tr><tr><td>description</td><td>用来定义网页的描述。</td></tr><tr><td>author</td><td>用来定义网页的作者。</td></tr><tr><td>copyright</td><td>用来定义网页的版权信息。</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span>   <span class="hljs-attr">content</span>=<span class="hljs-string">"一般是关键字类似的"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span>   <span class="hljs-attr">content</span>=<span class="hljs-string">"介绍"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span>   <span class="hljs-attr">content</span>=<span class="hljs-string">"author"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span>   <span class="hljs-attr">content</span>=<span class="hljs-string">"版权所有"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.charset属性</p>
<p><code>charset 是 HTML 5 中的新属性，用来定义页面的编码格式。</code></p>

























<table><thead><tr><th>常用属性值</th><th>说明</th></tr></thead><tbody><tr><td>ISO-8859-1</td><td>表示网页的默认编码格式。</td></tr><tr><td></td><td>UTF-8</td></tr><tr><td>gb2312</td><td>表示国际汉字码，不包含繁体。</td></tr><tr><td>gbk</td><td>表示国家标准扩展版。增加了繁体，包含所有亚洲字符集。</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"gb2312"</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"ISO-8859-1"</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"gbk"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.http-equiv属性</p>
<p><code>所有主流浏览器都支持 http-equiv 属性。它可以设置网页的过期时间，自动刷新等</code></p>





















<table><thead><tr><th>常用属性值</th><th>说明</th></tr></thead><tbody><tr><td>expires</td><td>设置网页的过期时间。</td></tr><tr><td></td><td>refresh</td></tr><tr><td>content-type</td><td>定义文件的类型，用来告诉浏览器该以什么格式和编码来解析此文件。</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"content-type"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"text/html"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"expires"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"0"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"refresh"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"1000"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.content-type常用属性值</p>

























<table><thead><tr><th>常用属性值</th><th>说明</th></tr></thead><tbody><tr><td>text/html</td><td>表示该文档是 HTML 格式的文档。</td></tr><tr><td>text/plain</td><td>表示该文档是纯文本格式的文档。</td></tr><tr><td>text/xml</td><td>表示该文档是 XML 格式的文档。</td></tr><tr><td>image/gif、jpeg、png</td><td>表示该文档是 gif、jpeg、png 图片格式的文档。</td></tr></tbody></table>
<p>可以设置 No-cache配置</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"pragma"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"no-cache"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"cache-control"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"no-cache"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"expires"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"0"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">6.form如何关闭自动完成功能</h2>
<p>form 或下面某个 input 设置为 <code>autocomplete = off</code>。</p>
<h2 data-id="heading-7">7.页面可见性（Page Visibility）</h2>
<p>浏览器标签页被隐藏或显示的时候会触发visibilitychange事件。
这是HTML5新提供的一个api，作用是记录当前标签页在浏览器中的激活状态。</p>
<p>具体可查看阮老师的文章
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2018%2F10%2Fpage_visibility_api.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2018/10/page_visibility_api.html" ref="nofollow noopener noreferrer">Page Visibility API 教程</a></p>
<h2 data-id="heading-8">8.渐进增强和优雅降级之间的区别</h2>
<p>渐进增强：先以低版本开始，保证基本的功能情况下，再针对高级浏览器进行效果，交互等方面的改进和追加功能，以达到更好的用户体验。</p>
<p>优雅降级：一开始就针对高版本的浏览器构建页面，先完善所有的功能，然后再针对低版本的浏览器进行兼容。</p>
<h2 data-id="heading-9">9.为什么利用多个域名来存储网站资源会更有效 （这是在掘友一篇文章中看到的，也记录下）</h2>
<ul>
<li>CDN缓存更加方便；</li>
<li>突破浏览器并发限制；</li>
<li>节约cookie宽带；</li>
<li>节约主域名的连接数，优化页面下响应速度；</li>
<li>防止不必要的安全问题；</li>
</ul>
<p><a href="https://juejin.cn/post/6844904180943945742#heading-62" target="_blank" title="https://juejin.cn/post/6844904180943945742#heading-62">html篇--这可能是目前较为全面的html面试知识点了吧</a></p>
<h2 data-id="heading-10">10.缓存</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Famandakelake%2Fblog%2Fissues%2F43" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/amandakelake/blog/issues/43" ref="nofollow noopener noreferrer">缓存的作用</a></p>
<p>少了Service Worker 做一下补充</p>
<p><a href="https://juejin.cn/post/6844903613270081543" target="_blank" title="https://juejin.cn/post/6844903613270081543">Service Worker —这应该是一个挺全面的整理</a></p></div>  
</div>
            