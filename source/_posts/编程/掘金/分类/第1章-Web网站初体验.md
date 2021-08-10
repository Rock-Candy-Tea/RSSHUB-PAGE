
---
title: '第1章-Web网站初体验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc32182cae8e4c35ad5d6e811eb6dd6c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 18:21:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc32182cae8e4c35ad5d6e811eb6dd6c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>带着问题去看书学习，不失为一种好的方式。</p>
<p>HTML5＋CSS3＋JavaScript Web 前端开发案例教程（慕课版），微信读书中找到的学习Web前端书籍，好啦，我要带着课后习题，开始学习前端开发了，耶(＾－＾)V</p>
<h3 data-id="heading-0">习题</h3>
<h4 data-id="heading-1">1-1 网页制作的核心技术有哪些？</h4>
<p>HTML5（纯文本类型的语言）、CSS3（层叠样式表）和JavaScript（网页设计的一种脚本语言）</p>
<h4 data-id="heading-2">1-2 概述HTML5文件的基本结构。</h4>
<p>一个HTML5文件由一些元素和标签组成。元素是HTML5文件的重要组成部分，例如title（文件标题）、img（图片）及table（表格）等。元素名不区分大小写，HTML5用标签来规定元素的属性和它在文件中的位置。</p>
<h4 data-id="heading-3">1-3 创建一个HTML文档的开始标签是什么？结束标签是什么？</h4>
<p>文件的全部内容</p>
<h4 data-id="heading-4">1-4 元素的分类有哪些？请分别具体说明。</h4>
<ul>
<li>块状元素</li>
</ul>
<p>本身的属性为display:block的元素。不是块状的元素，通过设置display:block，可以将该元素变成块状元素。</p>
<p>1、在默认情况下，每个块状元素从新的一行开始，其后面的元素另起一行；</p>
<p>2、在默认情况下，块状元素是自上而下垂直排列，且每个块状元素独占一行；</p>
<p>3、块状元素一般都作为其他元素的容器，可以容纳内联元素和其他块状元素。</p>
<p>4、块状元素的高度，行高及其外边距和内边距都可以通过CSS属性来控制和调整！</p>
<p>5、在不设置宽度的情况下，块级元素的宽度则和它的父级元素的宽度一致。</p>
<p>6、在不设置高度的情况下，块级元素的高度则和它的父级元素的高度一致。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc32182cae8e4c35ad5d6e811eb6dd6c~tplv-k3u1fbpfcp-watermark.image" alt="块状元素" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li>内联元素</li>
</ul>
<p>指本身属性为display:inline的元素，其宽度随元素的内容而变化。不是内联元素，通过设置display:inline，可以将该元素变成内联元素。</p>
<p>1、内联元素不会独占一行，多个相邻的内联元素会排列在同一行中，顺序是从左到右排列，直到排列不下，才会另起新的一行；</p>
<p>2、内联元素设置高度height是无效的，宽度由其自身内容决定的，但高度可以通过行高line-height来进行调整；</p>
<p>3、内联元素设置宽度width是无效的，其宽度是由元素内容本身的大小决定的，比如文字、图片等；</p>
<p>4、内联元素设置外边距margin，只有左外边距margin-left和右外边距margin-right是有效的，而上下是无效的；</p>
<p>5、内联元素设置内边距padding，只有左内边距padding-left和右外边距padding-right是有效的，而上下是无效的；</p>
<p>6、内联元素只能容纳文本或者其他内联元素，请不要在内联元素中嵌套块状元素。</p>
<blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f8c0ee3b43749c496c3b24027a59ffc~tplv-k3u1fbpfcp-watermark.image" alt="内联元素" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li>块状内联元素</li>
</ul>
<p>内联块状元素（inline-block）就是既能设置宽高，又能独占一行显示，这样，同时具备了内联元素和块状元素的特点，设置display:inline-block，就是将元素转换成为内联块状元素类型。</p>
<p>1、内联块状元素和其他相邻元素同在一行， 但它们之间存在间隙，间隙大小为字体大小；</p>
<p>2、内联块状元素的高度、宽度、行高以及顶和底边距都可设置。</p>
<p>常见内联块状元素：</p>
<p>button，textarea，input、select、img是内联块状元素(inline-block)</p>
<h4 data-id="heading-5">1-5 说明网页中注释的意义以及添加注释的方式。</h4>
<p>适当的注释可以帮助用户更好地了解页面中各个模块的划分情况，也有助于以后对代码的检查和修改。给代码加注释，是一种很好的编程习惯。</p>
<ul>
<li>在文件开始标签中的注释：</li>
</ul>
<pre><code class="copyable"><!--注释的文字-->
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在CSS中的注释：</li>
</ul>
<pre><code class="copyable">/*注释的文字*/
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在JavaScript脚本语言中的注释</li>
</ul>
<pre><code class="copyable">单行注释:      //注释的文字
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">多行注释:      /*注释的文字*/
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">其他笔记</h3>
<ul>
<li><strong>查看网页源代码：单击鼠标右键，点击查看源代码</strong></li>
</ul>
<blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2116cf94c4ba4bb5bfd99f96a0eca614~tplv-k3u1fbpfcp-watermark.image" alt="右键" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99ea83f1528547a1b29293b19cef8ed5~tplv-k3u1fbpfcp-watermark.image" alt="掘金源代码" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li><strong>下载 WebStorm</strong></li>
</ul>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jetbrains.com%2Fwebstorm%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jetbrains.com/webstorm/" ref="nofollow noopener noreferrer">www.jetbrains.com/webstorm/</a></p>
</blockquote></div>  
</div>
            