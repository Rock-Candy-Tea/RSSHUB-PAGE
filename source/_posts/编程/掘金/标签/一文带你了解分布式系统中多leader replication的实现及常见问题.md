
---
title: '一文带你了解分布式系统中多leader replication的实现及常见问题'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0544105ddb954be29f3ef82df792309e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 18:57:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0544105ddb954be29f3ef82df792309e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我们在前面的文章中介绍的都是单leader的实现。也就是说所有的写操作都会通过这个leader来实现。虽然说这是一种比较常见的实现方法，但是它也尤其局限性，比如说leader可能会有问题，比如网络问题等，这个时候就会有一段时间没法进行写操作。或者说当写操作很重的时候，所有的写的load都需要到leader这边，无形中就加重了leader的traffic。本文就来介绍一种多leader的实现方案。</p>
<p>顾名思义，多leader实现方案就是可以同时有多个节点成为leader，所有的写操作可以同时通过这些节点来进行。当其中一个leader在写的时候，另外的leader就和follower一样，也需要从它这边进行replication。</p>
<h2 data-id="heading-0">多leader的使用场景</h2>
<p>多leader其实并不是一个比较常见的方案。那么一般在什么情况下，我们会考虑多leader的方案呢？</p>
<h2 data-id="heading-1">多数据中心的操作</h2>
<p>假如我们的数据库是在多个数据中心的时候（实际上为了防止但数据中心出问题，一般的数据库都会分布在不同的数据中心），假如使用单leader的实现，那么leader就会在一个数据中心，从而使得所有的写都得通过那个数据中心。</p>
<p>而假如是多leader的实现，我们就可以在每一个数据中心放一个leader，这样在每一个数据中心中，还是单leader的情况，但是这个数据库则是多leader的情况。具体的架构如下图所示：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0544105ddb954be29f3ef82df792309e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面我们来看看这样的实现有什么好处：</p>
<ul>
<li>性能</li>
</ul>
<p>单leader的情况下，所有的写都需要到leader那边，显然跨数据中心的访问性能不会很好。而多leader的情况下，所有的读操作可以直接访问本地的数据中心，虽然需要在数据中心进行数据replication，但是数据中心之间的延迟其实对用户来说是黑盒，所以对用户来说性能是有提升的。</p>
<ul>
<li>数据中心宕机的容忍性</li>
</ul>
<p>单leader的情况下，如果有数据中心宕机，那么需要通过failover来找到新的leader，然后可以继续服务。多leader的情况下，单个数据中心的宕机不影响整体的写操作，无需做额外的failover也可以继续进行写操作。</p>
<ul>
<li>网络问题的容忍性</li>
</ul>
<p>同样的，但leader其实受leader所在数据中心的网络情况所影响，而相对来说多leader则可以更好的容忍单个数据中心网络的问题。</p>
<p>虽然看起来多leader的实现有很多好处，但其实它也有其问题，那就是冲突写，比如两个写同时发生在两个不同的leader上，并且彼此冲突，该如何进行处理，这个问题我们后面会详细介绍一些处理的方案。</p>
<h2 data-id="heading-2">Offline操作的应用</h2>
<p>另外一个多leader replication常见的场景就是offline操作，比如你有一个应用哪怕没有网络也希望能够持续工作。</p>
<p>比如说你手机中的日历程序，你希望安排你的日程，比如添加事项，看看后面哪天有哪些安排。这些操作哪怕是在没有网络的时候也希望能够正常工作。只要当这个设备能够再次访问网络的时候我们能够成功同步这些就可以了。其实这就是一个多leader的场景，你可以把你的设备想象成一个数据中心，有网络的时候，就是正常的多leader同步。没有网络的时候，本地的leader也支持读、写操作。当再次有网络的时候能够做跨数据中心（设备）的replication。</p>
<h2 data-id="heading-3">协同写操作的应用</h2>
<p>另外一个常见的使用场景就是会有多人同时写一个文档。比如说Google Doc，它支持同时有多个人来编辑。这种常见就和上面的比较类似，我们不希望一个人的写去影响另外一个人的写，所以这里通常就会写入本地leader，然后进行多节点的同步。</p>
<h2 data-id="heading-4">处理写冲突</h2>
<p>我们上面提到多leader最大的问题就是写冲突，毕竟两个leader完全有可能同时修改同样的内容，如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4866e9b93f5434991b79158166a71d4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里User1通过Leader1修改了title到B，但是User2又通过leader2修改了title到C，这个时候在他们进行replication的时候就会出现了冲突的问题，究竟是该改成B还是改成C呢？</p>
<h2 data-id="heading-5">避免冲突</h2>
<p>假如我们现在能够想到一个简单的方法来避免冲突，那么这个问题就自然而然解决了。比如所有修改title的请求全部要到同一个leader来处理，这就可以规避掉上文提到的写冲突。这个方案还是蛮常见的，比如说用户的资料只能他自己能修改，而所有这个用户修改自己资料的请求我们全部指向同一个leader，这样就可以实现冲突的避免。</p>
<p>但是世事显然不会总是这么一帆风顺，比如说有时候某一个数据中心突然就出问题了，那么无可避免的，你就只能把所有的写操作都指向另外数据中心，这样就还是会出现写冲突。</p>
<h2 data-id="heading-6">收敛到一致状态</h2>
<p>多leader其实很难说谁是最后写的，所以最终应该是什么样的内容有时很难讲，就像上面的例子一样，你说最终title应该是B还是C呢？这个时候就需要一些额外手段来辅助判断：</p>
<ul>
<li>给每一个写一个独有的ID（比如使用timestamp，UUID等等），然后比较他们的大小。大得获胜。当这个ID使用的时间，那我们称这种方法为最后写的获胜（Last write wins LWW）。这个方法听起来不错，但也有其问题，我们在后面的文章中再具体讨论。</li>
<li>给每一个replica一个独有的ID，高number的replica总是能够覆盖低replica的写。这个方法也可能到数据的lost</li>
<li>把两者merge起来，按照一定的方法进行merge，比如上面的例子最终title就变成B/C</li>
<li>把所有的冲突记录下来，然后通过一定的工具来解决，甚至可以提醒用户自己来处理。</li>
</ul>
<h2 data-id="heading-7">多leader replication的拓扑结构</h2>
<p>Replication的拓扑结构是指如何把一个写操作传播到别的节点，假如你只有两个leader，那比较容易，就是相互传递就好了，leader1的写传到leader2，leader2的写传到leader1。但假如你有多个leader该怎么样呢？下图是一些常见的拓扑结构：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aebe4bf4584046eb936cf2fc276ece09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比较常见的拓扑结构就是如c所示的all-to-all，就是当有写的时候，一个leader会把它发送给所有的leader。当然也有如图a所示的，就是所有的leader是一个环，一个leader的写只会发送给它的下一个leader，然后再继续往下传递。最后还有一种是如图b所示的星型结构，就是所有的leader都是通过一个中心节点来传递的，然后再由这个中心节点把数据发送出去。</p>
<p>星型和环形结构是需要进行传递的，那么如何决定传还是不传（不能一直传），就需要一个id来区分自己是否已经传递过了，假如已经传递过了就不需要再继续了。它们的问题也很明显，就是单个leader的failure可能会导致后续所有的leader也lost这个数据。</p>
<p>那是不是说all-to-all的方式就最好呢，其实它也有其自身的问题。如下图所示，假如节点之间的通信速度不同，就会产生问题：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac08f4f8b1904e0797e48b31c5e17ff6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们看到在leader2上，由于leader1到它的速度比较慢，就导致了它先收到update然后才收到insert的操作。这显然不是我们想要的。解决这个问题的方法我们称之为version vector，这个会在后面的文章中再详细介绍。</p>
<h2 data-id="heading-8">总结</h2>
<p>本文介绍了多leader的概念以及其使用场景，并简单分析了这种实现可能遇到的问题和相应的常见解决方法。最后对其常见的三种拓扑结构做了一个介绍。</p></div>  
</div>
            