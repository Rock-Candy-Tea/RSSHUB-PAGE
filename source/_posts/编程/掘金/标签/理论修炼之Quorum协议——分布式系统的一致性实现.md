
---
title: '理论修炼之Quorum协议——分布式系统的一致性实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd605b809e08490fa3ba2f079536da1f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 06:47:29 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd605b809e08490fa3ba2f079536da1f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第16天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>“但凡有现成的中间件或者开源库，就拿现成的用吧，不要再造轮子了。”之前公司的某同事曾经这么说过。</p>
<p>有现成的东西拿来用，固然轻松惬意省劲，可是当没有现成的东西或者不够合适的时候，我们也需要知道构建它的原理，甚至自己动手构建出类似的组件。</p>
<p>当然多学一下别人的底层思路甚至原理，遇到问题的时候，思路大开，或许就刚好恰当的解决了手中的问题。</p>
<h1 data-id="heading-1">🎏 01. Quorum的缘起？</h1>
<p>1979年，David K. Gifford 发表了一篇《Weighted Voting for Replicated Data》的论文，详细阐述了一种被称作Quorum的算法用来保持分布式系统中复制副本的一致性。</p>
<p>在分布式系统中，为了保持数据的可用性，增加了更多的节点来并行处理相同的数据，并隐藏部分系统的故障。</p>
<h1 data-id="heading-2">🎏 02. Quorum的逻辑？</h1>
<ul>
<li>每个拥有文件的副本节点都有投票权,总结点为 n</li>
<li>我们设定每笔读事务收到的票数为 r，每笔写事务收到的票数为w，并且 r+w > n</li>
<li>然后，每对读/写集的交集为非空⇒ 每次读取都会看到至少一份写入的最新值</li>
</ul>
<p>如果我们假设r=1,w=n，那么集群就变成了WARO（Write All Read one）模式的完全副本模式，不过这个模式并不能实现高可用，因为只要其中一个节点故障，那么就会导致不能写入，只能读取。</p>
<p>最好的性能模式时 1<r<w<n, 就是2个读，3个写，总共4个节点。这主要是大部分的应用都是读多写少的。</p>
<h1 data-id="heading-3">🎏 03. Quorum的一般流程</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd605b809e08490fa3ba2f079536da1f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里引入了时间戳概念，记录数据的版本号，每个节点都需要自己维护。
只要达到读票数和写票数就认为成功了。内部无需再次同步。</p>
<ol>
<li>
<p>如何读取最新的数据？在已经知道最近成功提交的时间戳的前提下，最多读r个副本就可以读到最新的数据了。</p>
</li>
<li>
<p>如何确定最新时间戳的数据是一个成功提交的数据？继续读其他的副本，直到读到的时间戳出现了w次。</p>
</li>
</ol>
<h1 data-id="heading-4">🎏 04. Quorum的优化</h1>
<p>上述的一般流程，大部分情况没有问题。但在数据量非常大的时候，就不太适合了。这是可以引入数据的Hash值。</p>
<ul>
<li>将Hash与数据一起存储在每台服务器上</li>
<li>在读取操作期间返回哈希值和元数据（非数据）</li>
<li>根据Hash进行投票</li>
<li>确定正确的Hash后，向单个服务器查询数据对象</li>
<li>并计算其Hash以验证数据完整性</li>
</ul>
<h1 data-id="heading-5">🎏 05. 系统分析</h1>
<p>读性能： 需要读取节点的平均响应时间；
写性能： 需要写入的节点的平均响应时间；</p>
<p>虽然使用Quorum协议的集群内部并不是强一致性（所有节点都写入），但其保留了高可用性。作为一个黑盒子来看待，对外达到了强一致性和高可用性的效果。</p>
<h1 data-id="heading-6">🎏 06. 小结</h1>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            