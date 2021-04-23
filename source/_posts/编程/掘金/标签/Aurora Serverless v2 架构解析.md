
---
title: 'Aurora Serverless v2 架构解析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6615cac01d7f4007a5d707803689b6d1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 02:36:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6615cac01d7f4007a5d707803689b6d1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>如果Aurora v1是数据库中革命性一个版本，但在Aurora Serverless V2这里也只能说是V1是一个实验性的版本，V2才算是真正的成熟。这里从AWS Invent大会获得的资料来解析一下Aurora Serverless V2。该架构感觉也是给数据库行业揭开了一个新的篇章。</p>
<p><strong>官宣：</strong> Amazon Aurora Serverless v2 目前为预览版，可以在不到一秒的时间内完成扩展，瞬间将处理能力从数百个事务扩展到数十万个事务。在扩展过程中，系统会以极为精细的增量调整容量，从而确保恰好提供应用程序所需的数据库资源量。您无需管理数据库容量，并且只需为您的应用程序使用的容量付费。与按照峰值负载来预置容量相比，您最高可以节省 90% 的数据库成本。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6615cac01d7f4007a5d707803689b6d1~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Aurora’s architecture</p>
<p>Aurora Serverless v2从架构上看有三个组件：RDS proxy , Query Layer 和Storage layer三层。三层服务相对独立实现， 只有Query layer是基于第三方的开源代码实现。</p>
<p>RDS Proxy</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42493772098745a580193cdba2e1e736~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RDS Proxy也可以说为Router Layer。实现上非常轻量。Router Layer可以理解为是一个Proxy但具备连接池和流控的作用。支持MySQL，PostgresSQL协议。</p>
<p>Proxy只是简单的处理连接请求及把请求路由到正确的Query进程之外还有两个目的：</p>
<ol>
<li>
<p>从原始的数据库中剥离出来，形成连接成的Serverless架构更易伸缩 。</p>
</li>
<li>
<p>会话保持后面的存储节点或是Query层重启，也可以保持客户端的连接不断开。</p>
</li>
</ol>
<p>路由层还可以跟踪数据库的连接分析数据库的使用及性能情况以便实现自动扩容，这种对于Serverless架构把接入层独立出来非常的重要。在一些版本中Aurora还支持通过HTTP Data API请求SQL，该设计就是基于router层来得的益处。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0828d14826274137b4b86487010c7790~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于写操作，也可以直接通过Primary 节点处理，对于Primary节点就处于一种非serverless架构下（如果不经过Proxy可能最大的问题就是没有写节点的高可用保障）</p>
<p>Query层</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7d8fe5c75e943c3b53b9a92be64bbd1~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以称query layer为数据库层，这个是主要的事务处理及计算实现的组件。通过Router层和Query层相连，同时接触Router层传递的SQL并执行，读取写入存储层的的数据和索引。</p>
<p>Query layer是直接借签使用开源的PostgreSQL和MySQL的代码，这部分代码基本没有变化，所以在使用Aurora时也要注意一下和那个版本的特性匹配（目前看MySQL是5.7的）在经典的software-as-a-Service的架构中一般是一个API支持多版本请求，但Aurora中只支持固定的版本对所有用户服务（避免多版本，让开发更轻松）。在自动扩展和自动故障转移方面更多的和自已托管的开源数据库方案一样。</p>
<p>在Aurora集群中同时只有一个写实例，可以支持多个read-only实例（目前支持15个）。和使用MySQL的Master/Slave一样的。</p>
<p>Query进程是跑在Vm中，所以选择合理的配置，可以让Query层获得更好的性能。这点更加体现了Serverless架构设计中，把计算层重的地方单独剥离出来，独立部署的好处了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b766632acd44456885c97530b0b7c86~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">Storage层</h3>
<p>Aurora中Storage层使用云上高速S3块存储构建。存储层使用Log-Structured  engine原生分布式设计。 同个Region中6副本，至少保证写4份才算成功。</p>
<p>在Aurora中Storage层控制数据在Region中及多Region中复制，该复制通过存储层实现的。这复制不同于传统的OS RDS通过RDMS自身的Query处理。</p>
<p>在Aurora中为了保证数据的强一致性，不管在哪个Region中的读写事务（或是强一致性的读)，写事务必须由路由到主进程处理。读操作可以走其它Reader进程，读取的数据最终都是一致的（从技术来讲Aurora也可以做到Multi-primary的对外服务模型，但有可能破坏数据的一致性）</p>
<p>由于这个限制，在Aurora中读写事务会随着Client和主进程之间的物理离增大而变的响应时间增长。针对这个问题Aurora在设计上引入了process-to-process的转发请求，尽可能的命中Local数据请求命中返回，但这个不能从根本上避免所有的强一致性的事务必须走主进程请求的性能问题。另外强一致的事务并发请求在主进程请求中也没有隔离。</p>
<p>为了高可用，每个Aurora Region为每个数据库保持6个副本，每个AZ中保存2个副本。从而来减少故障对于应用的最小影响：</p>
<ul>
<li>
<p>在不同的AZ中总共丢掉两个副本，用户是感知不到的。</p>
</li>
<li>
<p>在同一个AZ中丢失两个副本，则该AZ的请求用户会感知延迟增大，因为在这个AZ的请求自动转迁移到其它AZ中，但这个数据库依然可以提供写操作。</p>
</li>
<li>
<p>如果丢失三个副本将会让数据库进入只读模式，能写入，但数据不会丢失。</p>
</li>
<li>
<p>如果丢失4个副本整个集群可能不可用，且有可能造成数据丢失</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/883b494c5f0d4a89acd4c057b5dd95a4~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>--------------------------------</p>
<p>可能解析有误，直接把油管地址放出来自取：<a href="https://www.youtube.com/watch?v=PQHZrtIgdiA" target="_blank" rel="nofollow noopener noreferrer">www.youtube.com/watch?v=PQH…</a> 。欢迎交流。</p></div>  
</div>
            