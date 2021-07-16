
---
title: '怎么让b站不挂'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4af1e9ccdfa54c11ab1217406b7f7626~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 20:12:32 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4af1e9ccdfa54c11ab1217406b7f7626~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>打开知乎和头条，b站又冲上了热榜，这次不是煽情怀旧的跨年晚会，也不是敲钟上市，而是“挂了”</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4af1e9ccdfa54c11ab1217406b7f7626~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>b站的程序员跟进迅速，问题也得到了比较快的修复。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4787dd4baca34e5788bb77657b4e78f2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哈哈哈，上面是热点新闻，下面就是知识点了。
最近在学习分布式架构，刚好看到了“两地三中心”的高可用架构，我们云畅享一下，如果b站也用的是两地三中心的架构，还会挂掉不？这里先说明下两个概念：RPO和RTO</p>
<ul>
<li>
<p>RTO (Recovery Time Objective，复原时间目标)是指灾难发生后，从IT系统故障导致业务停顿之时开始，到IT系统恢复至可以支持各部门运作、恢复运营之时，此两点之间的时间段称为RTO。比如说灾难发生后半天内便需要恢复，RTO值就是十二小时；</p>
</li>
<li>
<p>RPO (Recovery Point Objective，复原点目标)是指从系统和应用数据而言，要实现能够恢复至可以支持各部门业务运作，恢复得来的数据所对应时的间点。如果现时企业每天凌晨零时进行备份一次，当服务恢复后，系统内储存的只会是最近灾难发生前那个凌晨零时的资料。</p>
</li>
</ul>
<h1 data-id="heading-0">啥是两地三中心</h1>
<p>两地三中心架构，即生产数据中心、同城灾备中心、异地灾备中心的高可用容灾方案。在这种模式下，两个城市的三个数据中心互联互通，如果一个数据中心发生故障或灾难，其他数据中心可以正常运行并对关键业务或全部业务实现接管。相比同城多中心方案，两地三中心具有跨城级高可用能力，可以应对城市级自然灾害。</p>
<p>两地三中心是高可用架构的一种实现方式，它是以整个应用系统为单位，一般来说会分为应用和数据库两部分。</p>
<p>应用部分通常是无状态的，这个无状态就是说应用处理每个请求时不需要从本地加载上下文数据。这样启动多个应用服务器就没有什么额外的成本，应用之间没有上下文依赖，所以很容易做到多活。</p>
<p>数据库需要最终持久化数据，所有的业务都要基于已有数据，数据内容在不断发生变化，数据库服务有逻辑很重的上下文。因此数据库的多活难度就大多了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bfa1ac9e06e470e8b95dc2df5862e67~tplv-k3u1fbpfcp-watermark.image" alt="流程图.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前针对数据库双活的解决方案有很多种。总的来说分为两大类：分布式数据库多活方案以及传统数据库的双活方案。</p>
<h1 data-id="heading-1">传统数据库方案</h1>
<p>传统数据库如Oracle, DB2，Informix等。由于这些数据库本身并没有在原生状态下考虑双活问题。因此双活方案都是在原生体系外面通过附加解决方案来构建的。这类解决方案基本上也都是在解决一个问题：就是如何将多块部署在不同数据中心上的数据盘（数据块）逻辑上merge成一个。
从接替思路上基本上有两种：
方法1：通过存储设备层实现。如EMC的vplex解决方案，IBM的SVC解决方案，IBM的HyperSwap解决方案，浪潮存储双活方案等。都是通过存储层来实现的。
方法2：通过分布式文件系统实现。例如GPFS解决方案，就是属于这一类。通过GPFS分布式文件系统的Failure Group功能，将另一份双活数据同步地写到另一个数据中心去。
更多细节可以看这里 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F48728378%2Fanswer%2F1385829459" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/48728378/answer/1385829459" ref="nofollow noopener noreferrer">www.zhihu.com/question/48…</a></p>
<h1 data-id="heading-2">分布式数据库</h1>
<p>目前新型的分布式NewSQL数据库OceanBase、TiDB、MemFireDB等，在系统设计方面就充分考虑到了多活的需求。因此原生满足。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a68bfa4199d44340bd747cc57bc3bb67~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分布式数据库两地三中心建设架构基于 Raft或Paxos 算法，保证了集群数据一致性和高可用。raft或paxos算法都是多数派协议，两地是同城、异地，同城双中心指在同城或临近城市建立独立数据中心，双中心通过高速链路实时同步数据，网络延迟相对较小，另外一个数据中心在异地城市。在这种场景下，同城的两个中心超过半数完成提交，这样就不会因为与异地机房通讯时间长而推高数据库的操作延时。</p>
<p>如果同城机房有一个不可用，异地机房节点的投票就会发挥作用，那么数据库的服务仍然可以正常运行，数据也未发生丢失，此时RTO=0，RPO=0。但是如果同城发生了自然灾害，两个机房均不可用，此时数据库服务无法提供服务，数据也会丢失，RPO就不为零了。在此基础上还可以升级到三地三中心无副本，提供城市级别容灾，在邻近城市实现RPO为零。</p>
<h1 data-id="heading-3">引用</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcommunity.memfiredb.com%2Ftopic%2F28%2Fmemfire%25E6%258A%2580%25E6%259C%25AF%25E6%259E%25B6%25E6%259E%2584%25E7%25AE%2580%25E4%25BB%258B" target="_blank" rel="nofollow noopener noreferrer" title="https://community.memfiredb.com/topic/28/memfire%E6%8A%80%E6%9C%AF%E6%9E%B6%E6%9E%84%E7%AE%80%E4%BB%8B" ref="nofollow noopener noreferrer">community.memfiredb.com/topic/28/me…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F48728378%2Fanswer%2F1385829459" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/48728378/answer/1385829459" ref="nofollow noopener noreferrer">www.zhihu.com/question/48…</a></li>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fblog.itpub.net%2F26736162%2Fviewspace-2216584%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://blog.itpub.net/26736162/viewspace-2216584/" ref="nofollow noopener noreferrer">blog.itpub.net/26736162/vi…</a></li>
</ul></div>  
</div>
            