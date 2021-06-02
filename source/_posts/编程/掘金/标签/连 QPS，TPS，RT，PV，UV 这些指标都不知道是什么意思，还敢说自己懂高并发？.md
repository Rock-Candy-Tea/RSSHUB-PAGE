
---
title: '连 QPS，TPS，RT，PV，UV 这些指标都不知道是什么意思，还敢说自己懂高并发？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=7642'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 03:47:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=7642'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>废话不多说，直接开始。</p>
<h3 data-id="heading-0">QPS</h3>
<p>原理：每天 80% 的访问集中在 20% 的时间里，这 20% 时间叫做峰值时间。 </p>
<p>公式：( 总 PV 数 * 80% ) / ( 每天秒数 * 20% ) = 峰值时间每秒请求数（QPS）。</p>
<p>PV（page view）即页面浏览量，通常是衡量一个网络新闻频道或网站甚至一条网络新闻的主要指标。网页浏览数是评价网站流量最常用的指标之一，简称为 PV。</p>
<p>再来看一个计算机器数量的公式：</p>
<p>需要的机器数量：峰值时间每秒 QPS / 单台机器的 QPS。</p>
<p>举个例子，每天 300w PV 打在单台机器上，这台机器需要多少 QPS？ </p>
<p>( 3000000 * 0.8 ) / (86400 * 0.2 ) = 139 (QPS)。</p>
<p>一般需要达到 139 QPS，因为是峰值。（200 万 PV 才有 100 峰值 QPS）</p>
<h3 data-id="heading-1">TPS</h3>
<p>TPS：Transactions Per Second（每秒传输的事物处理个数），即服务器每秒处理的事务数。</p>
<p>TPS 包括一条消息入和一条消息出，加上一次用户数据库访问。</p>
<p>一个事务是指一个客户机向服务器发送请求然后服务器做出反应的过程。客户机在发送请求时开始计时，收到服务器响应后结束计时，以此来计算使用的时间和完成的事务个数。</p>
<p>一般的，评价系统性能均以每秒钟完成的技术交易的数量来衡量，系统整体处理能力取决于处理能力最低模块的 TPS 值。</p>
<h3 data-id="heading-2">RT（响应时长）</h3>
<p>响应时间是指：系统对请求作出响应的时间（一次请求耗时）。</p>
<p>直观上看，这个指标与人对软件性能的主观感受是非常一致的，因为它完整地记录了整个计算机系统处理请求的时间。由于一个系统通常会提供许多功能，而不同功能的处理逻辑也千差万别，因而不同功能的响应时间也不尽相同，甚至同一功能在不同输入数据的情况下响应时间也不相同。所以，在讨论一个系统的响应时间时，人们通常是指该系统所有功能的平均时间或者所有功能的最大响应时间。当然，往往也需要对每个或每组功能讨论其平均响应时间和最大响应时间。</p>
<p>对于单机的没有并发操作的应用系统而言，人们普遍认为响应时间是一个合理且准确的性能指标。需要指出的是，响应时间的绝对值并不能直接反映软件的性能的高低，软件性能的高低实际上取决于用户对该响应时间的接受程度。</p>
<p>对于一个游戏软件来说，响应时间小于 100 毫秒应该是不错的，响应时间在 1 秒左右可能属于勉强可以接受，如果响应时间达到 3 秒就完全难以接受了。而对于编译系统来说，完整编译一个较大规模软件的源代码可能需要几十分钟甚至更长时间，但这些响应时间对于用户来说都是可以接受的。</p>
<h3 data-id="heading-3">Load（系统负载）</h3>
<p>Linux 的 Load 是一个让新手不太容易了解的概念。Load 就是一定时间内计算机有多少个 active_tasks，也就是说是计算机任务执行队列的长度，CPU 计算的队列。</p>
<p>top/uptime 等工具默认会显示 1 分钟、5 分钟、15 分钟的平均 Load。</p>
<p>具体来说，平均 Load 是指，在特定的一段时间内统计的正在 CPU 中运行的（R 状态）、正在等待 CPU 运行的和处于不可中断睡眠的（D 状态）任务数量的平均值。        </p>
<p>最后，说一下 CPU 使用率和 Load 的关系吧。如果主要是 CPU 密集型的程序在运行，那么 CPU 利用率高，Load 一般也会比较高。</p>
<blockquote>
<p>If CPU utilization is near 100 percent (user + nice  +  system), the workload sampled is CPU-bound</p>
</blockquote>
<p>而 I/O 密集型的程序在运行，可能看到 CPU 的 %user, %system 都不高，%iowait 可能会有点高，这时的 Load 通常也比较高。</p>
<p>同理，程序读写慢速 I/O 设备（如磁盘、NFS）比较多时，Load 可能会比较高，而 CPU 利用率不一定高。这种情况，还经常发生在系统内存不足并开始使用 swap 的时候，Load 一般会比较高，而 CPU 使用率并不高。</p>
<h3 data-id="heading-4">PV</h3>
<p>页面访问次数：Page View。</p>
<h3 data-id="heading-5">UV</h3>
<p>访客数（去重复）：Unique Visitor。</p>
<p>以上。</p>
<p>关注微信公众号 <strong>AlwaysBeta</strong>，更多技术干货等你来。</p>
<p><strong>版权声明：</strong> 本文为 CSDN 博主「南无南有」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。</p>
<p><strong>原文链接：</strong> <a href="https://blog.csdn.net/qq_39416311/article/details/84892625" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/qq_39416311…</a></p></div>  
</div>
            