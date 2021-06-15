
---
title: '一起了解基于React的服务端渲染&同构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669189740f87450e8ad16524107bfef9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 06:35:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669189740f87450e8ad16524107bfef9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第14天，活动详情查看 <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">概念分析：</h2>
<p>服务端渲染（SSR）</p>
<ul>
<li>更好的⾸屏性能</li>
<li>更利于 SEO，爬虫可以直接抓取已渲染的内容</li>
</ul>
<p>客户端渲染</p>
<ul>
<li>前后分离，⻚⾯的交互</li>
</ul>
<p>同构：服务端和客户端都可以运⾏的同⼀套代码</p>
<ul>
<li>同一套代码，复用率，可维护性增强</li>
<li>同时具有SSR与前后端分离的优势，利于 SEO 优化</li>
<li>更好的性能与更好的用户体验</li>
</ul>
<h2 data-id="heading-1">架构思路及要点</h2>
<p>React提供了服务器渲染的各种API，可快速满足同构需求。
同一份代码要在服务端与客户端各执行一次，首屏加载完服务端渲染的页面后，客户端紧接着继续执行并重新渲染页面，接管后续的页面交互。</p>
<h2 data-id="heading-2">同构关键点</h2>
<p>所谓同一份代码同时运行服务端和客户端，其实可复用的基本为组件，服务端与客户端的差异无法完全被抹平，而React的好处就是对服务端构建提供了不少解决方案。</p>
<h3 data-id="heading-3">1. 路由不同</h3>
<p>客户端使用：<code><BrowserRouter /></code>    服务端使用：<code><StaticRouter /></code></p>
<h3 data-id="heading-4">2. 代码的同构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669189740f87450e8ad16524107bfef9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">ReactDOMServer.renderToString(element);
官方文档：
https://reactjs.org/docs/react-dom-server.html#rendertostring
源码分析：
https://github.com/facebook/react/blob/master/packages/react-dom/src/server/ReactDOMStringRenderer.js
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">ReactDOM.hydrate, 同全完法用 ReactDOM.render
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">总结：</h2>
<ul>
<li>双端路由怎么工作</li>
</ul>
<p>具体看代码，路由两端分开维护</p>
<ul>
<li>数据同构</li>
</ul>
<p>数据部分使用redux来互通</p>
<ul>
<li>渲染同构</li>
</ul>
<p>代码部分同构使用react</p>
<blockquote>
<p>SSR架构图</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a308230adbf14d2dab1ec2f396839ebb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上对基于React的同构方案进行了简单的介绍以及要点梳理，希望对你有帮助。</p>
<p>感兴趣的童鞋可以尝试一步步从零开始实现一个React同构项目Demo。</p>
<blockquote>
<p>参考资料：</p>
<p><a href="https://imweb.io/topic/5d2da910b17a4bd24bd0678a" target="_blank" rel="nofollow noopener noreferrer">imweb.io/topic/5d2da…</a> 腾讯IMWEB团队</p>
</blockquote></div>  
</div>
            