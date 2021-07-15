
---
title: '【建议收藏】阿ken的 JavaScript笔记(一)_初识 JavaScript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9dccc43030c4d68ab400c16fb368fb0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 00:48:39 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9dccc43030c4d68ab400c16fb368fb0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>感激相遇
你好
我是阿Ken</strong></p>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9dccc43030c4d68ab400c16fb368fb0~tplv-k3u1fbpfcp-watermark.image" width="400px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>这是我在贵平台 ————“掘金”发的第一篇文，这还得益于掘金Troy的引荐：</p>
<p>(偷偷码一半哈哈哈)</p>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf23d90fea3e4b608ef7e0fd0a1d84be~tplv-k3u1fbpfcp-watermark.image" width="400px" height="500" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>在未来相当长一段时间都会在掘金上付出一定的精力和时间去运作这个号，希望贵平台可以带着我共同成长进步吧哈哈哈</p>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a06e3626e29644ec8626de9e2d74495f~tplv-k3u1fbpfcp-watermark.image" width="300px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f32a5ff27264ee796b1d36bc1bec40d~tplv-k3u1fbpfcp-watermark.image" width="300px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<p><strong>好好好，我们言归正传！</strong>
<strong>下面开始我的表演</strong></p>
<h1 data-id="heading-0">1.1_什么是JavaScript</h1>
<h2 data-id="heading-1">1.1.1_JavaScript概述</h2>
<p>JavaScript是Web开发领域中的一种功能强大的编程语言，主要用于开发交互式的Web页面。在计算机、手机等设备上浏览的网页上，大多数的交互逻辑几乎都是由JavaScript实现的。</p>





















<table><thead><tr><th>语言</th><th>作用及说明</th></tr></thead><tbody><tr><td>HTML</td><td>决定网页的结构和内容，相当于人的身体</td></tr><tr><td>CSS</td><td>决定网页呈现给用户的模样，相当于给人穿衣服，化妆</td></tr><tr><td>JavaScript</td><td>实现业务逻辑和页面控制，相当于人的各种动作</td></tr></tbody></table>
<p>JavaScript 内嵌于 HTML网页中，通过浏览器内置的 JavaScript引擎进行解释执行，把一个原本只用来显示的页面转变成支持用户交互的页面程序。</p>
<h2 data-id="heading-2">1.1.2_JavaScript的诞生与发展</h2>
<p>1995年，Netscape（网景）公司（现在的Mozilla公司）的布兰登·艾奇在网景导航者浏览器上首次设计出了JavaScript。</p>
<p>Netscape 最初将这个脚本语言命名为LiveScript，后来Netscape公司与Sun公司（2009年被Oracle公司收购）合作之后将其改名为JavaScript。</p>
<p>这是由于当时Sun公司推出的Java语言备受关注，Netscape 公司为了营销借用了 Java 这个名称。实际上，JavaScript 与 Java 的关系就像雷峰塔与雷锋。它们本质上是两种不同的编程语言。</p>
<h2 data-id="heading-3">1.1.3_JavaScript 的特点</h2>
<ol>
<li>JavaScript 是一种脚本语言</li>
</ol>
<p>脚本(Script）简单地说就是一条条的文本命令，这些命令按照程序流程逐条被执行。常见的脚本语言有 JavaScript，TypeScript，PHP，Python 等。非脚本语言(如C、C++）一般需要编译、链接，生成独立的可执行文件后才能运行，而脚本语言依赖于解释器，只在被调用时自动进行解释或编译。脚本语言通常都有简单、易学、易用特点。语法规则比较松散，使开发人员能够快速完成程序的编写工作。</p>
<ol start="2">
<li>JavaScript 可以跨平台</li>
</ol>
<p>JavaScript 语言不依赖操作系统，仅需要浏览器的支持。</p>
<ol start="3">
<li>JavaScript 支持面向对象</li>
</ol>
<h2 data-id="heading-4">1.1.4_JavaScript的组成</h2>
<p>JavaScript 是由 ECMAScript、DOM、 BOM 三部分组成的：</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/609bf4bdf67f45909030923d903a8757~tplv-k3u1fbpfcp-watermark.image" width="600px" height="200" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>接下来我们对 JavaScript 的组成进行简单的介绍：</p>
<p>(1) ECMAScript : 是 JavaScript 的核心。ECMAScript 规定了JavaScript 的编程语法和基础核心内容，是所有浏览器厂商共同遵守的一套 JavaScript 语法工业标准。</p>
<p>(2) DOM : 文档对象模型，是 W3C 组织推荐的处理可扩展标记语言的标准编程接口，通过 DOM 提供的接口，可以对页面上的各种元素进行操作(如大小、位置、颜色等)。</p>
<p>(3) BOM : 浏览器对象模型，它提供了独立于内容的、可以与浏览器窗口进行互动的对象结构。通过 BOM，可以对浏览器窗口进行操作 (如弹出框、控制浏览器导航跳转等)。</p>
<h1 data-id="heading-5">1.2_常用的开发工具</h1>
<p>工欲善其事，必先利其器，一款优秀的开发工具能够极大提高程序开发效率与体验。在 Web 前端开发中，常用的开发工具有 Visual Studio Code、Sublime Text、HBuilder 等，接下来我们就来介绍这些开发工具的特点。</p>
<ol>
<li>Visual Studio Code</li>
</ol>
<p>Visual Studio Code (简称VS Code) 是一款由微软公司开发的，功能十分强大的轻量级编辑器。该编辑器提供了丰富的快捷键，集成了语法高亮、可定制热键绑定、括号匹配以及代码片段收集的特性，并且支持多种语法和文件格式的编写。</p>
<ol start="2">
<li>Sublime Text</li>
</ol>
<p>Sublime Text 是一个轻量级的代码编辑器，具有友好的用户界面，支持拼写检查、书签、自定义按键绑定等功能，还可以通过灵活的插件机制扩展编辑器的功能，其插件可以利用 Python 语言开发。Sublime Text 是一个跨平 台的编辑器，支持 Windows、Linux、macOS 等操作系统。</p>
<ol start="3">
<li>HBuilder</li>
</ol>
<p>HBuider 是由 DCloud (数字天堂) 公司推出的一款支持 HTML5 的 Web 开发编辑器，在前端开发、移动开发方面提供了丰富的功能和贴心的用户体验，还为基于 HTML5 的移动端 App 开发提供了良好的支持。</p>
<ol start="4">
<li>Adobe Dreamweaver</li>
</ol>
<p>Adobe Dreamweaver 是一个集网页制作 和网站管理于一身的所见即所得的网页编辑器，用于帮助网页设计师提高网页制作效率，简化网页开发的难度和学习HTML5 、CSS 的门槛。但缺点是可视化编辑功能会产生大量冗余代码，而且不适合开发结构复杂、需要大量动态交互的网页。</p>
<ol start="5">
<li>WebStorm</li>
</ol>
<p>WebStorm 是 JetBrains 公司推出的一款 Web 前端开发工具，JavaScript、HTML5 开发是其强项，支持许多流行的前端技术，如 jQuery、Prototype、Less 、Sass、AngularJS、 ESLint、webpack等。</p>
<h1 data-id="heading-6">1.3_JavaScript 入门</h1>
<h2 data-id="heading-7">1.3.1_代码书写位置</h2>
<h3 data-id="heading-8">1. 行内式</h3>
<p>行内式是指将单行或少量的 JavaScript 代码写在 HTML 标签的事件属性中（也就是以 on 开头的属性，如 onclick）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">HTML</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>DOCUMENT<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"点我"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"alert('行内式')“>
</body>
</head>
</html>
</span></span><span class="copy-code-btn">复制代码</span></code></pre>
<p>使用行内式编写 JavaScript 代码。实现：单击一个按钮后，弹出一个警告框，显示一些提示信息</p>
<p>第四行声明了网页的编码为 UTF-8，帮助浏览器正确识别网页的编码。在声明编码后，还需要确保文件本身的编码也是 UTF-8。目前大多数代码编辑器新建的文件，编码默认都是UTF-8。另外 Windows 记事本默认的编码是ANSI，在记事本中编写的网页容易出现乱码，因此读者应杜绝使用记事本编写代码文件。</p>
<p>使用行内式需要注意：</p>
<ul>
<li>注意注意单引号和双引号的使用。在 HTML 中使用双引号，而 Javascript 推荐使用单引号。</li>
<li>行内式可读性较差，尤其是在 HTML 中编写大量的 JavaScript 代码时。不方便阅读。</li>
<li>在遇到多层引号镶嵌的情况时非常容易混淆，导致代码出错。</li>
<li>只有临时测试或者特殊情况下再使用行内式，一般情况下不推荐使用行内式</li>
</ul>
<h3 data-id="heading-9">2.  内嵌式（嵌入式）</h3>
<p>内嵌式是只使用 < script > 标签包裹 JavaScript 代码，< script > 标签可以把标签可以写在 < head > 或 < body > 标签中。通过内嵌式，可以将多行 JavaScript 代码写在 < script > 标签中。内嵌式是学习 JavaScript 最常使用的方式。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
......
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
alert(<span class="hljs-string">'内嵌式'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第四行是一条 JavaScript 语句，其末尾的分号表示该语句结束，后面可以编写下一条语句。< script > 标签还有一个 type 属性，在HTML5 中，该属性的默认值为 " text / JavaScript "，因此在编写时可以省略 type 属性。</p>
<h3 data-id="heading-10">3. 外部式（外链式）</h3>
<p>外部式是将 JavaScript 代码写在一个单独的文件中，一般使用 ” js “ 作为文件的扩展名。在 html 页面中使用 < script > 标签进行引入，适合 JavaScript 代码量比较多的情况。
外部式的是 < script > 标签内不可以编写 JavaScript 代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
......
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"test.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">alert(<span class="hljs-string">'外部式'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在 html 中还有一种嵌入 JavaScript 代码的方法，就是使用伪协议。</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:alert('伪协议')"</span>></span>点我<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在代码中，href 属性中的 “ JavaScript ” 就表示伪协议，后面一段 JavaScript 代码，当单击这个超链接后就会弹出 alert 警告框。在实际开发中<strong>不推荐使用</strong>这种方式。</p>
<p>在编写JavaScript代码时，应注意基本的语法规则，避免程序出错，具体如下：</p>
<ol>
<li><strong>JavaScript 严格区分大小写</strong>，在编写代码时一定注意大小写的正确性。例如：将案例代码中的 alert 改成大写的 ALERT，则警告框无法弹出。</li>
<li><strong>JavaScript 代码对空格、换行、缩进不敏感</strong>，一条语句可以分成。能多行书写。例如，将 alert 后面的 “（ ” 换到下一行，程序依然正确执行。</li>
<li>如果一条语句书写结束后，换行书写下一条语句，前一行语句后面的分号可以省略。</li>
</ol>
<h2 data-id="heading-11">1.3.2_注释</h2>
<h3 data-id="heading-12">1. 单行注释 “ // ”</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
alert(<span class="hljs-string">'Hello,JavaScript'</span>); <span class="hljs-comment">// 输出Hello,JavaScript</span>
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2. 多行注释 “ /* */ ”</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
alert(<span class="hljs-string">'Hello,JavaScript'</span>); 
<span class="hljs-comment">/* 输出
Hello,JavaScript
*/</span>
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">1.3.3_输入和输出语句</h2>





















<table><thead><tr><th>语句</th><th>说明</th></tr></thead><tbody><tr><td>alert（’msg‘）</td><td>浏览器弹出警告框</td></tr><tr><td>console.log（’msg‘）</td><td>浏览器控制台输出信息</td></tr><tr><td>prompt ('msg')</td><td>浏览器弹出输出框，用户可以输入内容</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
alert(<span class="hljs-string">"这是一个警告框"</span>); 
<span class="hljs-built_in">console</span>.log (<span class="hljs-string">'在控制台输出信息'</span>);
prompt (<span class="hljs-string">'这是一个输入框'</span>);
<span class="hljs-built_in">document</span>.write(<span class="hljs-string">"输出语句"</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad450932ee594cf9b4a0c0d8f74d55fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fac37b0a6b594ad89d72846046c56576~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc5a820d7159483c912c2c4504ef778c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eafbbf057e74e389978d4d049b94cf4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">1.3.4_控制台的使用</h2>
<p>在浏览器的控制台中可以直接输入 JavaScript 代码来执行。</p>
<div align="center">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c08377550ffe4efda641cae20d01acec~tplv-k3u1fbpfcp-watermark.image" width="700px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<h1 data-id="heading-16">1.4_JavaScript变量</h1>
<h2 data-id="heading-17">1.4.1_什么是变量</h2>
<p>变量是程序在内存中申请的一块用来存放数据的空间</p>
<h2 data-id="heading-18">1.4.2_变量的使用</h2>
<h3 data-id="heading-19">1. <strong>声明变量</strong></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> age;   <span class="hljs-comment">// 声明变量</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">2. <strong>变量赋值</strong></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">age = <span class="hljs-number">10</span>;   <span class="hljs-comment">// 为变量赋值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">alert(age);        <span class="hljs-comment">// 使用alert()警告框输出age的值</span>
<span class="hljs-built_in">console</span>.log(age);  <span class="hljs-comment">// 将age的值输出到控制台中</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><strong>变量初始化</strong></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> age = <span class="hljs-number">10</span>;   <span class="hljs-comment">//声明变量同时赋值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">1.4.3_变量的应用案例</h2>
<ol>
<li><strong>使用变量保存个人信息</strong></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">var</span> myName = <span class="hljs-string">'阿ken'</span>; <span class="hljs-comment">// 名称</span>
<span class="hljs-keyword">var</span> address = <span class="hljs-string">'xx市xx区'</span>; <span class="hljs-comment">// 地址</span>
<span class="hljs-keyword">var</span> age = <span class="hljs-number">19</span>; <span class="hljs-comment">// 年龄</span>
<span class="hljs-keyword">var</span> email = <span class="hljs-string">'aken@localhost'</span>; <span class="hljs-comment">// 电子邮箱</span>
<span class="hljs-built_in">console</span>.log(myName);
<span class="hljs-built_in">console</span>.log(address);
<span class="hljs-built_in">console</span>.log(age);
<span class="hljs-built_in">console</span>.log(email);  <span class="hljs-comment">//输出相应的值</span>
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50e35163e1e04089aea4f99d09633cfc~tplv-k3u1fbpfcp-watermark.image" width="700px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<ol start="2">
<li><strong>使用变量保存用户输入的值</strong></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">var</span> myName = prompt(<span class="hljs-string">'请输入您的名字'</span>);
alert(myName);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e070ed59421e40f5b078d9234192d1e0~tplv-k3u1fbpfcp-watermark.image" width="700px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>输入“阿ken”：</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f3f251fff1c4e5cb4cedb26c9c54e64~tplv-k3u1fbpfcp-watermark.image" width="700px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>然后：</p>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34401f93d9f042c08e37065ecd0dfe50~tplv-k3u1fbpfcp-watermark.image" width="700px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<h2 data-id="heading-22">1.4.4_变量的语法细节</h2>
<h3 data-id="heading-23">1. <strong>更新变量的值</strong></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> myName = <span class="hljs-string">'小明'</span>;   <span class="hljs-comment">//变量赋初值</span>
<span class="hljs-built_in">console</span>.log (myName);  <span class="hljs-comment">//输出结果：小明</span>
<span class="hljs-keyword">var</span> myName = <span class="hljs-string">'李华'</span>;  <span class="hljs-comment">//更新变量的值</span>
<span class="hljs-built_in">console</span>.log (myName)  <span class="hljs-comment">//输出结果：小红</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">2. <strong>同时声明多个变量</strong></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> myName,age,email;  <span class="hljs-comment">//同时声明多个变量，不赋值</span>
<span class="hljs-keyword">var</span> myName = <span class="hljs-string">'小明'</span>，
age = <span class="hljs-number">18</span>,
email = <span class="hljs-string">'xiaoming@localhost'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">3. <strong>声明变量的特殊情况</strong></h3>
<p>（1）<strong>只声明变量，但不赋值，则输出变量时，结果为 undefined</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> age;
<span class="hljs-built_in">console</span>.log (age);  <span class="hljs-comment">//输出结果：undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(2) <strong>不声明变量，直接输出变量的值，则程序会出错</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log (age);  
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果前一行代码出错，则后面的代码不会执行。因此，在开发中，如果代码没有按照期望的执行，可以打开控制台看一下是否有错误提示，找到具体是哪一行出错了</p>
</blockquote>
<p>（3）不声明变量，只进行赋值</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">age1 = <span class="hljs-number">10</span>;       <span class="hljs-comment">//变量age1没有使用var进行声明</span>
<span class="hljs-built_in">console</span>.log (age1);  <span class="hljs-comment">//输出结果：10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>从输出结果可以看出，直接赋值一个未声明的变量，也可以正确输出变量的值。这个情况是 JavaScript 语言的特性，学到全局作用域、window 对象的时候就理解了</p>
</blockquote>
<h2 data-id="heading-26">1.4.5_变量的命名规范</h2>
<p>在对变最进行命名时，需要遵循变量的命名规范，从而避免代码出错，以及提高代码的可读性</p>
<p><strong>①由字母、数字、下划线和美元符号($)组成，如age、num。</strong></p>
<p><strong>②严格区分大小写，如app和App是两个变量。</strong></p>
<p><strong>③不能以数字开头，如18age是错误的变量名。</strong></p>
<p><strong>④不能是关键字、保留字，如var、for、 while 等是错误的变量名。</strong></p>
<p>⑤要尽量做到“见其名知其意”，如age表示年龄，num表示数字。</p>
<p>⑥建议遵循<strong>驼峰命名法，首字母小写，后面的单词首字母大写，如myFirsName。</strong></p>
<p>在 JavaScript 中，关键字分为“保留关键字”和“未来保留关键字”。保留关键字是指在 JavaScript 语言中被事先定义好并赋予特殊含义的单词， 不能作为变量名使用。</p>
<p>未来保留关键字是指 ECMAScript 规范中预留的关键字，目前它们没有特殊功能，但是在未来的某个时间可能会加上。
未来保留关键字建议不要当作变量名来使用，以避免未来它们转换成关键字时出错。</p>
<blockquote>
<p><strong>标识符</strong></p>
<p>在 JavaScript 中还有一个标识符的概念。标识符是指开发人员为变量、函数取的名字。例如，变量名 age 就是一个标识符。从语法上来说，不能使用关键字作为标识符，否则会出现语法错误。</p>
</blockquote>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed5edc83b5a24163b871a149c89f5d23~tplv-k3u1fbpfcp-watermark.image" width="700px" height="600" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li><strong>要将脸朝向有光的地方</strong></li>
</ul>
<p><strong>时间长了
你自然学会了和自己相处的诀窍</strong></p>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2cc891e8ed44c1da9ffe2b14914f155~tplv-k3u1fbpfcp-watermark.image" width="700px" height="400" loading="lazy" referrerpolicy="no-referrer">
</div>
<ul>
<li><strong>愿这一遭走过</strong></li>
</ul>
<p><strong>仍能心怀梦想</strong>
<strong>不丢信仰</strong></p>
<p><strong>你好，我是阿Ken
感谢来访</strong></p>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3544a3ff8ca143a1bf7dfce42606570f~tplv-k3u1fbpfcp-watermark.image" width="500px" height="300" loading="lazy" referrerpolicy="no-referrer">
</div>
<p><strong>哦豁</strong>
<strong>路过的宝儿请把大拇哥、小星星、评论区点亮一下</strong></p></div>  
</div>
            