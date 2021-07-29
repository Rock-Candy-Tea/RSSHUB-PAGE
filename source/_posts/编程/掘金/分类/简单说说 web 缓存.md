
---
title: '简单说说 web 缓存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://user-gold-cdn.xitu.io/2018/12/6/16781b35cd6f9b90?imageView2/0/w/1280/h/960/ignore-error/1'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 01:44:19 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2018/12/6/16781b35cd6f9b90?imageView2/0/w/1280/h/960/ignore-error/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style>
<h1 data-id="heading-0">web 缓存</h1>
<p>web 缓存是可以自动保存常见文档副本的 HTTP 机制.当 web 请求抵达缓存时,如果本地已经有缓存副本,那么这时候就可以从本地获取副本数据,而不是重新再一次去服务端获取拉取这个文档.</p>
<h2 data-id="heading-1">缓存的优缺点</h2>
<p>优势</p>
<ul>
<li>减少了冗余的数据传输,节约了网络请求</li>
<li>减缓了网络瓶颈,不需要更多的带宽就能更快的加载页面</li>
<li>降低了原始服务器的要求.服务器可以更快的响应,避免过载</li>
</ul>
<p>劣势</p>
<ul>
<li>消耗内存</li>
<li>缓存数据可能和服务端数据不同步,不一致(服务的数据更新)</li>
</ul>
<h1 data-id="heading-2">缓存可分为强缓存和协商缓存</h1>
<ul>
<li>浏览器进行资源请求时，会判断 <strong>response headers</strong> 是否命中强缓存，如果命中，直接从本地读取缓存，不会向服务器发送请求，</li>
<li>当强缓存没有命中时，会发送请求到服务端，判断协商缓存是否命中，如果命中，服务器将请求返回，不会返回资源，告诉浏览器从本地读取缓存。如何不命中，服务器直接返回资源<br>
区别： 强缓存命中，不会请求服务器，直接请求缓存；协商缓存命中，会请求服务器，不会返回内容，然后读取缓存；</li>
<li>缓存的处理流程
<img src="https://user-gold-cdn.xitu.io/2018/12/6/16781b35cd6f9b90?imageView2/0/w/1280/h/960/ignore-error/1" alt="缓存的处理流程" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h1 data-id="heading-3">from memory cache 和 from disk cache</h1>
<p>memory</p>
<blockquote>
<p>200 form memory cache :
不访问服务器，一般已经加载过该资源且缓存在了内存当中，直接从内存中读取缓存。浏览器关闭后，数据将不存在（资源被释放掉了），再次打开相同的页面时，不会出现 from memory cache。</p>
</blockquote>
<p>disk</p>
<blockquote>
<p>200 from disk cache：
不访问服务器，已经在之前的某个时间加载过该资源，直接从硬盘中读取缓存，关闭浏览器后，数据依然存在，此资源不会随着该页面的关闭而释放掉下次打开仍然会是 from disk cache。</p>
</blockquote>
<p>优先访问 memory cache,其次是 disk cache，最后是请求网络资源</p>
<p>协商缓存: 向服务器发送请求，服务器会根据这个请求的 request header 的一些参数来判断是否命中协商缓存，如果命中，则返回 304 状态码并带上新的 response header 通知浏览器从缓存中读取资源；</p>
<h1 data-id="heading-4">强缓存和协商缓存的 header 参数</h1>
<h2 data-id="heading-5">强缓存</h2>
<ul>
<li>
<p>Expires：过期时间，如果设置了时间，则浏览器会在设置的时间内直接读取缓存，不再请求</p>
</li>
<li>
<p>Cache-Control：当值设为 max-age=300 时，则代表在这个请求正确返回时间（浏览器也会记录下来）的 5 分钟内再次加载资源，就会命中强缓存。</p>
</li>
<li>
<p>cache-control：除了该字段外，还有下面几个比较常用的设置值：</p>
<ul>
<li>max-age：用来设置资源（representations）可以被缓存多长时间，单位为秒；</li>
<li>s-maxage：和 max-age 是一样的，不过它只针对代理服务器缓存而言；</li>
<li>public：指示响应可被任何缓存区缓存；</li>
<li>private：只能针对个人用户，而不能被代理服务器缓存；</li>
<li>no-cache：强制客户端直接向服务器发送请求,也就是说每次请求都必须向服务器发送。服务器接收到 请求，然后判断资源是否变更，是则返回新内容，否则返回 304，未变更。这个很容易让人产生误解，使人误 以为是响应不被缓存。实际上 Cache-Control: no-cache 是会被缓存的，只不过每次在向客户端（浏览器）提供响应数据时，缓存都要向服务器评估缓存响应的有效性。</li>
<li>no-store：禁止一切缓存（这个才是响应不被缓存的意思）。</li>
</ul>
</li>
<li>
<p>cache-control 是 http1.1 的头字段，expires 是 http1.0 的头字段,如果 expires 和 cache-control 同时存在，cache-control 会覆盖 expires，建议两个都写。</p>
</li>
</ul>
<h2 data-id="heading-6">协商缓存</h2>
<p>Last-Modifed/If-Modified-Since 和 Etag/If-None-Match 是分别成对出现的，呈一一对应关系</p>
<h2 data-id="heading-7">Etag/If-None-Match</h2>
<p>Etag：是属于 HTTP 1.1 属性，它是由服务器（Apache 或者其他工具）生成返回给前端，用来帮助服务器控制 Web 端的缓存验证。
Apache 中，ETag 的值，默认是对文件的索引节（INode），大小（Size）和最后修改时间（MTime）进行 Hash 后得到的。</p>
<p>If-None-Match:当资源过期时，浏览器发现响应头里有 Etag,则再次像服务器请求时带上请求头 if-none-match(值是 Etag 的值)。服务器收到请求进行比对，决定返回 200 或 304</p>
<p><img src="https://user-gold-cdn.xitu.io/2019/5/6/16a8c60fb0ef49f0?imageView2/0/w/1280/h/960/ignore-error/1" alt="请求示意图" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">Last-Modifed/If-Modified-Since</h2>
<p>Last-Modified：浏览器向服务器发送资源最后的修改时间</p>
<p>If-Modified-Since：当资源过期时（浏览器判断 Cache-Control 标识的 max-age 过期），发现响应头具有 Last-Modified 声明，则再次向服务器请求时带上头 if-modified-since，表示请求时间。服务器收到请求后发现有 if-modified-since 则与被请求资源的最后修改时间进行对比（Last-Modified）,若最后修改时间较新（大），说明资源又被改过，则返回最新资源，HTTP 200 OK;若最后修改时间较旧（小），说明资源无新修改，响应 HTTP 304 走缓存。</p></div>  
</div>
            