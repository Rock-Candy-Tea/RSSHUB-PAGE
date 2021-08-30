
---
title: 'SSR 技术概述'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a877a5f998c24c79bca9677c8ed09f91~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 04:26:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a877a5f998c24c79bca9677c8ed09f91~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第30天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>服务端渲染的概念这几年可以说是炒得火热，它不是一种新型的技术，而是互联网最开始时所使用的加载技术。</p>
<p>那么到底是什么原因，使得人们愿意拭去历史的尘埃，让服务端渲染这一古老的概念重新绽放光芒呢？</p>
<h2 data-id="heading-1">什么是服务端渲染？</h2>
<p>服务端渲染简称 SSR，全称是 <code>Server Side Render</code>，是指一种传统的渲染方式，就是在浏览器请求页面URL的时候，服务端将我们需要的HTML文本组装好，并返回给浏览器，这个HTML文本被浏览器解析之后，不需要经过 JavaScript 脚本的执行，即可直接构建出希望的 DOM 树并展示到页面中。</p>
<p>SSR 有两种模式，单页面和非单页面模式，第一种是后端首次渲染的单页面应用，第二种是完全使用后端路由的后端模版渲染模式。他们区别在于使用后端路由的程度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a877a5f998c24c79bca9677c8ed09f91~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>与之相对的是 CSR（Client Side Render），是一种目前流行的渲染方式，它依赖的是运行在客户端的JS，用户首次发送请求只能得到小部分的指引性HTML代码。第二次请求将会请求更多包含HTML字符串的JS文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79117648c5744098b7e551890a802346~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">为什么需要 SSR ？</h2>
<p>目前前端流行的框架大都是适用于构建 SPA（单页面应用程序），在SPA这个模型中，是通过动态地重写页面的部分与用户交互，而避免了过多的数据交换，响应速度自然相对更高。</p>
<p>但是，SPA应用的首屏打开速度一般都很慢，因为用户首次加载需要先下载SPA框架及应用程序的代码，然后再渲染页面，并且 SPA 应用不利于 SEO 优化。</p>
<p>这时候，人们想着是不是可以将应用首页先加载出来，然后让首页用不到的其他 JS 文件再慢慢加载。但是由于 JS 引擎是单线程的，数据的组装过程会受到阻塞，单靠浏览器端的话不容易实现。</p>
<p>SSR 重新焕发活力的契机就在于此，如果将组装数据、渲染 HTML 页面的过程放在服务端，而浏览器端只负责显示接收到的 HTML 文件，那首屏的打开速度无疑会快很多。</p>
<h2 data-id="heading-3">SSR 的优缺点</h2>
<p>那么，SSR 技术到底有哪些优点呢？我们来列举一下：</p>
<ol>
<li>更快的响应时间，相对于客户端渲染，服务端渲染在浏览器请求URL之后已经得到了一个带有数据的HTML文本，浏览器只需要解析HTML，直接构建DOM树就可以。</li>
<li>有利于 SEO ，可以将 SEO 的关键信息直接在后台就渲染成 HTML，而保证搜索引擎的爬虫都能爬取到关键数据，然后在别人使用搜索引擎搜索相关的内容时，你的网页排行能靠得更前，这样你的流量就有越高。</li>
</ol>
<p>以上是 SSR 技术最主要的两大优点，虽有优势，但缺点也不容忽视：</p>
<ol>
<li>相对于仅仅需要提供静态文件的服务器，SSR中使用的渲染程序自然会占用更多的CPU和内存资源。</li>
<li>一些常用的浏览器API可能无法正常使用，比如<code>window</code>、<code>docment</code>和<code>alert</code>等，如果使用的话需要对运行的环境加以判断。</li>
<li>开发调试会有一些麻烦，因为涉及了浏览器及服务器，对于SPA的一些组件的生命周期的管理会变得复杂。</li>
<li>可能会由于某些因素导致服务器端渲染的结果与浏览器端的结果不一致。</li>
</ol>
<h2 data-id="heading-4">总结</h2>
<p>以上就是对 SSR 技术的一些简要介绍，总结一下就是：</p>
<ul>
<li>SSR 提高 SPA 应用的首屏响应速度，有利于 SEO 优化。</li>
<li>SSR 最适用于静态展示页面，如果页面动态数据较多时需要谨慎使用。</li>
<li>是否使用 SSR、使用到什么程度都需要开发者仔细权衡。</li>
</ul>
<p>~</p>
<p>~本文完，感谢阅读！</p>
<p>~</p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好，我是〖<a href="https://juejin.cn/user/2893570333750744/posts" target="_blank" title="https://juejin.cn/user/2893570333750744/posts">编程三昧</a>〗的作者 <strong>隐逸王</strong>，我的公众号是『<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fyinyiwang%2FblogImages%2Fraw%2Fmaster%2Fimages%2F20210604%2520%2F19-26-03-txvEvM.png" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/yinyiwang/blogImages/raw/master/images/20210604%20/19-26-03-txvEvM.png" ref="nofollow noopener noreferrer">编程三昧</a>』，欢迎关注，希望大家多多指教！</p>
<p>你来，怀揣期望，我有墨香相迎！ 你归，无论得失，唯以余韵相赠！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote></div>  
</div>
            