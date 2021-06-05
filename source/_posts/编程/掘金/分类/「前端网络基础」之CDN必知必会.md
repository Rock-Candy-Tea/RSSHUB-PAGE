
---
title: '「前端网络基础」之CDN必知必会'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d93e38049da44bbfbc625ad22d2c3725~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 00:22:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d93e38049da44bbfbc625ad22d2c3725~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>想必大家公司的网站，为了加快用户访问网络资源的速度和稳定性提高用户体验，减轻源服务器的访问压力，
都使用了CDN缓存吧。那么何为CDN，原理是什么，今天就给大家普及普及。
（如果还不清楚DNS的同学可以先看一下这篇<a href="https://juejin.cn/post/6969101232166141965" target="_blank">「前端网络基础」之DNS必知必会
</a>,先大概了解一下DNS，已经了解的可以跳过）。</p>
<h2 data-id="heading-0">CDN是什么</h2>
<p>CDN的全称是(Content Delivery Network)，即内容分发网络。其目的是通过在现有的Internet中增加一层新的CACHE(缓存)层，将网站的内容发布到最接近用户的网络”边缘“的节点，使用户可以就近取得所需的内容，提高用户访问网站的响应速度。从技术上全面解决由于网络带宽小、用户访问量大、网点分布不均等原因，提高用户访问网站的响应速度。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d93e38049da44bbfbc625ad22d2c3725~tplv-k3u1fbpfcp-watermark.image" alt="edgeserver.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">CDN的工作原理</h2>
<p>DNS解析过程大家应该都知道吧，这里来复习一下，也可以看看这篇文章<a href="https://juejin.cn/post/6969101232166141965" target="_blank">「前端网络基础」之DNS必知必会
</a>。</p>
<p>当一个用户在地址栏输入 <a href="http://www.abc.com/" target="_blank" rel="nofollow noopener noreferrer">www.abc.com</a> 时，DNS解析大致有以下过程，如图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a14b01be8d74a1d991ae5a9f4d7272b~tplv-k3u1fbpfcp-watermark.image" alt="DNS解析" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>浏览器先检查自身缓存中有没有被解析过的这个域名对应的ip地址，如果有，解析结束。同时域名被缓存的时间也可通过TTL属性来设置。</li>
<li>如果浏览器缓存中没有（专业点叫还没命中），浏览器会检查操作系统缓存中有没有对应的已解析过的结果（我们这里假设缓存中没有结果，继续下一步）。</li>
<li>请求本地域名服务器（LDNS）来解析这个域名，这里采用的是递归查询（假设依旧没有命中）。</li>
<li>如果LDNS仍然没有命中，就向根域名服务器请求解析，后续就开始迭代查询了。</li>
<li>根域名服务器返回给LDNS下一次应该查询的顶级域名服务器IP。</li>
<li>LDNS向顶级域名服务器查询，顶级域名服务器返回下一次应该查询的权限域名服务器IP。</li>
<li>LDNS向权限域名服务器查询，权限域名服务器返回所查询的目标主机IP。</li>
<li>LDNS将最终查询到的IP返回给用户的主机，并写入缓存以便下次查询。</li>
</ol>
<p>这样的DNS解析有个问题：</p>
<blockquote>
<p>由于网民数量激增，网络访问路径过长，从而使用户的访问质量受到严重影响。特别是当用户与网站之间的链路被突发的大流量数据拥塞时，对于异地互联网用户急速增加的地区来说，访问质量会不太稳定，响应速度会慢。</p>
</blockquote>
<p>CDN就是为了解决这个问题而诞生的：</p>
<blockquote>
<p>通过在现有的Internet中增加一层新的<code>CACHE(缓存)层</code>，将网站的内容发布到最接近用户的网络”边缘“的节点，使用户可以就近取得所需的内容，提高用户访问网站的响应速度。基本原理是广泛采用各种缓存服务器，将这些缓存服务器分布到用户访问相对集中的地区或网络中，在用户访问网站时，利用全局负载技术将用户的访问指向距离最近的工作正常的缓存服务器上，由缓存服务器直接响应用户请求。</p>
</blockquote>
<ul>
<li>使用了CDN缓存后的网站的访问过程变为这样，如下图所示：</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccfb9827c8ff4692b0e65be3147c89c7~tplv-k3u1fbpfcp-watermark.image" alt="640.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>用户输入访问的域名,操作系统向本地域名服务器（LDNS）查询域名的ip地址.</li>
<li>LDNS向根域名服务器（ROOT DNS）查询域名的授权服务器(这里假设LDNS缓存过期)</li>
<li>ROOT DNS将域名授权dns记录回应给 LDNS</li>
<li>LDNS得到域名的授权dns记录后,继续向域名授权dns查询域名的ip地址</li>
<li>域名授权dns 查询域名记录后(一般是<code>CNAME</code>)，回应给 LDNS</li>
<li>LDNS 得到域名记录后,向智能调度DNS查询域名的ip地址</li>
<li>智能调度DNS 根据一定的算法和策略(比如静态拓扑，容量等),将最适合的CDN节点ip地址回应给 LDNS</li>
<li>LDNS 将得到的域名ip地址，回应给 用户端</li>
<li>用户得到域名ip地址后，访问站点服务器</li>
<li>CDN节点服务器应答请求，将内容返回给客户端.(缓存服务器一方面在本地进行保存，以备以后使用，二方面把获取的数据返回给客户端，完成数据服务过程)</li>
</ol>
<p>这里解释一下<code>CNAME</code>，CNAME即别名( Canonical Name )；可以用来把一个域名解析到另一个域名，当 DNS 系统在查询 CNAME 左面的名称的时候，都会转向 CNAME 右面的名称再进行查询，一直追踪到最后的 PTR 或 A 名称，成功查询后才会做出回应，否则失败。</p>
<p>例如，你有一台服务器上存放了很多资料，你使用docs.example.com去访问这些资源，但又希望通过documents.example.com也能访问到这些资源，那么你就可以在您的DNS解析服务商添加一条CNAME记录，将 documents.example.com 指向 docs.example.com，添加该条CNAME记录后，所有访问 documents.example.com 的请求都会被转到 docs.example.com，获得相同的内容。</p>
<h2 data-id="heading-2">CDN的功能</h2>
<p>归纳起来，CDN具有以下主要功能：</p>
<ol>
<li>节省骨干网带宽，减少带宽需求量</li>
<li>提供服务器端加速，解决由于用户访问量大造成的服务器过载问题；</li>
<li>服务商能使用Web Cache技术在本地缓存用户访问过的Web页面和对象，实现相同对象的访问无须占用主干的出口带宽，并提高用户访问因特网页面的相应时间的需求；</li>
<li>能克服网站分布不均的问题，并且能降低网站自身建设和维护成本；</li>
<li>降低“通信风暴”的影响，提高网络访问的稳定性。</li>
</ol>
<h2 data-id="heading-3">参考资料</h2>
<ul>
<li><a href="https://www.jianshu.com/p/1dae6e1680ff" target="_blank" rel="nofollow noopener noreferrer">CDN加速原理</a></li>
<li><a href="https://juejin.cn/post/6969101232166141965" target="_blank">「前端网络基础」之DNS必知必会</a></li>
</ul></div>  
</div>
            