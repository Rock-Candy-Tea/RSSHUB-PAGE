
---
title: 'HTTP 缓存简介'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd006b9210f44c8f9aba9f387fa3103e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 06:24:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd006b9210f44c8f9aba9f387fa3103e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>缓存作为前端性能优化的有效方式之一，对于前端开发工程师来说，相对熟悉的就是 HTTP 缓存。</p>
<h3 data-id="heading-0">一、什么是 HTTP 缓存？</h3>
<p>HTTP 缓存指的是：当客户端向服务器请求资源时，会先抵达浏览器缓存，如果浏览器缓存中有“要请求的资源”的副本，则直接从浏览器缓存中获取，而不是从目标服务器中获取这个资源。</p>
<blockquote>
<p>虽然 HTTP 缓存不是必须的，但重用缓存的资源通常是必要的。然而常见的 HTTP 缓存只能存储 GET 响应，对于其他类型的响应则无能为力。</p>
</blockquote>
<h3 data-id="heading-1">二、为什么要用 HTTP 缓存？</h3>
<ul>
<li>减少冗余的数据传输</li>
<li>缓解服务器压力，提高网站性能</li>
<li>加快了客户端加载网页及资源的速度</li>
</ul>
<h3 data-id="heading-2">三、哪些资源可以被缓存？</h3>
<p>一般包括 html 页面和其他静态资源（js、img、css等）</p>
<h3 data-id="heading-3">四、HTTP 缓存分类</h3>
<ol>
<li>强缓存</li>
</ol>
<ul>
<li>Expires（HTTP 1.0）
<ul>
<li>Response Headers 中</li>
<li>控制缓存过期时间</li>
<li>已被 Cache-Control 代替</li>
<li>值为服务器端的绝对时间</li>
</ul>
</li>
<li>Cache-Control（HTTP 1.1）
<ul>
<li>Response Headers 中</li>
<li>控制强制缓存的逻辑</li>
<li>例如 Cache-Control: max-age=31536000（单位是秒）</li>
<li>值
<ul>
<li>max-age 缓存过期时间（相对时间）</li>
<li>no-cache 不用本地强制缓存，需要进行协商缓存，发送请求到服务器确认是否使用缓存。</li>
<li>no-store 不用本地强制缓存，也不用服务端缓存措施，每一次都要重新请求数据。</li>
<li>private 只能被终端用户缓存，比如：电脑 浏览器 手机等</li>
<li>public 允许被任何中间人（比如中间代理、CDN等）缓存</li>
</ul>
</li>
</ul>
</li>
</ul>
<ol start="2">
<li>协商缓存（对比缓存）</li>
</ol>
<ul>
<li>服务器端缓存策略（服务端判断资源能不能用缓存的内容）</li>
<li>服务器判断缓存资源是否和服务端资源一样（一致返回 304，否则返回 200 和最新的资源）</li>
<li>在 Response Headers 中，有两种
<ul>
<li>Last-Modified 资源的最后修改时间（只能精确到秒级）</li>
<li>Etag 资源的唯一标示（优先使用）</li>
</ul>
</li>
</ul>
<h3 data-id="heading-4">五、缓存执行流程</h3>
<p>浏览器在加载资源时，会先根据本地缓存资源的 header（expires 和 cahe-control） 中的信息判断是否命中强缓存，如果命中则直接使用缓存中的资源不会再向服务器发送请求。
当强缓存没有命中的时候，浏览器会发送一个请求到服务器，服务器根据 header（If-Modified-Since 和 If-None-Match）中的信息来判断是否命中缓存。如果命中，则返回 304 ，告诉浏览器资源未更新，可使用本地的缓存。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd006b9210f44c8f9aba9f387fa3103e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">六、刷新操作方式，对缓存的影响</h3>
<ul>
<li>三种刷新操作
<ul>
<li>正常操作：地址栏输入 url，跳转链接，前进后退等</li>
<li>手动刷新：F5，点击刷新按钮，右击菜单刷新</li>
<li>强制刷新：ctrl + F5（Mac：shift + command + r）</li>
</ul>
</li>
<li>不同刷新操作，不同的缓存策略
<ul>
<li>正常操作：强制缓存有效，协商缓存有效</li>
<li>手动刷新：强制缓存无效，协商缓存有效</li>
<li>强制刷新：强制缓存失效，协商缓存失效</li>
</ul>
</li>
</ul></div>  
</div>
            