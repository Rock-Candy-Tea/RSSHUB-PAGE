
---
title: '字节面试被虐后，是时候搞懂 DNS 了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/408987c0882245cfb1c6a8d853c9d501~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 05:51:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/408987c0882245cfb1c6a8d853c9d501~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前几天面了字节</p>
<blockquote>
<p>👦🏻：“浏览器从输入URL到显示页面发生了什么？”</p>
<p>👧🏻：%^&@#^&（这我怎么可能没有准备？从网络到渲染说了一通后）</p>
<p>👦🏻：“你刚刚提到了 DNS，那说说 DNS 的查询过程吧”</p>
<p>👧🏻：“DNS 查询是一个递归 + 迭代的过程...”</p>
<p>👦🏻：“那具体的递归和迭代过程是怎样的呢？”</p>
<p>👧🏻：“...”</p>
</blockquote>
<p>当时我脑子里有个大概的过程，但是细节就记不起来了，所以今天就来梳理一下 DNS 相关的内容，如有不妥之处，还望大家指出。</p>
<h2 data-id="heading-0">什么是 DNS</h2>
<p>DNS 即域名系统，全称是 <strong>D</strong>omain <strong>N</strong>ame <strong>S</strong>ystem。当我们在浏览器输入一个 URL 地址时，浏览器要向这个 URL 的主机名对应的服务器发送请求，就得知道服务器的 IP，对于浏览器来说，DNS 的作用就是将<strong>主机名转换成 IP 地址</strong>。下面是摘自《计算机网络：自顶向下方法》的概念：</p>
<blockquote>
<p>DNS 是：</p>
<ol>
<li>一个由分层的 DNS 服务器实现的<strong>分布式数据库</strong></li>
<li>一个使得主机能够查询分布式数据库的<strong>应用层协议</strong></li>
</ol>
</blockquote>
<p>也就是，DNS 是一个应用层协议，我们发送一个请求，其中包含我们要查询的主机名，它就会给我们返回这个主机名对应的 IP；</p>
<p>其次，DNS 是一个分布式数据库，整个 DNS 系统由分散在世界各地的很多台 DNS 服务器组成，每台 DNS 服务器上都保存了一些数据，这些数据可以让我们最终查到主机名对应的 IP。</p>
<p><strong>所以 DNS 的查询过程，说白了，就是去向这些 DNS 服务器询问，你知道这个主机名的 IP 是多少吗，不知道？那你知道去哪台 DNS 服务器上可以查到吗？直到查到我想要的 IP 为止。</strong></p>
<h2 data-id="heading-1">分布式、层次数据库</h2>
<h5 data-id="heading-2">什么是分布式？</h5>
<p>这个世界上没有一台 DNS 服务器拥有因特网上所有主机的映射，每台 DNS 只负责部分映射。</p>
<h5 data-id="heading-3">什么是层次？</h5>
<p>DNS 服务器有 3 种类型：根 DNS 服务器、顶级域（Top-Level Domain, TLD）DNS 服务器和权威 DNS 服务器。它们的层次结构如下图所示：</p>
<div align="center">
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/408987c0882245cfb1c6a8d853c9d501~tplv-k3u1fbpfcp-watermark.image" alt="DNS 的层次结构.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>图片来源：《计算机网络：自顶向下方法》</p>
<ul>
<li>根 DNS 服务器</li>
</ul>
<p>首先我们要明确根域名是什么，比如 <code>www.baidu.com</code>，有些同学可能会误以为 <code>com</code> 就是根域名，其实 <code>com</code> 是顶级域名，<code>www.baidu.com</code> 的完整写法是 <code>www.baidu.com.</code>，最后的这个 <code>.</code> 就是根域名。</p>
<p>根 DNS 服务器的作用是什么呢？就是管理它的下一级，也就是顶级域 DNS 服务器。通过询问根 DNS 服务器，我们可以知道一个主机名对应的顶级域 DNS 服务器的 IP 是多少，从而继续向顶级域 DNS 服务器发起查询请求。</p>
<ul>
<li>顶级域 DNS 服务器</li>
</ul>
<p>除了前面提到的 <code>com</code> 是顶级域名，常见的顶级域名还有 <code>cn</code>、<code>org</code>、<code>edu</code> 等。顶级域 DNS 服务器，也就是 TLD，提供了它的下一级，也就是权威 DNS 服务器的 IP 地址。</p>
<ul>
<li>权威 DNS 服务器</li>
</ul>
<p>权威 DNS 服务器可以返回主机 - IP 的最终映射。</p>
<p>关于这几个层次的服务器之间是怎么交互的，接下来我们会讲到 DNS 具体的查询过程，结合查询过程，大家就不难理解它们之间的关系了。</p>
<h2 data-id="heading-4">本地 DNS 服务器</h2>
<p>之前对 DNS 有过了解的同学可能会发现，上一节的 DNS 层次结构，为什么没有提到本地 DNS 服务器？因为<strong>严格来说，本地 DNS 服务器并不属于 DNS 的层次结构</strong>，但它对 DNS 层次结构是至关重要的。那什么是本地 DNS 服务器呢？</p>
<p>每个 ISP 都有一台本地 DNS 服务器，比如一个居民区的 ISP、一个大学的 ISP、一个机构的 ISP，都有一台或多台本地 DNS 服务器。当主机发出 DNS 请求时，该请求被发往本地 DNS 服务器，<strong>本地 DNS 服务器起着代理的作用</strong>，并负责将该请求<strong>转发</strong>到 DNS 服务器层次结构中。</p>
<p>接下来就让我们通过一个简单的例子，看看 DNS 的查询过程是怎样的，看看客户端、本地 DNS 服务器、DNS 服务器层次结构之间是如何交互的。</p>
<h2 data-id="heading-5">递归查询、迭代查询</h2>
<p>如下图，假设主机 <code>m.n.com</code> 想要获取主机 <code>a.b.com</code> 的 IP 地址，会经过以下几个步骤：</p>
<div align="center">
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bb796a3045e409aabb0f89ad40d3fad~tplv-k3u1fbpfcp-watermark.image" alt="DNS.png" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<ol>
<li>
<p>首先，主机 <code>m.n.com</code> 向它的本地 DNS 服务器发送一个 DNS 查询报文，其中包含期待被转换的主机名 <code>a.b.com</code>；</p>
</li>
<li>
<p>本地 DNS 服务器将该报文转发到根 DNS 服务器；</p>
</li>
<li>
<p>该根 DNS 服务器注意到 <code>com</code> 前缀，便向本地 DNS 服务器返回 <code>com</code> 对应的顶级域 DNS 服务器（TLD）的 IP 地址列表。</p>
<p>意思就是，我不知道 <code>a.b.com</code> 的 IP，不过这些 TLD 服务器可能知道，你去问他们吧；</p>
</li>
<li>
<p>本地 DNS 服务器则向其中一台 TLD 服务器发送查询报文；</p>
</li>
<li>
<p>该 TLD 服务器注意到 <code>b.com</code> 前缀，便向本地 DNS 服务器返回权威 DNS 服务器的 IP 地址。</p>
<p>意思就是，我不知道 <code>a.b.com</code> 的 IP，不过这些权威服务器可能知道，你去问他们吧；</p>
</li>
<li>
<p>本地 DNS 服务器又向其中一台权威服务器发送查询报文；</p>
</li>
<li>
<p>终于，该权威服务器返回了 <code>a.b.com</code> 的 IP 地址；</p>
</li>
<li>
<p>本地 DNS 服务器将 <code>a.b.com</code> 跟 IP 地址的映射返回给主机 <code>m.n.com</code>，<code>m.n.com</code> 就可以用该 IP 向 <code>a.b.com</code> 发送请求啦。</p>
</li>
</ol>
<div align="center">
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdd07ee6ec0d492a95e48d4ed9b0d0e8~tplv-k3u1fbpfcp-watermark.image" alt="bqb4.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>“你说了这么多，递归呢？迭代呢？”</p>
<p>这位同学不要捉急，其实递归和迭代已经包含在上述过程里了。</p>
<p>主机 <code>m.n.com</code> 向本地 DNS 服务器 <code>dns.n.com</code> 发出的查询就是<strong>递归查询</strong>，这个查询是主机 <code>m.n.com</code> 以自己的名义向本地 DNS 服务器请求想要的 IP 映射，并且本地 DNS 服务器直接返回映射结果给到主机。</p>
<p>而后继的三个查询是<strong>迭代查询</strong>，包括本地 DNS 服务器向根 DNS 服务器发送查询请求、本地 DNS 服务器向 TLD 服务器发送查询请求、本地 DNS 服务器向权威 DNS 服务器发送查询请求，<strong>所有的请求都是由本地 DNS 服务器发出，所有的响应都是直接返回给本地 DNS 服务器</strong>。</p>
<p>那么问题来了，所有的 DNS 查询都必须遵循这种<strong>递归 + 迭代</strong>的模式吗？</p>
<p>当然不是。</p>
<p>从理论上讲，<strong>任何 DNS 查询既可以是递归的，也可以是迭代的</strong>。下图的所有查询就都是递归的，不包含迭代。</p>
<div align="center">
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd1422f81c2647a19cde72cb9694bc89~tplv-k3u1fbpfcp-watermark.image" alt="DNS2.png" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>看到这里，大家可能会有个疑问，TLD 一定知道权威 DNS 服务器的 IP 地址吗？</p>
<p>emmm...</p>
<div align="center">
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9bf80ce5eb9471d95bbe9c248d0d0cb~tplv-k3u1fbpfcp-watermark.image" alt="bqb7.png" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>还真不一定，有时 TLD 只是知道中间的某个 DNS 服务器，再由这个中间 DNS 服务器去找到权威 DNS 服务器。这种时候，整个查询过程就需要更多的 DNS 报文。</p>
<h2 data-id="heading-6">DNS 缓存</h2>
<p>为了让我们更快的拿到想要的 IP，DNS 广泛使用了缓存技术。DNS 缓存的原理非常简单，在一个 DNS 查询的过程中，当某一台 DNS 服务器接收到一个 DNS 应答（例如，包含某主机名到 IP 地址的映射）时，它就能够将映射缓存到本地，下次查询就可以直接用缓存里的内容。当然，缓存并不是永久的，每一条映射记录都有一个对应的生存时间，一旦过了生存时间，这条记录就应该从缓存移出。</p>
<p>事实上，<strong>有了缓存，大多数 DNS 查询都绕过了根 DNS 服务器</strong>，需要向根 DNS 服务器发起查询的请求很少。</p>
<h2 data-id="heading-7">面试感想</h2>
<p>这次面试收获还蛮大的，有些东西以为自己懂了，以为自己能说清楚，但到了真的要说的时候，又没有办法完整地梳理出来，描述起来磕磕绊绊，在面试中会很减分。</p>
<p>所以不要偷懒，不要抱有侥幸心理，踏实学。共勉。</p>
<h2 data-id="heading-8">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F30280001%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/30280001/" ref="nofollow noopener noreferrer">计算机网络（原书第7版）</a></p></div>  
</div>
            