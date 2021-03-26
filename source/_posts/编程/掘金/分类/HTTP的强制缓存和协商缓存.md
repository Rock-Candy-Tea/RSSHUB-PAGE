
---
title: 'HTTP的强制缓存和协商缓存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/588e2c24a59f46c18e647e7b0c5a69e2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 19:34:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/588e2c24a59f46c18e647e7b0c5a69e2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">缓存的优缺点：</h3>
<p>优点</p>
<ol>
<li>节省流量宽带</li>
<li>降低服务器的要求，避免服务器过载</li>
<li>提高浏览器加载速度
缺点</li>
<li>消耗客户端内存</li>
</ol>
<h3 data-id="heading-1">强制缓存</h3>
<p>请求数据是时去缓存数据库查找，有则去出数据，没有则向服务器请求。</p>
<p><img alt="强制缓存" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/588e2c24a59f46c18e647e7b0c5a69e2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>（图片来自：<a href="https://juejin.cn/post/6844903517702848526" target="_blank">juejin.cn/post/684490…</a> ）
强缓存会用到请求头里的Expires和Cache-Control两个字段来表示</p>
<h4 data-id="heading-2">Expires</h4>
<p>Expires的值为数据到期时间，当请求时间小于Expires值的时候则使用缓存数据。</p>
<h4 data-id="heading-3">Cache-control</h4>
<p>是用来区分对缓存机制的支持情况，通过Cache-control的值来提供不同的缓存策略。
no-store：所有内容都不缓存
no-cache：需要验证缓存的数据
private：客户端可以缓存
public：服务端和客户端都可以缓存
max-age=t：缓存内容将在t秒后失效</p>
<h3 data-id="heading-4">协商缓存</h3>
<p>客户端会从缓存数据库获取标识，得到标识后去服务器验证是否失效，如未生效会返回304，客户端去缓存数据库获取数据</p>
<p><img alt="协商缓存" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77dc115b719c4341b7d072c587e77b1e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">Last-Modified</h4>
<p>last-Modified:服务器会返回资源最后修改时间
if-Modified-Since: 浏览器再次请求时会，会携带上最后修改时间。服务端接收到请求发现有请求头有if-Modified-Since会与资源的最后修改时间进行对比。如果一致则返回304，浏览器去缓存数据库获取资源，不一致返回请求的资源
if-Unmodified0Since:从某个时间开始，资源有没有被修改。没有修改返回200，修改过返回412</p>
<h4 data-id="heading-6">Etag</h4>
<p>Etag：服务器返回时通过这个字段返回随机生成的唯一标识
If-None-Match:浏览器再次请求时会带上次字段，值为服务器生成的唯一标识（Etag）,服务器接收到请求发现有If-None-Match会进行对比
• 不同：说明资源被修改过，返回新的资源状态200
• 相同：资源没有被修改过，返回304，浏览器去缓存数据库获取数据</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            