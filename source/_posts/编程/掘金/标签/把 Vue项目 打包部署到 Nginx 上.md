
---
title: '把 Vue项目 打包部署到 Nginx 上'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8079'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:36:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=8079'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<h3 data-id="heading-1">吃饱饭才有力气写代码~</h3>
<p>昨天说到学了 Nginx 一些很基础的东西，但是也算是对这个东西有了基本的印象，突然想起来师傅之前也提到过把前端的 Vue 项目打包部署到 Nginx 上的过程，现在就结合者残存的记忆，以及在网络上找到的资料，把这一个过程稍微顺一顺~</p>
<h3 data-id="heading-2">打包项目</h3>
<p>我们都知道 Nginx 是一个高性能的HTTP和反向代理服务器，所有就用它来做静态资源服务器和后端的反向代理服务器。我用到的应该是用它部署我们用Vue搭建的前端项目。
<br></p>
<h4 data-id="heading-3">打包前</h4>
<p>在打包之前需要对我们写的Vue项目做一点点修改，因为开发环境和生产环境是不一样的。这个应该是具体项目具体分析吧！打包的时候会有相应的文档说明书的！应该是~</p>
<h4 data-id="heading-4">打包时</h4>
<p>在控制台的终端输入：npm run build<br>
等这个命令执行完会在项目结构的目录里看到增加了一个dist的文件夹，里面会有index.html，直接访问这个就可以。此外还有一个static的文件夹。<br>
到这打包就完成了，下面需要把这个包放到服务器上。</p>
<h3 data-id="heading-5">部署 Nginx</h3>
<h4 data-id="heading-6">复制粘贴</h4>
<p>把打包好的 dist 文件夹里的这两个文件（static 文件夹 和 index.html ）复制到 Nginx 文件中的 html 文件夹里，直接拖进去就行，会自动覆盖里面原来的东西。</p>
<h4 data-id="heading-7">修改 nginx.conf</h4>
<p>把内容复制粘贴进去以后需要在修改一下nginx 的配置文件；在 conf 的文件夹下的 nginx.conf 文件里，在 server 属性里面新增一个配置：</p>
<pre><code class="hljs language-js copyable" lang="js">location / &#123;
 try_files $uri $uri/  /index .html;  # 这里可以理解指定到 html 文件夹下的 index.html
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应该也是一样的道理，具体项目具体分析，会有相应的文档说明书的！</p>
<h4 data-id="heading-8">重启 Nginx</h4>
<p>配置完成后，需要重启 Nginx !启动成功后在浏览器输入相应 url ，成功的话就会看到自己项目的页面！</p>
<h3 data-id="heading-9">目前也只是听师傅简单讲了一遍Vue打包部署的流程，当时完全没意识到他在讲这些内容，也是后知后觉！还没有亲自上手操作过呢，到时候肯定会一步一个坎，再来补充！等我~</h3></div>  
</div>
            