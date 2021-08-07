
---
title: '什么是Node.js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfe967c6a693438a86f30e784c8bf5d5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 06:49:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfe967c6a693438a86f30e784c8bf5d5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">什么是Node.js</h2>
<p>通常被用于一个BFF层 Backend For Frontend 服务于前端的后端，通俗说就是一个为前端业务提供数据的后端程序。特点是不需要太强的服务器运算能力，但对程序灵活性要求高。</p>
<p>有BFF层可以让前端有能力自由组装后台数据。前端可以自主决定和后台的通信方式，让前端工程师有更多的能力着手于web应用的性能优化，BFF层涉及到RPC调用，进程管理，系统运维等。</p>
<h5 data-id="heading-1">Node.js里运行js和chrome运行js有什么区别？</h5>
<p>Chrome浏览器用的和Node.js是一样的JavaScript引擎和模型。在Node.js中写JS和chrome写js几乎一样。但是还是有不同。主要分为以下两点：</p>
<ul>
<li>Node.js没有浏览器API，比如document,window等。</li>
<li>Node.js有很多自己的API，比如有文件系统，进程等</li>
</ul>
<p><strong>对开发者而言，你在Chrome中写的JS控制的是浏览器，而Node.js让你用类似的方式控制整台计算机</strong>。</p>
<p>留着官方的话，以后有一天应该能完全理解</p>
<blockquote>
<p>Node.js是一个基于Chrome V8引擎的JavaScript运行环境</p>
<p>Node.js使用了一个事件驱动、非阻塞式I/O的模型</p>
</blockquote>
<p>Node.js现阶段用于什么项目:</p>
<ul>
<li>
<p>web服务：腾讯视频，使用Node.js作为中间层，是为了<strong>搜索引擎优化和网页首屏加速</strong> = <strong>需要做服务端的渲染</strong>。</p>
</li>
<li>
<p>服务端渲染+前后端同构 = Node.js</p>
</li>
<li>
<p>构建工作流：一个是gulp，一个是webpack</p>
<ul>
<li>
<p><strong>gulp</strong>:可以对html,js,css各自做一些预处理</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfe967c6a693438a86f30e784c8bf5d5~tplv-k3u1fbpfcp-watermark.image" alt="image-20210806112453955" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对模板做了预编译；把less编译成了css；js有很多个js文件，通过gulp打包在了一起并且做了一个压缩混淆然后放在生产目录。</p>
</li>
<li>
<p><strong>webpack</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62aa403213624e41ab58c1e33634fbcf~tplv-k3u1fbpfcp-watermark.image" alt="image-20210806114134299" loading="lazy" referrerpolicy="no-referrer"></p>
<p>前端性能优化的一个重要原则，<strong>将资源尽可能的缩小，这样就可以建立尽可能少的http链接，这样就能加速网页加载</strong>。</p>
<p>为什么要用node.js作为构建工具，因为以往用Java,shell等做构建工具，前端人员不好修改，用node.js就是解决了这个问题。</p>
</li>
</ul>
</li>
</ul>

<ul>
<li>
<p><strong>Visual Studio Code</strong></p>
<p>他的底层技术基于electron，electron就是在node.js基础上封装了一个chrome浏览器内核，通过node.js和chronium的结合，可以让开发者在chrome跑node.js，同时node可以控制整个计算机。</p>
</li>
<li>
<p><strong>Twitch.tv</strong></p>
<p>以下左边为浏览器端，右边为mac应用</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11e587b103c04c799080c2ed0896ef94~tplv-k3u1fbpfcp-watermark.image" alt="image-20210806120632896" loading="lazy" referrerpolicy="no-referrer"></p>
<p>应用开发采用的就是node.js(electron)，可以看到应用最大限度的复用了浏览器。因为底层都是chrome内核，只不过一个是浏览器一个是node。</p>
</li>
</ul></div>  
</div>
            