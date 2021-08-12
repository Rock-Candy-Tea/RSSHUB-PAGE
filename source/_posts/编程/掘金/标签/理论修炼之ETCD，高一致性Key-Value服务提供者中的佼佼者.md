
---
title: '理论修炼之ETCD，高一致性Key-Value服务提供者中的佼佼者'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6630'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 06:52:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=6630'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>以往在架构选项的时候，大概了解其做什么的，有什么优劣就够了，因为大部分互联网企业比较轻文档重快速迭代，往往并不会纠结过多的选型方案。</p>
<p>只要方案合适，干就行了。</p>
<p>遥忆刚工作那会，流行瀑布式开发模式，方案和需求的重要性放在最顶级的位置，往往方案需要写几十上百页，关键的技术选项还需要编写关键技术选项，经过好几轮的评审才可能最终走向需求、概要、详细和总结。当然评审里领导各种角度的问题，往往让人不知所措。</p>
<p>经过这些年的“放松”，编写技术文档的水平也越来越差了，甚至于很多中间件也只是了解个皮毛，深层次的原理都不愿意仔细看看，只关注怎么能利用这些中间件干点什么事上。</p>
<p>这不，开始碰壁了，因为缺少理论层面的指导，很多过去认为理所当然的事情，在需要仔细阐述并争取领导同意上，就遇到了自己解释不清楚的各种问题。</p>
<p>怎么能快速说服领导上，遇到了很大的阻力。也让我看清楚了自己的问题之所在：缺乏理论依据。当然作为大领导是否需要深入的介入技术问题在这里不谈，因为人生唯一最大的事，莫过于修炼自身。</p>
<p>因此这篇文章送给我自己，修炼重在点滴间。</p>
<h1 data-id="heading-1">🎏 01.ETCD是干啥的?</h1>
<p><strong>etcd</strong>是一种高一致的分布式键值存储，它提供了一种可靠的方式来存储需要由分布式系统或机器集群访问的数据。它在网络内优雅地处理领导者选举，并且可以容忍机器故障，就算是领导者故障也不会影响高一致性。</p>
<p>作为高一致性解决方案三剑客之一的ETCD（其他还有ZooKeeper、Consul），其最大的特点就是保持高一致性。</p>
<h1 data-id="heading-2">🎏 02.一致性的概念</h1>
<p>一致性是分布式系统提出的一个概念，因为对于单机系统，几乎不存在一致性的问题。</p>
<p>而为了解决单机存储的单点故障，就从架构上升级为了主备系统，备份系统使用各种方案对主系统上的数据进行备份，以便保持和主系统的数据同步。</p>
<p>而一旦开始复制数据，那么就产生了一致性的问题。</p>
<p>一致性的定义：对某个指定的客户端，读操作能保证返回最新的写操作的结果。</p>
<h1 data-id="heading-3">🎏 2.1 CAP定理</h1>
<p>作为分布式系统中的最基础的定理，CAP是由加州大学的布鲁尔最先提出的一个猜想，最后被证明，而使之成为分布式计算领域公认的定理，因此也被称作布鲁尔定理。</p>
<p>CAP定理是说在一个分布式系统（互相链接并共享数据节点的集合）中，当涉及读写操作时，只能保证一致性（Consistency）、可用性（Avaliability）、分区容错性（Partition Tolerance)三者中的两个，另外一个必须被牺牲。</p>
<p>可用性指非故障节点在合理的时间内返回合理的响应（不包含错误和超时）。
分区容错：指当出现网络分区后，系统能够继续履行职责。 换句话说，系统部分节点出现故障后，连接正常节点还可以使用系统提供的服务。</p>
<p>不懂就搜，分区容错这个概念不好理解，因此这里引用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F54105974" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/54105974" ref="nofollow noopener noreferrer">知乎</a>的回答。</p>
<blockquote>
<p>一个分布式系统里面，节点组成的网络本来应该是连通的。然而可能因为一些故障，使得有些节点之间不连通了，整个网络就分成了几块区域。数据就散布在了这些不连通的区域中。这就叫分区。</p>
</blockquote>
<blockquote>
<p>当你一个数据项只在一个节点中保存，那么分区出现后，和这个节点不连通的部分就访问不到这个数据了。这时分区就是无法容忍的。</p>
</blockquote>
<blockquote>
<p>提高分区容忍性的办法就是一个数据项复制到多个节点上，那么出现分区之后，这一数据项就可能分布到各个区里。容忍性就提高了。</p>
</blockquote>
<blockquote>
<p>然而，要把数据复制到多个节点，就会带来一致性的问题，多个节点上面的数据可能是不一致的。要保证一致，每次写操作就都要等待全部节点写成功，而这等待又会带来可用性的问题。</p>
</blockquote>
<blockquote>
<p>总的来说就是，数据存在的节点越多，分区容忍性越高，但要复制更新的数据就越多，一致性就越难保证。为了保证一致性，更新所有节点数据所需要的时间就越长，可用性就会降低。</p>
</blockquote>
<p>对于分布式系统，理论上不可能舍弃P，因此可选方案经常时CP或者AP架构，当然舍弃并不是什么也不做，当发生分区时，可以做些事情，等到分区恢复后重新达到CA的状态。</p>
<h1 data-id="heading-4">🎏 2.2 一致性分类</h1>
<p>一致性按照副本复制的策略又可以分为四种类型：</p>
<ol>
<li>严格一致性：任何写入操作立即马上同步给所有节点。而在分布式系统中，数据的同步都需要时间，因此可想而知，这种模型是无法做到的。</li>
<li>线性一致性：任何一次读都能读到某个数据的最近一次写的数据。系统中的所有进程，看到的操作顺序，都和全局时钟下的顺序一致。</li>
<li>顺序一致性：不管系统怎么运行，得到的结果就好像把所有节点的所有操作按照某个sequential order排序后运行，但是在这个sequential order顺序中，来自同一个节点的操作仍然保持着它们在节点中被指定的顺序。</li>
<li>最终一致性（弱一致性）</li>
</ol>
<p>不保证在任意时刻任意节点上的同一份数据都是相同的，但是随着时间的迁移，不同节点上的同一份数据总是在向趋同的方向变化。简单说，就是在一段时间后，节点间的数据会最终达到一致状态。</p>
<h1 data-id="heading-5">🎏 2.3 共识</h1>
<p>共识（consensus）是分布式计算中最重要也是最基本的问题，它想要做的事情是：<strong>让所有节点就某事达成一致</strong>。共识问题中所有的节点要最终达成共识，由于最终目标是所有节点都要达成一致，所以根本不存在一致性强弱之分。</p>
<p>例如，Paxos是共识（Consensus）算法而不是强一致性（Consistency）协议。共识算法没有一致性级别的区分。</p>
<h1 data-id="heading-6">🎏2.4 两阶段提交</h1>
<p><strong>两阶段提交（two-phase commit）</strong> 是一种跨多节点实现<strong>原子提交</strong>的算法，即确保所有节点提交或所有节点中止。</p>
<p>ETCD中数据写同步也使用了两阶段提交，在leader收到写数据后变发起阶段1的写通知，如果超过半数的节点写了log，则发起第二阶段的正式写数据，并通知各个节点，如果半数写成功则提交数据，否则虽然不回滚数据，但后续可以覆盖之。</p>
<p>二阶段协议的关键，它通过两个阶段来把不可靠事务提交失败的几率降低到了最小，第一阶段一般占据了整个事务的大部分时间，而真正提交事务的第二阶段几乎是瞬间完成的，因此第二阶段出错的机率大大降低，所以这正是二阶段的巧妙之处。</p>
<p>现实中我们很少使用二阶段提交协议来保证事务性，为什么呢？</p>
<ol>
<li>在现实场景中，最常用的是基于BASE理论的最终一致性</li>
<li>提交协议需要<strong>锁定资源</strong>，在性能上会有一定损失，这在高并发的场景中是不适合的。</li>
<li>提交协议引入了事务管理器（TM），导致系统实现比较复杂，复杂的事情一般很少有人愿意做。</li>
<li>分布式事务的最高境界是没有分布式事务！</li>
</ol>
<h1 data-id="heading-7">🎏 03. ETCD的RAFT算法</h1>
<p>概括如下，详细的可以搜各类文章。</p>
<p>选择leader，每个节点都可能时 leader、follower、candidate（候选人）三种角色，集群节点采用心跳检查各个节点的在线，如果发现leader跪了，则follower可以把自己提升为candidate，并广播所有节点，开始选举，超过半数同意，就可以选作leader。</p>
<p>当然为了防止错误数据的节点被推选为leader，在选举中，必须带上自己保存的最新数据序列，以供其他节点比对。其他节点只有在检查发现你的数据正确或者更新的情况下才可以选举你为leader。</p>
<p>ooop，这里不存在拉票和作弊。</p>
<p>当然候选人也没有特别要求，如果条件都一样，则按照时间顺序的先来后到排队。</p>
<p>选出leader后，则每次写数据都是先写到leader，然后leader广播给所有节点，按照两阶段提交的方式写到整个集群。</p>
<h1 data-id="heading-8">🎏 04.通讯协议</h1>
<p>ETCD采用ProtoBuf编码，GRPC协议的方式读写数据，当然其也提供了更上层的http方式进行读写。
.net core 下有github下热心网友的封装类库，并没找到官方维护的sdk。</p>
<h1 data-id="heading-9">🎏 05. 小结</h1>
<p>理论的学习还是比较枯燥的，幸亏有你们的陪伴，分享何尝不是一种快乐！</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            