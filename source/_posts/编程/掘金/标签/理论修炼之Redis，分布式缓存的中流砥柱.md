
---
title: '理论修炼之Redis，分布式缓存的中流砥柱'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67e743f679d64b3caf0064e503197eb3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 05:51:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67e743f679d64b3caf0064e503197eb3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>日更这个活动，初看是一种逼迫，时间久了，真的就把自己锤炼成受虐狂了，到了时间点，总觉得要写点啥。</p>
<p>每天写写文章，还是蛮好玩的，梳理梳理知识体系，写完后偶有所得的样子，比刷抖音，刷完后索然无味的感觉强多了。</p>
<p>这次写写Redis，以前的系统都是很自然的上Redis，然后后续的很多功能也是借助Redis实现，比如分布式锁。</p>
<h1 data-id="heading-1">🎏 01.缓存是什么？</h1>
<p>这个问题来的很突然，一时之间竟然不知道怎么回答。
其实缓存非常常见，比如我们电脑里的RAM，其内容断电即丢，但少了它，即使你电脑能跑起来，那也必然是爬行的蜗牛。</p>
<p>当然除了RAM，还有CPU的L1和L2高速缓存，显卡的显存，看，缓存是多么常见啊。</p>
<blockquote>
<p>定义： 缓存就是用来加快数据请求的存储组件，又称作Cache。当某一对象/设备要读取数据时，会首先从缓存中查找需要的数据，找到了则直接执行，找不到的话则从其他慢速设备中查找。</p>
</blockquote>
<p>实际上凡是位于速度相差较大的两种设备之间，用于协调两者数据传输速度差的结构，均可以成为广义的缓存。</p>
<p>缓存并不只是放在内存，比如SSD硬盘的在某些场景下也可以作为缓存的存储介质。</p>
<h2 data-id="heading-2">🎏 01.1 常用硬件读写量级</h2>
<p>那么问题来了，我们常用的硬件，它们的读写速度都是什么量级的呢？</p>
<p>借用专家的图，来看看，务必在脑海中有这个印象哦。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67e743f679d64b3caf0064e503197eb3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">🎏 01.2 与缓冲区的区别</h2>
<p>以下观点属于程老大，无节操默写。</p>
<blockquote>
<p>易混淆概念，<strong>缓冲区（buffer）</strong>：系统两端处理速度平衡（从长时间尺度上看）时使用的。它的引入是为了减小短期内突发I/O的影响，起到流量整形的作用。比如生产者——消费者问题，他们产生和消耗资源的速度大体接近，加一个buffer可以抵消掉资源刚产生/消耗时的突然变化峰值。</p>
</blockquote>
<blockquote>
<p><strong>Cache（缓存）</strong>: 则是系统两端处理速度不匹配时的一种折衷策略。因为CPU和memory之间的速度差异越来越大，所以人们充分利用数据的局部性（locality）特征，通过使用存储系统分级（memory hierarchy）的策略来减小这种差异带来的影响。</p>
</blockquote>
<h2 data-id="heading-4">🎏 01.3 常见分类</h2>
<p>缓存的常见分类有静态缓存、分布式缓存和本地缓存。</p>
<ul>
<li>静态缓存，比如动态页面静态化，可以很容易进行CDN化顶住大流量；</li>
<li>分布式缓存：处于网络远端，通过分布式集群可以扩展缓存性能的组件。</li>
<li>本地缓存：一般是本地的内存，其速度优于分布式缓存，不需要跨越网络，一般用于短时热点缓存。</li>
</ul>
<h2 data-id="heading-5">🎏 01.4 应用场景</h2>
<p>缓存这么好，能解决所有问题吗？</p>
<p>想啥呢？缓存不能解决所有问题。</p>
<ul>
<li>缓存最适合读多写少，带热点的场景；</li>
<li>缓存带来了复杂度，并且有数据不一致的风险；</li>
<li>缓存一般使用内存，其容量相比硬盘差了好几个量级；</li>
</ul>
<p>引入缓存需谨慎设计读写方案，以避免这些问题。</p>
<h1 data-id="heading-6">🎏 02 常用缓存读写机制以及数据一致性问题</h1>
<ul>
<li>Cache Aside</li>
<li>Read Through/Write Through</li>
<li>Write Behind Caching</li>
</ul>
<h2 data-id="heading-7">🎏 02.1  Cache Aside</h2>
<p><code>读数据：先读缓存，如果没有命中缓存，则读取数据库，如果命中，则直接返回缓存</code></p>
<p><code>写数据：先更新数据库，再删除缓存</code></p>
<p>该模式在开发中最常用，需要我们熟练掌握。
当然其并不完美，<strong>我们知道在分布式系统中，想完全保证数据一致性是极为困难的事情</strong>。
极端情况如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eddae8231dc147da984ad5cb0266ba06~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">🎏 02.2  Read Through/Write Through</h2>
<p>引入了缓存组件。</p>
<p><code>读数据：先读缓存，如果没有命中缓存，则有缓存组件读取数据库并加载缓存，如果命中，则直接返回缓存</code></p>
<p><code>写数据：查询缓存是否命中，如果命中，则更新缓存，并由缓存组件同步到数据库，否则，由缓存组件直接写数据库</code></p>
<p>由于写数据时，同步写数据库，因此，速度上会有影响，这种模式并不常见，因为引入了缓存组件，增加了复杂度。</p>
<h2 data-id="heading-9">🎏 02.3 Write Behind Caching</h2>
<p>这种模式通常是先将数据写入缓存，再异步写入数据库。其优势是增加了吞吐量，劣势也很明显，如果发生宕机，则由丢失数据风险。</p>
<h1 data-id="heading-10">03. Redis 支持的类型</h1>
<p>这里只做罗列，并不细讲，相关文章太多了，自己搜搜参考吧。</p>
<p>Redis支持多种数据类型：string，hash，list，set、zset、Bitmap、HyperLogLogs、Streams。</p>
<p>Redis具有发布订阅消息功能，利用最新的数据类型Streams，据说可以做到非常强大的消息队列功能，之前看过一篇文章，有兴趣的可以搜搜。</p>
<h1 data-id="heading-11">04. Redis 过期时间和策略</h1>
<p>Redis支持很多方式设置一个key的过期时间，过期的Key我们是读取不到数据的，然而这个Key在服务器上还占空间吗？</p>
<p>默认情况下，是不清理内存占用的。</p>
<p>Redis有很多种内存淘汰机制，默认采用的是 noeviction。</p>
<ul>
<li>noeviction:默认策略，不淘汰，如果内存已满，添加数据就报错；</li>
<li>allkeys-lru:在所有键范围，选取最近使用频率最低的数据抛弃；</li>
<li>allkeys-random: 在所有键范围，随机抛弃；</li>
<li>volatile-lru:在设置了过期时间的所有键中，选取最近使用频率最低的数据抛弃；</li>
<li>volatile-ttl:在设置了过期时间的所有键，存活时间最短的数据抛弃；</li>
<li>volatile-random: 在设置了过期时间的所有键，随机抛弃；</li>
</ul>
<p>删除键不是一个小活，因此可以搭配定时删除和惰性删除相结合的方式进行。</p>
<h1 data-id="heading-12">05. Redis 高可用</h1>
<p>Redis <strong>Sentinel</strong> 为Redis提供高可用。这意味着使用 <strong>Sentinel</strong>，您可以创建一个 Redis 部署，无需人工干预即可抵抗某些故障。</p>
<p>Sentinel 功能：</p>
<ul>
<li><strong>监控</strong>，Sentinel 会不断检查您的主节点和副本节点是否按预期工作。</li>
<li><strong>通知</strong>，Sentinel 可以通过 API 通知系统管理员或其他计算机程序，其中一个受监控的 Redis 实例出现问题。</li>
<li><strong>自动故障转移</strong>，如果 master 没有按预期工作，Sentinel 可以启动一个故障转移过程，其中一个副本被提升为 master，其他额外的副本被重新配置为使用新的 master，并且使用 Redis 服务器的应用程序会被告知要使用的新地址连接。</li>
<li><strong>配置提供程序</strong>，Sentinel 充当客户端服务发现的权威来源：客户端连接到 Sentinel 以请求负责给定服务的当前 Redis 主节点的地址。如果发生故障转移，Sentinels 将报告新地址。</li>
</ul>
<h1 data-id="heading-13">🎏 06. 小结</h1>
<p>其实还有很多内容，我想写的更多，可是实力和时间不允许，暂时到这吧，后续有什么不妥的还可以修改追加，感谢你看到这里！</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            