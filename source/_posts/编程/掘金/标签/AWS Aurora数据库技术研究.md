
---
title: 'AWS Aurora数据库技术研究'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cfd219968ec45f1b9871fcdec08dd44~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 07:10:14 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cfd219968ec45f1b9871fcdec08dd44~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>最近在调研AWS云上提供的Aurora for mysql，Aurora是一种与 MySQL 和 PostgreSQL 兼容的关系型数据库，专为云打造，既具有传统企业数据库的性能和可用性，又具有开源数据库的简单性和成本效益。</p>
<p>虽然AWS网站上也有不少介绍，但想弄懂它，还是要花费不少精力的，因此记录如下，有相关需要的可以节省部分时间。</p>
<h1 data-id="heading-1">🎏 1.基本特点</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cfd219968ec45f1b9871fcdec08dd44~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-17_222000.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这款数据库，是基于AWS提供的自研引擎构建，其有下列特点：</p>
<ul>
<li>号称吞吐量比MySql快5倍</li>
<li>云上部署，可以快速扩展</li>
<li>存储容量可以自动扩展</li>
<li>可构建多大15个低延迟副本</li>
<li>除了经典的单主集群外，还有多主集群和无服务开箱即用等多种模式可选</li>
<li>高可用和持久性</li>
<li>全球数据库，异地容灾</li>
<li>快照、回溯、备份等</li>
<li>容错和自我修复</li>
</ul>
<p>广告做完了，如果有人想购买AWS服务，不要联系我，联系我也没有折扣。</p>
<h1 data-id="heading-2">🎏 2.技术分析</h1>
<p>看图好说话，一图胜万言。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d15394357ac548e58bd178a285802535~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-17_223145.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Aurora架构与MySQL RDS的单主集群相比较有这些区别：</p>
<ol>
<li>
<p>mysql的IO需要完成日志、binlog、data、帧文件、Double-Write等相关操作，其既需要写到本地存储，又需要同步到副本实例。</p>
</li>
<li>
<p>Aurora简化了IO操作，其仅仅写入LOG文件到存储卷即可，当然主副同步的时候也节省了大量数据，仅仅应用帧文件和日志即可。虽然没有直接写数据，但针对db实例来说，Data是不可或缺的，因此在Aurora的存储卷部分，会单独开启线程管理从Log解析为Data部分的工作。</p>
</li>
<li>
<p>Aurora的读写和MySql也是不同的，其采用了Quorum的6节点协议模式，在存储卷投票写完4个后，才算完成数据的写入，而读取的投票需要获取3个，也即需要读取3个存储节点，并且一致才行。</p>
</li>
</ol>
<p>其采用了分布式一致算法，确保数据能达到读写强一致性。</p>
<ol start="4">
<li>Aurora的读写主节点和只读副本节点均共享底层的存储卷，存储卷在3个不同的可用区内，保证了数据的多活特性。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16f4321e53542b5bb42ade6cc1147ed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
5. Aurora的只读副本同步数据来自主节点或临近节点的数据同步拷贝，拷贝的数据直接应用到mysql的数据缓存区，保证了副本快速的更新数据，当然在必须的时机，也需要同步来自存储卷的数据，这取决于其内置的算法。</p>
<p>和大多数的主从副本一样，从副本在数据的同步上和主节点之间有一定的延迟。AWS的延迟保证是小于100ms，一般平稳保持在10ms左右。</p>
<p>因此如果使用读写分离的场景，高一致性要求的事务应该只走主节点。要求不高的可以走只读副本。</p>
<h1 data-id="heading-3">🎏 3. IO写流程分析</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cc58ba7f223475694cbed5f80cf80cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>收到日志记录并入队列</li>
<li>写到更新队列存储并返回ACK。这里分析的是1个节点的存储，按照Quorum协议，有4个节点返回ACK，则可以认为写成功了。</li>
<li>组织记录和标识日志块</li>
<li>和存储节点协商读写</li>
</ol>
<p>5.展开日志到数据页
6.周期性记录日志和页数据到S3
7.周期性的回收老页数据
8.周期性验证数据合法性</p>
<p>全部步骤都是异步，写性能的延迟主要在步骤1和步骤2。</p>
<h1 data-id="heading-4">🎏 4. 部署结构图</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0980af9c22144f9596b3f815cde2d471~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在单主模式的DB集群下，DB存储是单独的虚拟存储卷，DB实例和DB只读副本构建这个之上，因此秒开实例是比较容易的，因为没有数据复制被需要。实例只有一个，在需要的时候可以被扩展。</p>
<p>这里仅仅介绍了单主模式。</p>
<h1 data-id="heading-5">🎏 5. 多主模式集群</h1>
<p>在多主模式集群下，所有DB实例均可读写，目前最大支持4个。</p>
<p>多主模式不支持单个实例读写其他只读的策略。</p>
<p>某个DB实例不可用后，没有故障切换处理机制，因为其他db实例直接接管写操作。</p>
<p>为了区分这种可用性，AWS称它是<strong>持续可用</strong>，以区分单实例的高可用。</p>
<p>多主集群需要处理写冲突，为了减轻用户负担，也可以开启多主强一致开关，可以开启先写后读，这种模式牺牲了部分性能。</p>
<h1 data-id="heading-6">🎏 06. 小结</h1>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            